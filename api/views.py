from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes

@api_view(['GET'])
@permission_classes(())
def index(request):
    return JsonResponse({'status': 'OK'}, status=status.HTTP_200_OK)
