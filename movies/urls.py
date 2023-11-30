from django.urls import path

from movies.views import  MovieViewSet

from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    # path('', movie_list_view, name="movie_list"),
    # path('', MovieListView.as_view(), name='movie_list')
    path("", include(router.urls))
]

app_name = "movies"
