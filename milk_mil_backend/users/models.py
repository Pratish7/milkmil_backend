from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

from milk_mil_backend.users.managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for milk_mil_backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
    
class UserTypes(models.Model):

    user_types = (
        ('Data Entry', 'Data Entry'),
        ('QR Code Scan', 'QR Code Scan'),
        ('Photo Clicking', 'Photo Clicking'),
        ('Report Admin', 'Report Admin'),
        ('Material Inward', 'Material Inward'),
        ('Material Outward', 'Material Outward'),
        ('Report View', 'Report View'),
        ('Master Data Admin', 'Master Data Admin'),
        ('Transaction Admin', 'Transaction Admin'),
        ('Visitors Admin', 'Visitors Admin'),
        ('Vehicle Admin', 'Vehicle Admin'),
        ('Status View', 'Status View'),
    )

    id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=255, choices=user_types)
