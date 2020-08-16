from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http.request import QueryDict
from core.api_permission import IsAdminUser
import pandas as pd


class MovieViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for the movies.
    """
    model = Movie
    serializer_class = MovieSerializer
    queryset = model.get_movies_all()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self, request):
        """
            To list the movies
            URL Structure: /movie/
            Required Fields: None
        """

        queryset = self.model.get_movies_all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
            To create the movies
            URL Structure: /movie/
            Required Fields: 'name', 'director', 'genre', 'popularity','imdb_score'
        """
        # To create movies bulky using file by pandas
        if 'upload_file' in request.data:
            df = pd.read_json(request.FILES['upload_file'])
            df.rename(columns={"99popularity": "popularity"}, inplace=True)

            objs = [
                Movie(
                    name=e.name,
                    director=e.director,
                    genre=','.join(e.genre),
                    popularity=e.popularity,
                    imdb_score=e.imdb_score
                )
                for e in df.itertuples()
            ]
            self.model.objects.bulk_create(objs)
            return Response({'msg':'Success'}, status=200)

        # For create movie
        data = QueryDict.dict(request.data)
        genre = data.get('genre', '')

        data['genre'] = ','.join(genre) if genre and isinstance(genre, list) else genre
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """
            To update the particular movie
            URL Structure: /movie/1/
            Required Fields: 'id', 'name', 'director', 'genre', 'popularity','imdb_score'
        """
        queryset = get_object_or_404(self.model, id=pk)

        data = QueryDict.dict(request.data)
        genre = data.get('genre', '')

        data['genre'] = ','.join(genre) if genre and isinstance(genre, list) else genre
        serializer = self.serializer_class(queryset, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
            To delete the particular movie
            URL Structure: /movie/1/
            Required Fields: id
        """
        queryset = get_object_or_404(self.model, id=pk)
        queryset.set_is_not_active()

        return Response({'message': 'Deleted'}, status=200)

    def search(self, request):
        """
            To search the movies
            URL Structure: /movie/search/
            Required Fields: name
        """
        query_string = request.data.get('name', '')
        if query_string:
            queryset = self.model.search_movies(query_string)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        return Response({'message': 'Movie name required'}, status=400)