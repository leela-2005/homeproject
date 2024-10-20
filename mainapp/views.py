from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Prepare email details
        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['your_email@gmail.com']  # Your email address

        # Send email
        send_mail(subject, body, from_email, recipient_list)

        return HttpResponse(f"Thank you for your message, {name}! We will get back to you shortly.")

    return render(request, 'contact_us.html')
    
