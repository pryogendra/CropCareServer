from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=255)
    mobile = models.CharField(max_length=18)
    pincode = models.CharField(max_length=15, null=True, blank=True)
    profile_image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(UserProfile, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    data_type=models.CharField(max_length=200, default='jpg')
    caption = models.CharField(max_length=9255)
    likes = models.IntegerField()
    comments = models.IntegerField()
    parent=models.CharField(max_length=5555,blank=True,null=True)
    posted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.user}: {self.caption[:30]}"

    @property
    def posted_ago(self):
        from datetime import timedelta
        now = timezone.now()
        diff = now - self.posted_at
        if diff < timedelta(minutes=1):
            return "Just now"
        elif diff < timedelta(hours=1):
            minutes = diff.seconds // 60
            return f"{minutes} minutes ago"
        elif diff < timedelta(days=1):
            hours = diff.seconds // 3600
            return f"{hours} hours ago"
        elif diff < timedelta(days=7):
            days = diff.days
            return f"{days} days ago"
        elif diff < timedelta(weeks=52):
            weeks = diff.days // 7
            return f"{weeks} week{'s' if weeks > 1 else ''} ago"
        elif diff < timedelta(days=365):
            months = diff.days // 30
            return f"{months} month{'s' if months > 1 else ''} ago"
        else:
            years = diff.days // 365
            return f"{years} year{'s' if years > 1 else ''} ago"


class Govt_Scheme(models.Model):
    title=models.CharField(max_length=5000, blank=True, null=True)
    discription=models.TextField()
    benefit=models.TextField()
    eligibility=models.TextField()
    document=models.TextField()
    apply_process=models.TextField()
    contact=models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.title

class Notification(models.Model):
    user=models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notification')
    message=models.CharField(max_length=700, blank=True, null=True)
