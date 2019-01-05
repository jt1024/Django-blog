app_name = 'account'

from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # url(r'^login/$', views.user_login, name="user_login"),
    # url(r'^login/$', LoginView.as_view(), name="user_login"),
    url(r'^login/$', LoginView.as_view(template_name="account/login.html"), name="user_login"),
    # url(r'^logout/$', LogoutView.as_view(), name="user_logout"),
    url(r'^logout/$', LogoutView.as_view(template_name="account/logout.html"), name="user_logout"),
    url(r'^register/$', views.user_register, name="user_register"),

]
