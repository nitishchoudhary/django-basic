from django import template

register = template.Library()

@register.filter(name=cut)
def cut(value, arg):
    """
    This filter use to cut out of the arg value!
    """
    return value.replace(arg, '')

#register.filter('cuttext', cut)
