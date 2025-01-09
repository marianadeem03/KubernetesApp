from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import hello_task


# Create your views here.

class TestCeleryView(APIView):
    @staticmethod
    def get(request):
        result = hello_task.delay()  # Trigger the Celery task
        return Response({"message": "Task has been triggered", "task_id": result.id})


class TestingDockerView(APIView):
    @staticmethod
    def get(request):
        return Response("Okay")
