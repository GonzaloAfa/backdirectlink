from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template

from django.core.mail import EmailMessage, EmailMultiAlternatives

def index(request):

    send_contact();

    return HttpResponse("Send Email")


def send_contact():

    mail = EmailMultiAlternatives(
        subject="Contacto DirectLink",
        body="Contacto",
        from_email="Directlink <contacto@directlink.cl>",
        to=["gonzalo@afachile.cl"],
        headers={"Reply-To": "ventas@directlink.cl"}
    )

    template = get_template('emails/contact.html')

    context = Context({ 'name': "Gonzalo", 'email': "test@afachile.cl",
                       'msg': "A cuanto tiene los nsm5?",})

    html = template.render(context)
    mail.attach_alternative(html, "text/html")
    mail.send()
