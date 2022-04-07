from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    body=models.TextField()
    def __str__(self):
        return 'by'.join(self.title,self.writer)
        