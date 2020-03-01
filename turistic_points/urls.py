from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from attractions.api.viewsets import AttractionsViewSet
from core.api.viewsets import TuristicPointsViewSet
from comments.api.viewset import CommentsViewSet
from locations.api.viewsets import LocationsViewSet
from reviews.api.viewsets import ReviewsViewSet


# api entrypoints
router = routers.DefaultRouter()
router.register(r'attractions', AttractionsViewSet)
router.register(r'turistic', TuristicPointsViewSet, basename='TuristicPoints')
router.register(r'locations', LocationsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'reviews', ReviewsViewSet)


# urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
