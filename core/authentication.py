from django.core.exceptions import ObjectDoesNotExist

from account.models import User


def is_authenticate(username, password):
    """
    Authenticate the user
    1. on the basis of email + password
    :param username: required(email/username)
    :param password: required
    :return: if success user object, otherwise pass
    """
    try:
        user = User.objects.get(email__iexact=username, is_active=True)
        if user.check_password(password):
            return user
    except ObjectDoesNotExist:
        pass