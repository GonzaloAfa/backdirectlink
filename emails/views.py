import json
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template

from django.core.mail import EmailMessage, EmailMultiAlternatives

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
def index(request):

    if request.method == 'GET':
        print "GET"
        name    = request.GET.get('name', False)
        email   = request.GET.get('email', False)
        msg     = request.GET.get('msg', False)

        send_contact(name, email, msg);

    if request.method == 'POST':
        print "POST"
        json_data = json.loads(request.body)

        try:
            print json_data
            name    = json_data['name']
            email   = json_data['email']
            msg     = json_data['msg']

            send_contact(name, email, msg);

        except KeyError:
            HttpResponseServerError("Malformed data!")

        HttpResponse("Got json data")

    return HttpResponse("Send")


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
