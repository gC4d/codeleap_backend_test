from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("posts.urls")),
    path("health/", health_check, name="health_check"),
]
