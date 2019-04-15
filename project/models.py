from django.db import models
from django.contrib.auth.models import User

# For user-profile consistancy
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Tag(models.Model):
    # ...
    def __str__(self):
        return self.tag_title

    TAG_TYPE_CHOICES = (
        (0, 'Topic'),
        (1, 'Tech'),
        (2, 'Event'),
    )

    tag_title = models.CharField(max_length=200)
    tag_type = models.IntegerField(choices=TAG_TYPE_CHOICES, default=0)

class Profile(models.Model):
    # ...
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, null=True, blank=True)

class Project(models.Model):
    # ...
    def __str__(self):
        return self.project_title

    PROJECT_STAGE_CHOICES = (
        (0, 'Commenting'),
        (1, 'Bootstrapping'),
        (2, 'Prototyping'),
        (3, 'Testing'),
        (4, 'Maintaining'),
        (5, 'Drifting'),
        (6, 'Hibernating'),
    )

    project_title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True)
    stage = models.IntegerField(choices=PROJECT_STAGE_CHOICES, default=0)
    homepage_link = models.CharField(max_length=200, null=True, blank=True)
    developer_link = models.CharField(max_length=200, null=True, blank=True)
    community_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    members = models.ManyToManyField(Profile, blank=True)

class Update(models.Model):
    # ...
    def __str__(self):
        return self.update_title

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    update_title = models.CharField(max_length=200)
    update_content = models.TextField(max_length=1000, null=True, blank=True)

class Role(models.Model):
    # ...
    def __str__(self):
        return self.role_title
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role_title = models.CharField(max_length=200)
    filled_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()