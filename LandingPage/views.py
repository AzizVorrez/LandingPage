from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from . import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

def subscribe(mail):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": mail,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))



def home_view(request):
    return render(request, 'index.html')


def newsletter_view(request):
    if request.method == "POST":
        mail = request.POST.get('news_mail')
        subscribe(mail)                    # function to access mailchimp
        messages.success(request, "Email received. thank You! ") # message

    return render(request, 'index.html')



def message_view(request):

    if request.method == "POST":
        message_name = request.POST.get('name')
        message_email = request.POST.get('email')
        message_phone = request.POST.get('phone')
        message_subject = request.POST.get('subject')
        message_message = request.POST.get('message')

        send_mail(
            message_subject,
            message_message,
            message_email,
            ["azizvorrez8@gmail.com"],
        )

        context = {
            'name' : message_name,
            'email' : message_email,
            'phone' : message_phone,
            'subject' : message_subject,
            'message' : message_message,
        }

        return render(request, 'index.html')
    
    else:
        return redirect('/')