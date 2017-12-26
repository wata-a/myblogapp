from django.conf.urls import url
from django.views.generic import TemplateView
# 同じ階層からviews.pyを読み込み
from . import views

app_name = "posts"
# r:正規表現（パターン一致）
# 特に指定がない場合にはr'^$'を引数に。
# 特にurlの指定がない場合には、viewsのindex関数を渡す
urlpatterns = [url(r'^$', views.index, name = 'index')]
# urlpatterns = [url(r'^$', index.as_view(), name = 'index')]