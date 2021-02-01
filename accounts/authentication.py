from accounts.models import Token,User
from django.contrib.auth.backends import ModelBackend
from django.contrib import auth
import sys
class PasswordlessAuthenticationBackend(ModelBackend):
    def authenticate(self,uid):
        try:
            token=Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None
    def get_user(self,email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
    def login(self,request,user):
        auth.login(request,user)
    def logout(self,request):
        auth.logout(request)