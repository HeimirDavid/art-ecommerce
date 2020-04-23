from django.shortcuts import render
from django.utils import timezone
from newsposts.models import NewsPost


# Create your views here.
def index(request):

    posts = NewsPost.objects.filter(published_date__lte=timezone.now
        ()).order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})
