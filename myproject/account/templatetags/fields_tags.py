from django import template
from jalali_date import datetime2jalali
register = template.Library()


@register.simple_tag
def verbose_name(modelinstance,fieldname):
    return modelinstance.first()._meta.get_field(fieldname).verbose_name.title()

