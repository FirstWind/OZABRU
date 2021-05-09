from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # path('', include(router.urls)),
    # path to djoser end points
    path('auth/', include('djoser.urls')),  # создание нового Usera /auth/users/
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),  # залогинивание Usera /auth/jwt/create
    path('auth/', include('rest_framework_social_oauth2.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),

    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/digest/', include('backend.digest.urls')),
    path('api/v1/event/', include('backend.event.urls')),
    path('api/v1/club/', include('backend.club.urls')),
    path('api/v1/category/', include('backend.sports_category.urls')),
    path('api/v1/registration/', include('backend.registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
