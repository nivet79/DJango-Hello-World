from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>Hello world, kakrot, testing</H1>")
