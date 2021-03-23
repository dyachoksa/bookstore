from django import template

from ..models import Author


register = template.Library()


@register.filter()
def rating_class(rating):
    if rating >= 7:
        return "text-success"
    elif rating >= 4:
        return "text-warning"
    elif rating == 0:
        return "text-secondary"

    return "text-danger"


@register.simple_tag()
def get_authors():
    return Author.objects.all().order_by('name')


@register.inclusion_tag("books/_sidebar.html")
def render_sidebar():
    return {
        "authors": get_authors()
    }
