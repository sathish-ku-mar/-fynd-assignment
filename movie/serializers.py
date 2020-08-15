from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'name', 'director', 'genre', 'popularity', 'imdb_score')
        read_only_fields = ('id',)