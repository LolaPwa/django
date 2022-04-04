from unicodedata import name
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Home, About, Profile, Category, Portfolio

from django.core.mail import send_mail

from django.template import loader
from django.core.mail import EmailMultiAlternatives
from .models import Contact

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()



    context = {
       'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
        
    }

    return render(request, 'index.html', context)  


#def contact(request):
 #    if request.method=="POST":
  #      contact=Contact()
   #     name=request.POST.get('name')
    #    email=request.POST.get('email')
     #   message=request.POST.get('message')
      #  contact.name=name
       # contact.email=email
        #contact.message=message
        #contact.save()
        #return HttpResponse("<h1> Thanks for contacting me</h1>")


def contact(request):
        if request.method == "POST":
         contact = Contact(name = request.POST.get('name'), email = request.POST.get('email'), message = request.POST.get('message'))
         contact.save()

         messages.success (request, "message sent successfully !")
         return HttpResponseRedirect('/')

#def send_mail(request):
    #name = request.POST.get('name')
    #email = request.POST.get('email')
    #message = request.POST.get('message')

    #template = loader.get_template('contact_form.txt')
    #context = {
       # 'name' : name,
      #  'email' : email,
     #   'message' : message,
    #}
    #message = template.render(context)
    #emil = EmailMultiAlternatives(
       # "Portfolio (message)", message,
      #  "New messages " + "- Customers",
     #   ['lolapwasanga.tech@gmail.com, email]']
    #)

    #email.content_subtype = 'html'
    #email.send()
    #messages.success(request, ',' )
   # return HttpResponseRedirect('/') 








