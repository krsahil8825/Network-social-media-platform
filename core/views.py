from django.shortcuts import render

from .models import ContactMessage


# Home page view
def index(request):
    return render(request, "core/index.html")


# About page view
def about(request):
    return render(request, "core/about.html")


def error_404_view(request, exception=None):
    # custom 404 handler
    return render(request, "core/404.html", status=404)


# Contact page view
def contact(request):
    # handle form submit
    if request.method == "POST":

        # must be logged in
        if not request.user.is_authenticated:
            message_unsuccess = "You need to be logged in to send a message."
            return render(
                request,
                "core/contact.html",
                {"message_unsuccess": message_unsuccess},
                status=403,
            )

        # read form fields
        try:
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            user = request.user

            # trim input
            subject = subject.strip() if subject else ""
            message = message.strip() if message else ""

            # validation
            if not subject or not message:
                message_unsuccess = "Subject and message cannot be empty."
                return render(
                    request,
                    "core/contact.html",
                    {"message_unsuccess": message_unsuccess},
                )

            # check duplicates
            if ContactMessage.objects.filter(
                user=user, subject=subject, message=message
            ).exists():
                message_success = "You have already sent this message."
                return render(
                    request, "core/contact.html", {"message_success": message_success}
                )

            # save message
            ContactMessage.objects.create(user=user, subject=subject, message=message)
            message_success = "Your message has been sent successfully."
            return render(
                request, "core/contact.html", {"message_success": message_success}
            )

        except Exception as e:
            # fallback error
            print("Error:", e)
            message_unsuccess = "There was an error sending your message."
            return render(
                request, "core/contact.html", {"message_unsuccess": message_unsuccess}
            )

    # GET request → normal page render
    return render(request, "core/contact.html")
