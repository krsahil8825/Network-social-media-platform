from django.shortcuts import render

from .models import ContactMessage

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    if request.method == "POST":
        if not request.user.is_authenticated :
            message_unsuccess = "You need to be logged in to send a message."
            return render(request, "core/contact.html", {"message_unsuccess": message_unsuccess})
        try:
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            user = request.user
            ContactMessage.objects.create(user=user, subject=subject, message=message)
            message_success = "Your message has been sent successfully."
            return render(request, "core/contact.html", {"message_success": message_success})
        except Exception as e:
            print("Error:", e)
            message_unsuccess = "There was an error sending your message."
            return render(request, "core/contact.html", {"message_unsuccess": message_unsuccess})
    return render(request, "core/contact.html")