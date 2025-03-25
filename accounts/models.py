from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class Store(models.Model):
    name = models.CharField(max_length=255) 
    city = models.CharField(max_length=100) #商店所在城市
    address = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    introduction = models.TextField(blank=True)
    image = models.ImageField(upload_to="store_images/") #商店图片
    sub_image1 = models.ImageField(upload_to='store_images/', blank=True, null=True)
    sub_image2 = models.ImageField(upload_to='store_images/', blank=True, null=True)



    def __str__(self):
        return self.name


class Favourite(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="favourites")  # FK 关联 Store
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # FK 关联 User
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('store', 'user')  # 防止重复收藏

    def __str__(self):
        return f"{self.user.username} likes {self.store.name}"


class Like(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="likes")  # FK 关联 Store
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # FK 关联 User
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('store', 'user')

    def __str__(self):
        return f"{self.user.username} liked {self.store.name}"
    

class Comment(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="comments")  # 关联商店
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 关联用户
    content = models.TextField()  # 评论内容
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return f"{self.user.username} commented on {self.store.name}"