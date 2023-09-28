from django.shortcuts import HttpResponse


def home_view(request):
    return HttpResponse("<html><body>hello world</body></html>")
