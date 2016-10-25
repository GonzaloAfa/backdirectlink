from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template

from django.core.mail import EmailMessage, EmailMultiAlternatives

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
def index(request):

    if request.method == 'POST':
        name    = request.POST.get('name', False)
        email   = request.POST.get('email', False)
        msg     = request.POST.get('msg', False)

        send_contact(name, email, msg);

    return HttpResponse("Send Email")


def send_contact(name, email, msg):

    mail = EmailMultiAlternatives(
        subject="Contacto DirectLink",
        body="Contacto",
        from_email="Directlink <contacto@directlink.cl>",
        to=["gonzalo@afachile.cl"],
        headers={"Reply-To": "ventas@directlink.cl"}
    )

    template = get_template('emails/contact.html')

    context = Context({
            'name': name,
            'email': email,
            'msg': msg })

    html = template.render(context)
    mail.attach_alternative(html, "text/html")
    mail.send()
