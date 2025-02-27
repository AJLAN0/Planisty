from django.shortcuts import render

from django.urls import reverse
from django.http import JsonResponse

def api_home(request):
    api_endpoints = {
        "Authentication": {
            "Register": request.build_absolute_uri(reverse('register')),
            "Login": request.build_absolute_uri(reverse('login')),
            #"Token Refresh": request.build_absolute_uri(reverse('token_refresh')),
        },
    }
    return JsonResponse(api_endpoints, safe=False)
