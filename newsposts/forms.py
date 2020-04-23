from django.forms import ModelForm
from .models import NewsPost


class NewsPostForm(ModelForm):
    """
    Same Forms design as 'Django Blog Miniproject' from Code Institutes Code Along
    """
    class Meta:
        model = NewsPost
        fields = ['title', 'content', 'image', 'tag', 'published_date']