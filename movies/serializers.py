from rest_framework import serializers

from movies.models import Movie, Director, Star, Genre, Certification


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    year = serializers.IntegerField()
    time = serializers.IntegerField()
    imdb = serializers.FloatField()
    votes = serializers.IntegerField()
    meta_score = serializers.FloatField(allow_null=True)
    gross = serializers.FloatField(allow_null=True)
    certification = serializers.PrimaryKeyRelatedField(queryset=Certification.objects.all())
    description = serializers.CharField()
    genre_ids = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True, required=False)
    director_ids = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all(), many=True, required=False)
    star_ids = serializers.PrimaryKeyRelatedField(queryset=Star.objects.all(), many=True, required=False)

    def create(self, validated_data):
        genre_ids = validated_data.pop('genre_ids', [])
        director_ids = validated_data.pop('director_ids', [])
        star_ids = validated_data.pop('star_ids', [])

        movie = Movie.objects.create(**validated_data)

        movie.genres.set(genre_ids)
        movie.directors.set(director_ids)
        movie.stars.set(star_ids)

        return movie
