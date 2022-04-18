from django.contrib.auth import get_user_model
from django.db import models
from account.models import User


User_ = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('In stock', 'В наличии'),
    ('out of stock', 'Нет в наличии')
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='post')
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,)
    price = models.DecimalField(max_digits=15,
                                decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User_,
                               on_delete=models.CASCADE,
                               related_name='post')

    def __str__(self):
        return self.title

# 102
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class PostImg(models.Model):
    picture = models.ImageField(upload_to='post_media')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')