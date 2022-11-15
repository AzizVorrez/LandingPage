from django.http import HttpResponse
from django.shortcuts import render, redirect

def sendMessage_view(request):
    return redirect('')

def message_view(request):
    if request.POST == 'post':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_phone = request.POST['phone']
        message_subject = request.POST['subject']
        message_message = request.POST['message']

        context = {
            'name' : message_name,
            'email' : message_email,
            'phone' : message_phone,
            'subject' : message_subject,
            'message' : message_message,
        }
        
        return redirect('', context)

    else:
        return HttpResponse('Une erreur')