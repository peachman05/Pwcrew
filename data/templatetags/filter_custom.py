import datetime
from .. import viewHelper
from django import template

register = template.Library()

@register.filter
def ACtoBC(value):
    # import pdb; pdb.set_trace()
    if value != None:
        return viewHelper.AD_date_to_BD_str(value)
    else:
        return ""


# @register.filter
# def ACtoBC2(value):
#     # import pdb; pdb.set_trace()
#     return field.as_widget(attrs={"class":css}) viewHelper.AD_date_to_BD_str(value)