from django.urls import path, include
from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='home'),
    path('login1/', views.login1, name='login1'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout, name = 'logout'),
    path('password/', views.change_password, name='change_password'),
    


    #path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


   

     path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password_reset_form.html',
             subject_template_name='commons/password_reset_subject.txt',
             email_template_name='commons/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons//password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
]                 