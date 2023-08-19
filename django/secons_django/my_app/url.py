from django.urls import path
from my_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="home"),
    path('send_otp',views.send_otp,name="send_otp"),
    path('multiple-image-upload',views.multipleImageUploaded,name="multipleImageUploaded"),
    path("send-otp-mail",views.sendOTPToEmail,name="sendOTPToEmail"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
