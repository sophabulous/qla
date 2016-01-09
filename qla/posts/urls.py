from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>)contributors/$', views.AllContributorsView.as_view(), name='contributors'),
    url(r'^(?P<pk>[0-9]+)/bio/$', views.BioView.as_view(), name='bio'),
    url(r'^(?P<pk>[0-9]+)/qla/$', views.QLAView.as_view(), name='qla'),
    url(r'^(?P<pk>)all-qlas/$', views.AllQLAsView.as_view(), name='all-qlas'),
    url(r'^(?P<pk>)contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^(?P<pk>)about/$', views.AboutView.as_view(), name='about'),
    url(r'^(?P<pk>)weekly-vignette/$', views.WVView.as_view(), name='weeklyvignette'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<post_id>[0-9]+)/vote/$', views.vote, name='vote'),
]