from django.conf.urls import url
from . import views

app_name = 'image'  # 一定要写这一行，否则会报错 'image' is not a registered namespace

urlpatterns = [
    url(r'^list-images/$', views.list_images, name="list_images"),
    url(r'^upload-image/$', views.upload_image, name="upload_image"),
    url(r'^del-image/$', views.del_image, name="del_image"),
]
