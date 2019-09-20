from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from dataapis import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'outdoordate', views.OutdoorDateViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('api-auth', include('rest_framework.urls')),
  path('token-auth-pair/', TokenObtainPairView.as_view()),
  path('token-auth-refresh/', TokenRefreshView.as_view()),
  path('current-user', views.currentUserDetail),
  path('users', views.UserList.as_view()),
  
  re_path(r'outdoordate/(\d+)/', include('dataapis.urls2')),
  re_path(r'outdoordate/', include('dataapis.urls2')),
]