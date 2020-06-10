from django import template
register = template.Library()

def first_eight_upper(value):
    """This is my own filter """
    result = value[:8].upper()
    return result

register.filter('f8uppper', first_eight_upper)