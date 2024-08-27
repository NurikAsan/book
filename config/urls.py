from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.store import views

router = routers.SimpleRouter()

router.register(r'book', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', views.auth)
]

urlpatterns += router.urls
