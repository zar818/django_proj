from yougo.models import Post, Research
from django.contrib import admin

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','date','user']
@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display=['id','title','date','research_by']    