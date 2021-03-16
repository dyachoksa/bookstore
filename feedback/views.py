from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import ContactData


class ContactUsView(SuccessMessageMixin, CreateView):
    template_name = "feedback/contact-us.html"
    model = ContactData
    fields = ['name', 'email', 'subject', 'message']
    success_message = "Thank you, %(name)s! Your message was sent. We will respond as soon as possible."
    success_url = reverse_lazy('feedback:contact-us')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user

        response = super().form_valid(form)

        self.send_mail(form)

        return response

    def send_mail(self, form):
        context = {**form.cleaned_data}

        message_txt = render_to_string('feedback/email/contact-us.txt', context=context)
        message_html = render_to_string('feedback/email/contact-us.html', context=context)

        mail_managers(
            form.cleaned_data['subject'],
            message_txt,
            fail_silently=False,
            html_message=message_html
        )
