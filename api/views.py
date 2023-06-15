
from django.http import JsonResponse
from rest_framework.decorators import api_view
import random

@api_view(['GET'])
def my_view(request):
    if request.method == 'GET':
        data = {
            "key1": random.randint(1, 1000),
            "key2": "value2"
        }
        return JsonResponse(data)

