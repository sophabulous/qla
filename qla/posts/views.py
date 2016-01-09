from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Post, Contributor, SocialMediaIcon, QLA, WeeklyVignette


class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

    
class AllContributorsView(generic.ListView):
    context_object_name = 'all_contributors'
    template_name = 'posts/all-contributors.html'

    def get_context_data(self, **kwargs):
        context = super(AllContributorsView, self).get_context_data(**kwargs)
        context['all_icons'] = SocialMediaIcon.objects.all()
        return context

    
    def get_queryset(self):
        """Return the last five published questions."""
        return Contributor.objects.order_by('-contributor_name')

  
class BioView(generic.DetailView):
    model = Contributor
    template_name = 'posts/bio.html'
    
    def get_context_data(self, **kwargs):
        context = super(BioView, self).get_context_data(**kwargs)
        context['latest_post_list'] = Post.objects.order_by('-pub_date')[:5]
        context['all_icons'] = SocialMediaIcon.objects.all()
        return context

class QLAView(generic.DetailView):
    model = QLA
    template_name = 'posts/single-qla.html'
    
    def get_context_data(self, **kwargs):
        context = super(QLAView, self).get_context_data(**kwargs)
        context['all_icons'] = SocialMediaIcon.objects.all()
        return context

class AllQLAsView(generic.ListView):
    context_object_name = 'all_qlas'
    template_name = 'posts/all-qlas.html'
    
    def get_queryset(self):
        """Return the 10 most popular QLAs."""
        return QLA.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(AllQLAsView, self).get_context_data(**kwargs)
        context['date'] = timezone.now()
        context['all_icons'] = SocialMediaIcon.objects.all()
        return context


class ContactView(generic.ListView):
    context_object_name = 'all_icons'
    template_name = 'posts/contact.html'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return SocialMediaIcon.objects.all()

class AboutView(generic.ListView):
    context_object_name = 'all_icons'
    template_name = 'posts/about.html'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return SocialMediaIcon.objects.all()

class WVView(generic.ListView):
    template_name = 'posts/weekly-vignette.html'
    context_object_name = 'weeklyvignette'

    def get_queryset(self):
        """Return the last five published questions."""
        return WeeklyVignette.objects.all()[:1]  
    
    def get_context_data(self, **kwargs):
        context = super(WVView, self).get_context_data(**kwargs)
        context['popular_posts'] = Post.objects.order_by('-pub_date')[:5]
        context['all_icons'] = SocialMediaIcon.objects.all()
        return context

