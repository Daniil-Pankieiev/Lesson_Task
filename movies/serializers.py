from rest_framework import serializers

from movies.models import Movie, Director, Star, Genre, Certification


class MovieSerializer(serializers.ModelSerializer):

    genre_ids = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, required=False)
    director_ids = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all(), many=True, required=False)
    star_ids = serializers.PrimaryKeyRelatedField(queryset=Star.objects.all(), many=True, required=False)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'time', 'imdb', 'votes', 'meta_score', 'gross', 'certification',
                  'description', 'genre_ids', 'director_ids', 'star_ids')

    def create(self, validated_data):
        genre_ids = validated_data.pop('genre_ids', [])
        director_ids = validated_data.pop('director_ids', [])
        star_ids = validated_data.pop('star_ids', [])

        movie = Movie.objects.create(**validated_data)

        movie.genres.set(genre_ids)
        movie.directors.set(director_ids)
        movie.stars.set(star_ids)

        return movie
