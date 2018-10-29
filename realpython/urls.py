from django.urls import path

from .views import index, crawl, get_status

urlpatterns = [
    path('', index),
    path('crawl/', crawl),
    path('get-status/', get_status),
]
