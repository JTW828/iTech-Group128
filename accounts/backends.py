from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # 先尝试用 email 查找
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)  # 再尝试用 username 查找
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user
        return None
