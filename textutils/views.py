from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>Hello</H1>")
