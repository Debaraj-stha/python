from django.shortcuts import render, redirect, HttpResponse
from my_app.forms import multipleImageUploadForm
from my_app.models import User, multipleImageUpload
from django.core import serializers
from django.db.models import Count, F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import randint
from django.conf import settings
import http.client
import requests
import random
from django.shortcuts import render, redirect

# from django_otp.plugins.otp_totp.models import TOTPDevice
from twilio.rest import Client
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    users = User.objects.all()
    userList = []
    i = 0
    request.session["name"] = "Devraj Shrestha"
    for u in users:
        print(u.pk)
        userImage = multipleImageUpload.objects.filter(userId=u)
        user = {
            "image": list(userImage),
            "name": u.name,
        }
        print(list(userImage))
        userList.insert(i, user)
        i = i + 1

    # Print userList to see its contents
    print("user list" + str(userList))

    # Print user details and images
    for u in userList:
        print("Name:", u["name"])
        for image in u["image"]:
            print(
                "Image:", image.images
            )  # Access the 'images' attribute of the Image model

    # Grouping and aggregation
    grouped_queryset = User.objects.annotate(
        image_count=Count("multipleimageupload")
    ).values("name", "email", "address", "image_count")

    # Iterate through the grouped results
    for user in grouped_queryset:
        user_name = user["name"]
        user_email = user["email"]
        user_address = user["address"]
        image_count = user["image_count"]
        # print(f"User: {user_name}, Email: {user_email}, Address: {user_address}, Image Count: {image_count}")

    # user=User(name="mand",email="mandi@gmail.com",address="dharam")
    # user.save()
    # users = User.objects.all()
    # print(serializers.serialize("json", users))
    orderBy = multipleImageUpload.objects.order_by("pk")[:10]
    # Grouping and aggregation
    grouped_queryset = multipleImageUpload.objects.values("userId__name").annotate(
        image_count=Count("userId")
    )

    # Iterate through the grouped results
    # for entry in grouped_queryset:
    #     user_name = entry['userId__name']
    #     image_count = entry['image_count']
    #     print(f"User: {user_name}, Image Count: {image_count}")

    # print(serializers.serialize("json", orderBy))
    print("\n\n\n\n\n")
    if request.session.__contains__("name"):
        request.session.__delitem__("name")
        request.session.__setitem__("phone", 999999)
        print("name is in session")
    # name=request.session.get('name')
    # print("sessiin name is" + name)
    return render(
        request,
        "home.html",
    )


def multipleImageUploaded(request):
    m = multipleImageUpload.objects.select_related("userId").filter(userId=2)

    if m.exists():
        x = m.first()
        print(x.userId.name)

    if request.method == "POST":
        form = multipleImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.filter(id=2)
            for image in request.FILES.getlist("images"):
                if user.exists():
                    u = user.first()
                    print(u.pk)
                    multipleImageUpload.objects.create(images=image, userId=u)
            m = multipleImageUpload.objects.filter(userId=u)
            print(serializers.serialize("json", m))
            form.save()
            print("saved")
            return redirect("multipleImageUploaded")
        else:
            print(form.errors)
            return redirect("multipleImageUploaded")

    return render(request, "uploadMultipleImage.html")


@api_view(["POST"])
# views.py


def send_otp(request):
    if request.method == "POST":
        data = request.data
        phone_number = data.get("phone_number")

        # Generate a random OTP
        otp = str(random.randint(100000, 999999))

        # Send the OTP via MSG91 API
        url = "https://api.msg91.com/api/v5/otp"
        headers = {"authkey": settings.MSGAUTHKEY}
        data = {
            "otp": otp,
            "mobile": phone_number,
            "message": f"Your OTP is: {otp}",
            "sender": "jeevan",
            "otp_expiry": 5,  # OTP expiration in minutes
            "otp_length": 6,  # Length of the OTP
        }
        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()
        print(response_data)
        if response_data.get("type") == "success":
            # Successful OTP send
            request.session["otp"] = otp
            request.session.set_expiry(settings.OTP_EXPIRATION_TIME)
            return Response({"status": 200, "status": "success"})
        else:
            # OTP send failed
            return Response({"status": 200, "status": "failed"})
@api_view(['POST'])
def sendOTPToEmail(request):
    data=request.data
    email=data.get("email")
    print("email" + str(email))
    if email is None:
        return Response({"status":200,"message":"email is required"})
    else:
        otp=str(randint(100000,999999))
        # subject = 'Hello from Django Email'
        # message = 'This is a test email sent from a Django application.'
        # from_email = settings.EMAIL_HOST_USER
        # recipient_list = [email]

        # response=send_mail(subject, message, from_email, recipient_list)

        subject = 'Hello from Django Email with HTML'
        message = f'<div><p>This is an <strong>HTML</strong> email sent from a Django application.</p><div style="margin-top:20px" >{otp}</div></div>'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=message)

        return Response({"message":"Email sent successfully!","status":200})
