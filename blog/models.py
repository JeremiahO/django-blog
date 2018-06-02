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

# This allows our blog objects to have their name represented by their title
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:255] + '....'

    def pub_preety(self):
        return self.pub_date.strftime('%e %b %Y')
#Add the Blog app to the settings

# create a migration

# Migrate

# Add to admin
