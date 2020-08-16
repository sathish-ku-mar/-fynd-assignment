from django.db import models
from django.db.models import Q
from django_mysql.models import ListTextField
from account.models import CommonModel
# Create your models here.


class Movie(CommonModel):
    """
    This model is used to store the movie details.
    """
    name = models.CharField(max_length=200, help_text='The name of the move')
    director = models.CharField(max_length=200, help_text='A person name who controls the making of a movie')
    genre = ListTextField(base_field=models.CharField(max_length=100), size=100, help_text='The category of the movie')
    popularity = models.FloatField(help_text='How much people liked the movie')
    imdb_score = models.FloatField(help_text="Users to rate films on a scale of one to ten")

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Movies'
        db_table = 'movie'
        get_latest_by = "-created_at"
        verbose_name = "Movie"

    def __str__(self):
        return self.name

    @classmethod
    def get_movies_all(cls):
        """
        Get all the movies
        :param: None
        :return: Movie object
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(is_active=True)

    def set_is_not_active(self):
        """
        Set active as false to remove the movie
        """
        self.is_active = False
        self.save(update_fields=['is_active'])

    @classmethod
    def search_movies(cls, query_string):
        """
        search all the movies by query_string
        :param query_string: search string
        :return: Movie objects
        :rtype: django.db.models.query.QuerySet
        """
        return cls.objects.filter(name__icontains=query_string, is_active=True)