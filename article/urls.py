from django.conf.urls import url
from . import views

app_name = 'article'  # 一定要写这一行，否则会报错 'article' is not a registered namespace

urlpatterns = [
    url(r'^article-column/$', views.article_column, name='article_column'),
    url(r'^rename-article-column/$', views.rename_article_column, name='rename_article_column'),
    url(r'^del-article-column/$', views.del_article_column, name='del_article_column'),
    url(r'^article-post/$', views.article_post, name='article_post'),
]
