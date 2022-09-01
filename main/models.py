"""
Models page for main app.
"""
from django.utils.translation import ugettext as _
from django.db.models import JSONField
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """
    Manager for users.
    Need to customize to override the create_user and
    create_superuser by email field (not username).
    """
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a superuser with the given email and password."""
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model."""
    degrees = (
        ('ms', 'Masters'),
        ('bc', 'Bachelors'),
        ('hs', 'High school'),
        ('nd', 'No degree'),
    )
    experience = (
        ('no', 'No experience'),
        ('1', 'Less than 1 year'),
        ('12', 'From 1 to 2 years'),
        ('23', 'From 1 to 3 years'),
        ('3', 'More than 3 years'),
    )

    email = models.EmailField(_("Email address"), max_length=255, unique=True)
    name_en = models.CharField(
        _("Users name EN"), default=None, blank=True, null=True,
        max_length=50
    )
    name_ru = models.CharField(
        _("Users name RU"), default=None, blank=True, null=True,
        max_length=50
    )
    surname_en = models.CharField(
        _("Users surname EN"), default=None, blank=True, null=True,
        max_length=50
    )
    surname_ru = models.CharField(
        _("Users surname RU"), default=None, blank=True, null=True,
        max_length=50
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    skills = JSONField(_("Users skills"), default=dict, blank=True, null=True)
    birthday = models.DateField(
        _("Date of birth"), default=None, blank=True, null=True
    )
    phone = models.CharField(
        _("Phone number"), default=None, blank=True, null=True, max_length=20
    )
    instagram = models.CharField(
        _("Instagram"), default=None, blank=True, null=True,
        max_length=255
    )
    linkedin = models.CharField(
        _("LinkedIn"), default=None, blank=True, null=True, max_length=255
    )
    github = models.CharField(
        _("Github"), default=None, blank=True, null=True, max_length=255
    )
    experience = models.CharField(
        _("Experience"), max_length=50, choices=experience
    )
    degree = models.CharField(
        _("Users degree"), max_length=50, choices=degrees
    )

    address_en = models.CharField(
        _("Address EN"), default=None, blank=True, null=True, max_length=50
    )
    address_ru = models.CharField(
        _("Address RU"), default=None, blank=True, null=True, max_length=50
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'


class WorkExperience(models.Model):
    """Model that describes work experience of the user"""
    class Meta():
        ordering = ['end_date']

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("User name")
    )
    company_name_en = models.CharField(_("Company name EN"), max_length=50)
    company_name_ru = models.CharField(_("Company name RU"), max_length=50)
    position_en = models.CharField(_("Position of the user EN"), max_length=50)
    position_ru = models.CharField(_("Position of the user RU"), max_length=50)
    start_date = models.DateField(_("The date when the user started working"))
    end_date = models.DateField(
        _("The date when the user ended working"), default=None, blank=True,
        null=True
    )
    work_description_en = models.CharField(
        _("Brief work description EN"), default=None, blank=True, null=True,
        max_length=250
    )
    work_description_ru = models.CharField(
        _("Brief work description RU"), default=None, blank=True, null=True,
        max_length=250
    )

    def __str__(self) -> str:
        return self.position_en


class Education(models.Model):
    """Model that describes the education of the user"""

    types = (
        ('un', 'University'),
        ('cl', 'College'),
        ('cr', 'Certification'),
    )
    degrees = (
        ('ms', 'Masters'),
        ('bc', 'Bachelors'),
        ('hs', 'High school'),
        ('nd', 'No degree'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("User name")
    )
    institution_name_en = models.CharField(
        _("Institution name EN"), max_length=50
    )
    institution_name_ru = models.CharField(
        _("Institution name RU"), max_length=50
    )
    speciality_en = models.CharField(_("Specialty EN"), max_length=50)
    speciality_ru = models.CharField(_("Specialty RU"), max_length=50)
    type = models.CharField(
        _("Type of education"), max_length=50, choices=types
    )
    degree = models.CharField(
        _("Students degree"), max_length=50, choices=degrees
    )
    start_date = models.DateField(_("The date when the user started"))
    end_date = models.DateField(
        _("The date when the user graduated"), default=None, blank=True,
        null=True
    )
    course_description_en = models.CharField(
        _("Brief course description EN"), default=None, blank=True,
        null=True, max_length=250
    )
    course_description_ru = models.CharField(
        _("Brief course description RU"), default=None, blank=True,
        null=True, max_length=250
    )

    class Meta():
        ordering = ['end_date']

    def __str__(self) -> str:
        return self.degree
