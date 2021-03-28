from django.conf import settings


def show_toolbar(request):
    """
    Function to determine whether to show the toolbar on a given page.
    """
    return settings.DEBUG \
        and request.META.get("REMOTE_ADDR") in settings.INTERNAL_IPS \
        and not request.path.startswith("/summernote/")
