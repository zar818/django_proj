from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=50,null=False)
    image=models.FileField(upload_to='image/%Y/%m/%d/',null=True,verbose_name='')
    text=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering=['-time']
    # def __str__(self):
    #     return self.text
class ArtWork(models.Model):
    art=models.FileField(upload_to='image/%Y/%m/%d/',null=False,verbose_name='')
    date=models.DateTimeField(auto_now_add=True)
    art_desc=models.CharField(max_length=205,help_text='Description of Your Art with in 205',null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,db_constraint=True,auto_created=True)
    ordering=['-time']
    arts=models.Manager()
    # def __str__(self):
    #     return self.art
class Article(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,auto_created=True)
    article_title=models.CharField(max_length=58,null=False)
    main_article=models.TextField(null=False)
    def __str__(self):
        return 'by'.join(self.article_title,self.user)


