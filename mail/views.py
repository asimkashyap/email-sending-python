from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.


def index(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        print(sub, msg, email)
        send_mail(
            sub, msg, 'asimji29@gmail.com', [email]

        )
        return HttpResponse('email sent successfully')

    return render(request, 'home.html')
