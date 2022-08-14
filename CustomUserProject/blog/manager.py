from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
class CustomManager(BaseUserManager):
    '''
    Custom User Manager where email is unique identifiers rather than username
    '''
    def create_user(self,username,email,password,**extra_fields):
        if not username:
            raise ValueError('Username must be set')
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extrafields):
        extrafields.default.set('is_staff',True)
        extrafields.default.set('is_superuser',True)
        extrafields.default.set('is_active',True)
        extrafields.default.set('is_verified',True)
        if extrafields.get('is_staff')is not True:
            raise ValueError('SuperUser Must be is_staff')
        if extrafields.get('is_superuser')is not True:
            raise ValueError('SuperUser Must be is_superuser')
        return self.create_user(email,password,**extrafields)