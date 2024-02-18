import base64
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt

from .utils import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def logout(request):
    return redirect("logout")


@csrf_exempt
def find_user_view(request):
    photo = request.POST.get("photo")
    print(photo)
    _, img = photo.split(";base64")
    decodedFile = base64.b64decode(img)
    l = Log()
    l.photo = ContentFile(decodedFile, "upload.png")
    l.save()
    res = classify_face(l.photo.path)
    user_exists = User.objects.filter(username=res).exists()
    if user_exists:
        user = User.objects.get(username=res)
        profile = Profile.objects.get(user=user)
        l.profile = profile
        l.save()

        login(request, user)
        return JsonResponse({"success": True})
    return JsonResponse({"status": True})
