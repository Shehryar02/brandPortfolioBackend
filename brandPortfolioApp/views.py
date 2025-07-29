import threading
from django.core.mail import EmailMessage
from rest_framework import viewsets
from .models import ContactMessage, EmailFromFooter
from .serializers import ContactMessageSerializer, EmailFromFooterSerializer

# Utility function to send email in a thread
def send_email_async(email):
    try:
        email.send(fail_silently=True)
    except Exception as e:
        print("Email sending error:", str(e))

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Admin Notification
        admin_subject = "Message via Contact - Senvotex"
        admin_body = f"""
Name: {instance.first_name} {instance.last_name}
Email: {instance.email}
Phone: {instance.phone}
Subject: {instance.subject}

Message:
{instance.message}
"""
        admin_email = EmailMessage(
            subject=admin_subject,
            body=admin_body,
            from_email="Senvotex-Contact <digital@senvotex.com>",
            to=["senvotex@gmail.com"]
        )
        threading.Thread(target=send_email_async, args=(admin_email,)).start()

        # Auto-response to User
        user_subject = "Thank you for contacting Senvotex!"
        user_body = f"""Dear {instance.first_name},

Thank you for reaching out to Senvotex. We have received your message and our team will get back to you shortly.

Here’s a copy of your message:
----------------------------------------
Subject: {instance.subject}
Message: {instance.message}
----------------------------------------

Best regards,  
Team Senvotex  
senvotex@gmail.com
"""
        user_email = EmailMessage(
            subject=user_subject,
            body=user_body,
            from_email="Senvotex <digital@senvotex.com>",
            to=[instance.email]
        )
        threading.Thread(target=send_email_async, args=(user_email,)).start()


class EmailFooterViewSet(viewsets.ModelViewSet):
    queryset = EmailFromFooter.objects.all()
    serializer_class = EmailFromFooterSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Notify Admin
        admin_subject = "New Email via Footer - Senvotex"
        admin_body = f"New user subscribed with email: {instance.email}"

        admin_email = EmailMessage(
            subject=admin_subject,
            body=admin_body,
            from_email="Senvotex-Footer <digital@senvotex.com>",
            to=["senvotex@gmail.com"]
        )
        threading.Thread(target=send_email_async, args=(admin_email,)).start()

        # Auto-reply to the user
        user_subject = "Thanks for connecting with Senvotex!"
        user_body = f"""Hi there,

Thank you for staying connected with Senvotex. We'll keep you updated with our latest news and services.

Best regards,  
Senvotex Team"""
        user_email = EmailMessage(
            subject=user_subject,
            body=user_body,
            from_email="Senvotex <digital@senvotex.com>",
            to=[instance.email]
        )
        threading.Thread(target=send_email_async, args=(user_email,)).start()
