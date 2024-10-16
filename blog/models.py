from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.



    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    Excerpt = models.CharField(max_length=200)
    Image_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
    


