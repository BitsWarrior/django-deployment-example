from django import template

register = template.Library()

def cat(value,arg):
    return value.replace(arg,'***')

register.filter('cat',cat)
