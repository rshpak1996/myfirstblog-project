from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_date = models.DateTimeField(auto_now=True)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/')