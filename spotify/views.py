from django.shortcuts import HttpResponse


def home_view(request):
    return HttpResponse("hello world")
