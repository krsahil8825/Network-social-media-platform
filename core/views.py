from django.shortcuts import render

from .models import ContactMessage


# Home page view
def index(request):
    return render(request, "core/index.html")


# About page view
def about(request):
    return render(request, "core/about.html")


def error_404_view(request, exception=None):
    return render(request, "core/404.html", status=404)


# Contact page view
def contact(request):
    # Handle contact form submission
    if request.method == "POST":

        # Check if user is authenticated
        if not request.user.is_authenticated:
            message_unsuccess = "You need to be logged in to send a message."
            return render(
                request, "core/contact.html", {"message_unsuccess": message_unsuccess}
            )

        # Process the form data
        try:
            # Extract form data
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            user = request.user

            subject = subject.strip() if subject else ""
            message = message.strip() if message else ""

            # Validate data
            if not subject or not message:
                message_unsuccess = "Subject and message cannot be empty."
                return render(
                    request,
                    "core/contact.html",
                    {"message_unsuccess": message_unsuccess},
                )

            # Check for duplicate messages
            if ContactMessage.objects.filter(
                user=user, subject=subject, message=message
            ).exists():
                message_success = "You have already sent this message."
                return render(
                    request, "core/contact.html", {"message_success": message_success}
                )

            # Save the message to the database
            ContactMessage.objects.create(user=user, subject=subject, message=message)
            message_success = "Your message has been sent successfully."
            return render(
                request, "core/contact.html", {"message_success": message_success}
            )

        # Handle unexpected errors
        except Exception as e:
            print("Error:", e)
            message_unsuccess = "There was an error sending your message."
            return render(
                request, "core/contact.html", {"message_unsuccess": message_unsuccess}
            )

    # For GET requests, simply render the contact page
    return render(request, "core/contact.html")
