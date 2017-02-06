from django.conf.urls import url

from . import views

app_name = 'generator'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<character_name>[a-zA-Z0-9_]+)/$', views.detail, name='details'),
]
