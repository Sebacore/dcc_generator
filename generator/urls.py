from django.conf.urls import url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'character', api.CharacterViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)), )

urlpatterns += (
    # urls for Character
    url(r'^generator/character/$',
        views.CharacterListView.as_view(),
        name='generator_character_list'),
    url(r'^generator/character/create/$',
        views.CharacterCreateView.as_view(),
        name='generator_character_create'),
    url(r'^generator/character/detail/(?P<slug>\S+)/$',
        views.CharacterDetailView.as_view(),
        name='generator_character_detail'),
    url(r'^generator/character/update/(?P<slug>\S+)/$',
        views.CharacterUpdateView.as_view(),
        name='generator_character_update'), )
