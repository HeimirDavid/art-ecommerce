from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import NewsPost
# The code comes from a part of the Code institutes code along,
# The blog project, has been slightly modified for my needs

def get_newsposts(request):
    """
    return a list of Posts, sort them by date with the most recent being first,
    and render them to the newsposts.html template
    """

    posts = NewsPost.objects.filter(published_date__lte=timezone.now
        ()).order_by('-published_date')
    return render(request, 'newsposts.html', {'posts': posts})


def news_detail(request, pk):
    """
    return a single Post based in the post ID
    and render it to the 'articepost.html' template.
    or return a 404 error if the post is not found
    """
    post = get_object_or_404(NewsPost, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'articlepost.html', {'post': post})

