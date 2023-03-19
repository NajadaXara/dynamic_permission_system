from django.db import models
from django.contrib.auth.models import User, Group, Permission


Permission.add_to_class('degree', models.IntegerField(
    null=True,
    help_text='Assign a value to be available to the user.'
))
