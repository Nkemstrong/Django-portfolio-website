from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(upload_to="projects/")

    github = models.URLField(blank=True)

    technologies = models.CharField(max_length=200)

    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.name
    
class Profile(models.Model):

    name = models.CharField(max_length=100)

    title = models.CharField(max_length=200)

    hero_description = models.TextField()

    about = models.TextField()

    email = models.EmailField()

    github = models.URLField()

    linkedin = models.URLField()

    whatsapp = models.URLField()

    profile_image = models.ImageField(upload_to="profile/")

    def __str__(self):
        return self.name
    
class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"