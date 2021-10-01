from django.contrib import admin
from django.urls import path,include
from dungeon.views import LandingView
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,\
    PasswordResetConfirmView,PasswordResetCompleteView
from dungeon.raznoe import CustomLogout,Signup



urlpatterns = [
    path('admin/', admin.site.urls),
    path('zayavki/', include('dungeon.urls',namespace='zayavki')),
    path('',LandingView.as_view(),name='landing-p'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', CustomLogout.as_view(), name='logout'),
    path('signup', Signup.as_view(), name='signup'),
    path('reset-password', PasswordResetView.as_view(), name='reset_password'),
    path('reset-done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
