from django.contrib import admin
from django.urls import path
from accounts import views
from allauth.account.views import LogoutView
from allauth.socialaccount.views import ConnectionsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page_view, name='main_page'),
    path('kakao_login/', views.kakao_login_view, name='kakao_login'),
    path('kakao_profile/', views.profile_view, name='kakao_profile'),
    path('disconnect_kakao/', views.disconnect_kakao, name='disconnect_kakao'),  # 추가된 URL
    path('logout/', LogoutView.as_view(), name='logout'),
    path('social/connections/', ConnectionsView.as_view(), name='connections'),
    path('accounts/kakao/login/callback/', views.KakaoLogin.as_view(), name='kakao_login_callback'),  # 추가된 URL
]
