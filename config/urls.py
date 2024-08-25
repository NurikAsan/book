from django.contrib import admin
from django.urls import path
from rest_framework import routers

from apps.store import views

router = routers.SimpleRouter()

router.register(r'book', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
