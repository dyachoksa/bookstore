from celery import shared_task
from django.core.mail import mail_managers
from django.template.loader import render_to_string


@shared_task
def send_contact_us_email(data):
    context = {**data}

    message_txt = render_to_string('feedback/email/contact-us.txt', context=context)
    message_html = render_to_string('feedback/email/contact-us.html', context=context)

    mail_managers(
        data['subject'],
        message_txt,
        fail_silently=False,
        html_message=message_html
    )

    return True
