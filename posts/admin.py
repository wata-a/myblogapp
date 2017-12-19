from django.contrib import admin

# Register your models here.
# 同じディレクトリのmodels.pyからPostモデルをimport
from .models import Post

admin.site.register(Post)