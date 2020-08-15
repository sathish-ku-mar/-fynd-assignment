from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from core.common import (mobile_regex)


class CommonModel(models.Model):
    """
    Abstract common model class to be used in all the models
    """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(CommonModel):
    """
    This model is used to store the user details.
    """
    name = models.CharField(max_length=200, help_text='The name of the user')
    email = models.EmailField(unique=True, help_text='A unique email id of the user')
    phone = models.CharField(max_length=15, validators=[mobile_regex], help_text='The phone number of the user')
    password = models.TextField(help_text='The hashed password of the user')
    last_login = models.DateTimeField(blank=True, null=True, help_text='The last login of the user')
    is_admin = models.BooleanField(default=False, help_text='Boolean flag to check user is admin or not')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def __str__(self):
        return self.name