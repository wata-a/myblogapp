# djangoのdbからmodelsクラスをインポート
from django.db import models

# Create your models here.
# modelsクラスのModelというテンプレートを使う
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    # upload_to: データを保存するためのフォルダを指定
    image = models.ImageField(upload_to='media/')
    body = models.TextField()


    # Classには属性値（プロパティ）だけでなく、命令（関数）も持たせられる
    # __str__: 文字列をページに返す
    # return self.titleでPostクラスに定義したtitleが返るようになる
    def __str__(self):
        return self.title

    def summary(self):
        # [:100]：先頭から100文字取得
        return self.body[:30]