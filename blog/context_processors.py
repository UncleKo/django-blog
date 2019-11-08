from .models import Category, Tag, Post
from django.db.models import Count

def global_val(request):
  archives = Post.objects.values('date_posted__year','date_posted__month').annotate(Count('id')).order_by()

  return {
    'latest_posts': Post.objects.all().order_by('-date_posted')[:5],
    'drafts': Post.objects.filter(draft=True).order_by('-date_posted')[:5],
    'categories': Category.objects.all(),
    'tags': Tag.objects.all(),
    'archives': archives
  }