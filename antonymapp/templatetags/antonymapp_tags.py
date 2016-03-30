from django import template

register = template.Library()

@register.assignment_tag
def get_top_list():
    top_list = User.objects.filter().order_by('-score')[:10] 
    return top_list