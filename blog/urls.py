from django.conf.urls import url
from . import views

app_name = 'blog'  # 一定要写这一行，否则html中的 href="{% url 'blog:blog_title' %}" 会报错 'blog' is not a registered namespace

urlpatterns = [
    url(r'^$', views.blog_title, name='blog_title'),
    url(r'(?P<article_id>\d)/$', views.blog_article, name='blog_detail'),
]
