from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from feedback.tasks import send_contact_us_email

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
        send_contact_us_email.delay(form.cleaned_data)
