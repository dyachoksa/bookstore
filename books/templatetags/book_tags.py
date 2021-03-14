from django import template

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
