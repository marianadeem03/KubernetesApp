from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import hello_task


# Create your views here.

class TestCeleryView(APIView):
    def get(self, request, *args, **kwargs):
        result = hello_task.delay()  # Trigger the Celery task
        return Response({"message": "Task has been triggered", "task_id": result.id})

