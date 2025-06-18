from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField

class Co_User(BaseUserManager):
    def create_user(self, email, password=None, role='passager', **extra_fields):
        if not email:
            raise ValueError("l'adresse email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(
        Group,
        related_name='user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    ROLE_CHOICES = (
         ('conducteur', 'Conducteur'),
         ('passager', 'Passager'),
    )
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = PhoneNumberField(blank=True, null=True, region='BJ')  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    objects = Co_User()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'role', 'username']
    
    def __str__(self):
        return self.email


