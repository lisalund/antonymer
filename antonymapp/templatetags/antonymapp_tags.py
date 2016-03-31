from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.assignment_tag
def get_top_list():
	top_list = User.objects.order_by('-userprofile__score')[:10]
   	return top_list