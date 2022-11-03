from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['POST'])
def calculator(request):
    try:
        result = None
        if request.method == "POST":
            operation = request.POST["operation"]
            no1 = int(request.POST["no1"])
            no2 = int(request.POST["no2"])

            if operation == '+':
                result = no1 + no2
            elif operation == '-':
                result = no1 - no2
            elif operation == '*':
                result = no1 * no2
            elif operation == '/':
                result = no1 / no2

        return JsonResponse({"result": result})
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)