from django.conf.urls import url
from . import views

app_name = 'article'  # 一定要写这一行，否则会报错 'article' is not a registered namespace

urlpatterns = [
    url(r'^article-column/$', views.article_column, name='article_column'),
]
