from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from movies.models import Movie


from rest_framework import viewsets

from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
#
# def movie_list_view(request: HttpRequest) -> HttpResponse:
#     movies = Movie.objects.all()[:5]
#     context = {
#         "movies": movies,
#     }
#     return render(request, "movies/movies_list.html", context=context)
#
#
# class MovieListView(ListView):
#     model = Movie
#     template_name = "movies/movies_list.html"
#     context_object_name = "movies"
#     paginate_by = 4
#
#     def get_queryset(self):
#         genre_filter = self.request.GET.get("genre")
#
#         queryset = super().get_queryset()
#
#         if genre_filter:
#             queryset = queryset.filter(movie_genres__genre__name=genre_filter)
#
#         return queryset
