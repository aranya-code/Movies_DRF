from rest_framework import serializers
from movies.models import Movies, Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rating
        fields= '__all__'

    def validate(self, data):
        if Rating.objects.filter(
            reviewer=data['reviewer'],
            movie=data['movie']
        ).exists():
            raise serializers.ValidationError(
                "You have already posted a review on this movie."
            )
        return data


class MovieSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()
    class Meta:
        model= Movies
        fields= '__all__'

    def validate_movie_name(self, value):
        if Movies.objects.filter(movie_name = value).exists():
            raise serializers.ValidationError(detail='Movie name already exists.')
        return value


    def get_ratings(self, obj):
        ratings = obj.ratings.all().order_by('rating')
        return RatingSerializer(ratings, many=True).data
    