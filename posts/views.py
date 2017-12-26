from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# models.pyからPostのクラス定義を取り出す
from .models import Post

# indexで呼ばれたページの内容をレンダリング（整形）する前に、Postから取り出した値をテンプレートに添えて転送する
# ビュー関数の引数は慣習的にrequest
def index(request):
    # index.htmlを読みに行き、ブラウザに戻す
    # Postクラスの全てのオブジェクトを取り出し、公開日の降順でソート
    posts = Post.objects.order_by('-published')
    # return HttpResponse("HelloWorld!　このページは投稿のインデックスです。")
    # views.pyが呼ばれたときに、外部のin
    # {'posts': posts}: {'テンプレ内での変数名': 渡す変数名}
    # render関数は、request、テンプレートパスを渡すとそのテンプレートを使用したレンダリング結果をHttpResponseとして介してくれる
    return render(request, 'posts/index.html', {'posts':posts})

def post_detail(request,post_id):
    # post = Post.objects.get(pk=post_id)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html',{'post':post})


# Create your views here.

