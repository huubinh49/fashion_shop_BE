from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt
from django.conf import settings
from datetime import datetime, timedelta,  time
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length = 100, unique = True)
    password = models.CharField(max_length = 100)
    
    username = models.CharField(max_length = 100, default = "guestNULL")
    is_staff = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token(self)

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        deltaTime = datetime.now() + timedelta(days = 30)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(deltaTime.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')
