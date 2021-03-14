from django.forms import ModelForm, IntegerField

from .models import Review


class ReviewCreateForm(ModelForm):
    rating = IntegerField(max_value=10, min_value=0, initial=0)

    class Meta:
        model = Review
        fields = ["title", "rating", "content"]
