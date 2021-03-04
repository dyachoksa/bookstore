from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from .forms import UserProfileForm
from .models import UserProfile


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['current_user'] = self.request.user

        user_profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        context['profile'] = user_profile

        context['favorite_books'] = user_profile.user.favorite_books\
            .order_by('book__title')\
            .select_related("book")\
            .all()

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile
