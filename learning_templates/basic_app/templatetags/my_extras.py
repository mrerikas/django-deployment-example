from django import template

register = template.Library()


@register.filter(name='cut')  # using decorator instead of register.filter('cut', cut)
def cut(value, arg):
    """
    This cuts all values of "arg" from the string!
    """
    return value.replace(arg, "")


# register.filter('cut', cut)
