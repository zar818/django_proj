from django.contrib import admin
from .models import Post, ArtWork
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','user','user_id','text','time']
@admin.register(ArtWork)
class ArtWorkAdmin(admin.ModelAdmin):
    list_display=['id','art','user','user_id','date']