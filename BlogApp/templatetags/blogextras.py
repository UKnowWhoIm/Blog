from django import template
from BlogApp.models import User,Post

register = template.Library()

@register.filter
def get_status(post_id,email):
    if Post.objects.get(id=post_id).Votes.filter(Email=email):
        return "Liked"
    return "Like"
