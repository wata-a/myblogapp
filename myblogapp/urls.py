"""myblogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 他のファイルを使うので、includeを追加
from django.conf.urls import include, url
from django.contrib import admin

# staticファイルを読み込むためのパッケージをインポート
# 必ずstaticを先に！
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # urlにpostsが入っていたら、postsフォルダのurls.pyを呼び出す
    url(r'^posts/', include('posts.urls')),
    # urlにadminが入っていたら、admin.site.urlsを見に行く
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # （staticデータを表示するURLの設定, そのデータをどこに保持しているか）
    # document_root: staticファイルのいちばん上の階層をどこに置くのか

