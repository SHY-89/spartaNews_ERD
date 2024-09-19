from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserProfileSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
import re
from django.conf import settings
from .models import User

# 회원 가입
class Signup(APIView):
    # 검증 과정.
    def post(self,request):
        username = request.data.get('username') if request.data.get('username') else ''
        password = request.data.get('password') if request.data.get('password') else ''
        password_ok = request.data.get('password_ok') if request.data.get('password_ok') else ''
        error = ''
        
        if len(username)<5 or not re.search(r"[a-zA-Z0-9]", username):
            return Response({'error':'영문 및 숫자만 가능. 5자 이상'},status=400)
        if password_ok != password:
            return Response({'error':'비밀번호가 다릅니다.'}, status=400)
        # 비밀번호 검증
        if not re.search(r"[a-zA-Z]", password):
            error = "비밀번호는 하나 이상의 영문이 포함되어야 합니다."
        if not re.search(r"\d", password):
            error = "비밀번호는 하나 이상의 숫자가 포함되어야 합니다."
        if not re.search(r"[!@#$%^&*()]", password):
            error = "비밀번호는 적어도 하나 이상의 특수문자(!@#$%^&*())가 포함되어야 합니다."

        if error != '':
            return Response({'error':error},status=400)
        
        # 유저 검증 통과 시,
        user=User.objects.create_user(username=username,password=password)
        return Response(status=200)


# profile 조회
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def patch(self, request, username):
        user = get_object_or_404(User, username=username)
        if user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            email = request.data.get('email')
            if email and email != user.email and User.objects.filter(email=email).exists():
                return Response({'message': '이미 사용중인 이메일입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            if request.data.get('new_password'):
                new_password = request.data.get('new_password') # 패스워드 이름
                cf_password = request.data.get('cf_password')
                if cf_password != new_password:
                    return Response({'message': '동일하지 않은 password입니다.'}, status=status.HTTP_400_BAD_REQUEST)
                        # 비밀번호 검증
                error = ''
                if not re.search(r"[a-zA-Z]", new_password):
                    error = "비밀번호는 하나 이상의 영문이 포함되어야 합니다."
                if not re.search(r"\d", new_password):
                    error = "비밀번호는 하나 이상의 숫자가 포함되어야 합니다."
                if not re.search(r"[!@#$%^&*()]", new_password):
                    error = "비밀번호는 적어도 하나 이상의 특수문자(!@#$%^&*())가 포함되어야 합니다."
                if error != '':
                    return Response({'error':error},status=400)
                user.set_password(new_password)
            user.save()
            serializer.save()
            return Response({'message': '프로필이 업데이트 되었습니다.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.


class SendEmail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        self.object = request.user
        if not request.user.email:
            return Response("먼저 이메일을 등록 하셔야합니다.",status=400)
        send_mail(
            '{}님의 회원가입 인증메일 입니다.'.format(self.object.username),
            None,
            settings.EMAIL_HOST_USER,
            [request.user.email],
            html_message=render_to_string('accounts/email_verification.html', {
                'user': self.object,
                'uid': urlsafe_base64_encode(force_bytes(self.object.pk)).encode().decode(),
                'domain': self.request.META['HTTP_HOST'],
                'token': default_token_generator.make_token(self.object),
            }),
        )
        return Response()

def activate(request, uid64, token):
    message = "메일 인증에 실패했습니다."
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        current_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
        context = {
            "message": message
        }
        return render(request,"accounts/email_status.html",context)

    if default_token_generator.check_token(current_user, token):
        # current_user.is_active = True
        # current_user.save()
        message = "메일 인증에 성공했습니다."
    
    context = {
        "message": message
    }
    return render(request,"accounts/email_status.html",context)