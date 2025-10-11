from django.contrib import admin
from django.urls import path, include
from my_portfolio.views import api_root_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Portfolio API",
      default_version='v1',
      description="API documentation for portfolio",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tazulislam42609770@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', api_root_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls'), name='api-root'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
