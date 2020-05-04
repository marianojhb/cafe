from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    if request.method == 'POST':
        email_name = request.POST["email_name"]
        email_address = request.POST["email_address"]
        email_message = request.POST["email_message"]
    
        # EmailMessage(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
        email = EmailMessage(
            subject="Consulta", 
            body = f"{email_name} <{email_address}>\n{email_message}",
            from_email = email_address,
            to=['mbelgrano@gmail.com'],
            reply_to=[email_address]
        )
        email.send(fail_silently=False)
        return render(request, 'contact/message_sent.html')
    return render(request, "contact/contact.html")

