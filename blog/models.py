from django.db import models

# Create your models here.
# Title
# PUB_Date
# body
# image
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')


    def summary(self):
        return self.body[:255] + '....'
#Add the Blog app to the settings

# create a migration

# Migrate

# Add to admin
