from rest_framework import serializers
from movies.models import Movies, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movies
        fields= '__all__'

    def movie_validator(self, name):
        if Movies.objects.filter(movie_name = name).exists():
            raise serializers.ValidationError(detail='Movie name already exists.')
        return name

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rating
        fields= '__all__'