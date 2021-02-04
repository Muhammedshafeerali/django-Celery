from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_review_email(name, email_list, review):

    for email in email_list:


        context = {
            'name': name,
            'email': email,
            'review': review,
        }

        email_subject = 'Thank you for your review'
        email_body = render_to_string('email_message.txt', context)

        email = EmailMessage(
            email_subject, email_body,
            settings.DEFAULT_FROM_EMAIL, [email, ],
        )

        email.send(fail_silently=False)
        
    return 'success'