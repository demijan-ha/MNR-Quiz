from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError(_('Please insert a valid email.'))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name= last_name, **extra_fields)
        user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if not email:
            raise ValueError(_('Please insert a valid email.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CategoryManager(models.Manager):
    def new_category(self, category):
        new_category = self.create(category=category).lower()

        new_category.save()
        return new_category


class ProgressManager(models.Manager):
    def new_progress(self, user):
        new_progress = self.create(user=user, score="")
        new_progress.save()
        return new_progress


class AnonProgressManager(models.Manager):
    def new_progress(self, anon_user):
        new_progress = self.create(anon_user=anon_user, score="")
        new_progress.save()
        return new_progress



