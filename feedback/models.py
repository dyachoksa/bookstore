from django.contrib.auth.models import User
from django.db import models


class ContactDataStatus(models.TextChoices):
    NEW = 'new', 'New message'
    IN_PROCESS = 'in_process', 'In process'
    DONE = 'done', 'Done'


class ContactData(models.Model):
    status = models.CharField(
        max_length=15, choices=ContactDataStatus.choices, default=ContactDataStatus.NEW, db_index=True
    )
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'contact form data'
        verbose_name_plural = 'contact forms data'

    def __str__(self):
        return self.subject

    def __repr__(self):
        return f"<ContactData id={self.pk} name={self.name} email={self.email}>"
