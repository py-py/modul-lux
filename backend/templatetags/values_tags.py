from django import template


def has_values(value):
    if isinstance(value, dict):
        return any(value.values())
    return False

register = template.Library()
register.filter('has_values', has_values)

