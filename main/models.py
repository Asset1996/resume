from django.db import models
from django.contrib.auth.models import User

class WorkExperience(models.Model):
    """Model that describes work experience of the user"""
    class Meta():
        ordering = ['end_date']
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Name of the user")
    company_name = models.CharField(max_length=50, verbose_name="Name of the company")
    position = models.CharField(max_length=50, verbose_name="Position of the user")
    start_date = models.DateField(verbose_name="The date when the user started working")
    end_date = models.DateField(default=None, blank=True, null=True, verbose_name="The date when the user ended working")
    work_description = models.CharField(default=None, blank=True, null=True, max_length=250, verbose_name="Brief work description")

    def __str__(self) -> str:
        return self.position

