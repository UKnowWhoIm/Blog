from django import template
from BlogApp.models import User,Post
from django.utils import timezone

register = template.Library()

@register.filter
def get_status(post_id,email):
    print(email)
    if Post.objects.get(id=post_id).Votes.filter(Email=email):
        return "Liked"
    return "Like"

@register.filter
def gettime(time):
    # TO DO
    # Converts the time passed to readable format
    return time
    time_past = timezone.now()-time
    
