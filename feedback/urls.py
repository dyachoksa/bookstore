from django.urls import path

from .views import ContactUsView

app_name = "feedback"

urlpatterns =[
    path("contact-us/", ContactUsView.as_view(), name="contact-us"),
]