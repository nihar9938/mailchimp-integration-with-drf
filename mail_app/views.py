from rest_framework import status
from mailchimp_marketing import Client
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from mailchimp_marketing.api_client import ApiClientError
from mailchimp_integration.settings import (
                                            MAILCHIMP_API_KEY,
                                            MAILCHIMP_DATA_CENTER,
                                            MAILCHIMP_LIST_ID,
                                            )



class MailSubscriptionAPIView(GenericAPIView):

    def subscribe_email(email):
        """
        This function will communicate with mailchimp api
        to create a member in an audience list
        """
        mailchimp = Client()
        mailchimp.set_config({
            "api_key": MAILCHIMP_API_KEY,
            "server": MAILCHIMP_DATA_CENTER
        })
        member_info = {
            "email_address": email,
            "status": "subscribed",
        }
        try:
            mailchimp.lists.add_list_member(MAILCHIMP_LIST_ID, member_info)
        except ApiClientError as error:
            print(error.text)

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        MailSubscriptionAPIView.subscribe_email(email)
        return Response({
                "status_code": status.HTTP_200_OK,
                "message": "Mail added to mailchimp"
            })