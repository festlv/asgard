from django.conf import settings


def format_currency(value):
    try:
        return settings.CURRENCY_FORMAT % value
    except TypeError:
        return "(none)"
