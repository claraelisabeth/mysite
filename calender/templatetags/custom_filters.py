
from django import template 
from django.template.defaultfilters import stringfilter
  
register = template.Library() 
  
@register.filter
@stringfilter
def change_to_no(value): 
    value = "no"
    