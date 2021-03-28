from django.contrib.flatpages.views import flatpage
from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('about-us/', flatpage, {'url': '/about-us/'}, name='about'),
    path('terms/', flatpage, {'url': '/terms/'}, name='terms'),
    path('<path:url>', flatpage, name='page'),
]
