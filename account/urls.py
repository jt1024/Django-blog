from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'account'

urlpatterns = [
    # url(r'^login/$', views.user_login, name="user_login"),
    # url(r'^login/$', LoginView.as_view(), name="user_login"),
    url(r'^login/$', LoginView.as_view(template_name="account/login.html"), name="user_login"),

    # url(r'^logout/$', LogoutView.as_view(), name="user_logout"),
    url(r'^logout/$', LogoutView.as_view(template_name="account/logout.html"), name="user_logout"),

    url(r'^register/$', views.user_register, name="user_register"),

    url(r'^password-change/$', PasswordChangeView.as_view(template_name="account/password_change_form.html",
                                                          success_url="/account/password-change-done"),
        name="password_change"),

    url(r'^password-change-done/$', PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),
        name="password_change_done"),

    url(r'^password-reset/$', PasswordResetView.as_view(template_name="account/password_reset_form.html",
                                                        email_template_name="account/password_reset_email.html",
                                                        subject_template_name='account/password_reset_subject.txt',
                                                        success_url='/account/password-reset-done/'),
        name='password_reset'),

    url(r'^password-reset-done/$', PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
        name='password_reset_done'),

    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",
                                         success_url='/account/password-reset-complete/'),
        name="password_reset_confirm"),

    url(r'^password-reset-complete/$',
        PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
        name='password_reset_complete'),

]
