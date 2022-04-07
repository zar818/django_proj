from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    media=models.FileField(upload_to='Postfile')
    body=models.TextField()
    def __str__(self):
        return self.title
class Research(models.Model):
    researcher=models.ManyToManyField(User)
    title=models.CharField(max_length=25)
    abstract=models.CharField(max_length=150)
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    def __str__(self):
        return self.title
    def research_by(self):
        return ','.join([str(x) for x in self.researcher.all()])    
class Page(models.Model):
    page_admin=models.OneToOneField(User,on_delete=models.CASCADE)    
    page_name=models.CharField(max_length=70)  
    date=models.DateField(auto_now_add=True)
    page_purpose=models.CharField(max_length=101)
    def __str__(self):
        return self.page_name
