from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Post API',
        default_version='v1',
        description='Test description',
        terms_of_service='demo service',
        contact=openapi.Contact('aa2004bek@gmail.com'),
        license=openapi.License(name='Demo License')
    ),
    public=True,
    permission_classes = [permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
    path('api/v1/',include('posts.urls')),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger'),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/',include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),
]
