import uuid
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rx import create
from .models import CustomUser, Profile
from .views import user_sign
uuid


# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_profile(instance,sender,created,**kwargs):
#     if not created and instance.is_active:
#         user_profile=Profile.objects.create(instance.id)
#         return user_profile
#     # user_obj=CustomUser.objects.filter(email=instance)
#     # auth_token=str(uuid.uuid4())
#     # user_oj=Profile.objects.create(instance.id,auth_token=auth_token)
#     # user_oj.save()
#     print('sender:',sender)
#     print('instance',instance)
#     print('create',created)