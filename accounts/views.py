from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import UserProfileSerializer, UserSerializer
from .models import User
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

import re

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
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            email = request.data.get('email')
            if email and email != user.email and User.objects.filter(email=email).exists():
                return Response({'message': '이미 사용중인 이메일입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            if request.data.get('old_password'):
                old_password = request.data.get('old_password')
                new_password = request.data.get('new_password')
                if new_password != old_password:
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


class TestEmail(APIView):
    def get(self, request):
        from django.core.mail import send_mail
        send_mail(
            "Subject here",
            "Here is the message.",
            "tjduwkrn@gmail.com",
            ["tjduwkrn@naver.com"],
            fail_silently=False,
        )
        return Response()