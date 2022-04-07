from django.contrib.auth.base_user import BaseUserManager
class CustomManager(BaseUserManager):
    '''Create and Save user on the basis of given email and password '''
    def create_user(self,email,password,**extrafields):
        if email is None:
            raise ValueError('Email must be set.')
        email=self.normalize_email(email)
        user=self.model(email=email,**extrafields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('is_active',True)
        if extrafields.get('is_staff') is not True:
            raise ValueError('SuperUser Must be is_staff')
        if extrafields.get('is_superuser') is not True:
            raise ValueError('SuperUser Must be is_superuser')
        return self.create_user(email,password,**extrafields)
