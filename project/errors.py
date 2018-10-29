from django.shortcuts import render


def handler404(request):
    return render(request, 'backend/errors/404.html', status=404)


def handler500(request):
    return render(request, 'backend/errors/500.html', status=500)
