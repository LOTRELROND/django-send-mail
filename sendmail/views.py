from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

#mail
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        age = form.cleaned_data.get("age")
        mail = form.cleaned_data.get("mail")
        form.save()

        email_body = ("hi " + first_name + " " + last_name + ", you've emailed for your applied our project." )


        # host@gmail.com should be email host users gmail like settings.py
        try:
            send_mail('You contacted us!',email_body,
                        'host@gmail.com',
                         [mail])
        
            messages.success(request, "mail sent." )

            return redirect("index")
        except:
            messages.error(request, "mail couldn't be send")

            return redirect("index")
        
    
    return render(request, 'index.html', {"form": form})