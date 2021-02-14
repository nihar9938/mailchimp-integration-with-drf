from django.urls import path
from .views import MailSubscriptionAPIView


urlpatterns = [
    path('subscribe_email', MailSubscriptionAPIView.as_view(), name= 'subscribe-email' ),
]