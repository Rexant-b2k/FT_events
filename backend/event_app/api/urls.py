from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (EventViewSet, EventRegistrationViewSet,
                    SubeventViewSet, SpeakerViewSet, TagViewSet)

router = DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register(
    r'^events/(?P<event_id>\d+)/subevents',
    SubeventViewSet,
    basename='subevent'
)
router.register(r'^events/(?P<event_id>\d+)/registrations',
                EventRegistrationViewSet, basename='registration')
router.register('speakers', SpeakerViewSet, basename='speaker')
router.register('tags', TagViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]
