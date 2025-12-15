from django import template
from women import views

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
	return views.cats_db