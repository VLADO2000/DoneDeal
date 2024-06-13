import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from datetime import date
from django.urls import reverse


BUSINESS_ROLES = (
    (0, 'individual'),
    (1, 'company'),
)

class AccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a new user account based on email and password
        """
        if not email:
            raise ValueError("User email ought to be provided")
        
        email = self.normalize_email(email)
        user = self.model(
            id = uuid.uuid4(), 
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user 
    
class Account(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    is_active = models.BooleanField(default=True)
    brand_name = models.CharField(max_length=255, unique=True, verbose_name='brand name', null=True)
    description = models.TextField(default='', null=True)
    date_joined = models.DateField(auto_now_add=True)
    role = models.IntegerField(choices=BUSINESS_ROLES, default=0)
    #Let's Add custom id field to reduce confusion
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    objects  = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['brand_name']

    def __str__(self):
        return f'{self.email}--{self.brand_name}'

    def __repr__(self):
        return f'{Account.__name__}-(label={self.brand_name})' 
    
    def get_role_display(self):
        return BUSINESS_ROLES[self.role][1].title()
    
    def get_absolute_url(self):
        return reverse('account_detail', kwargs={'pk': self.id})
    



