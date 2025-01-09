from django.urls import path
from .views import (
    TestCeleryView,
    TestingDockerView,
)

urlpatterns = [
    path('test-celery/', TestCeleryView.as_view(), name='test_celery'),
    path('testing/', TestingDockerView.as_view(), name='test_celery'),
]
