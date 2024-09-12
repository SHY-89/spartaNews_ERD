from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
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

# Create your views here.
