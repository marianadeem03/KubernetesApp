from django.urls import path
from .views import TestCeleryView

urlpatterns = [
    path('test-celery/', TestCeleryView.as_view(), name='test_celery'),
]
