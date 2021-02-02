from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Photo(models.Model):
    """画像"""

    title = models.CharField('写真タイトル', max_length=150)
    comment = models.TextField('コメント(空欄可)', blank=True)
    image = models.ImageField('画像', upload_to='photos/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', auto_now=True)

    def __str__(self):
        return self.title




