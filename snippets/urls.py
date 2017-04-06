from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippets-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetails.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', views.UserList.as_view(), name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)