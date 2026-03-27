import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Post(models.Model):
    publisher = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None, null=True)  # Added default value to avoid issues with blank titles
    locationTown = models.CharField(max_length=30)
    locationNeighborhood = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField(default=datetime.time.min)
    end_time = models.TimeField(default=datetime.time.min)
    volunteer = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='posts_volunteered')

    def clean(self):
        errors = {}
        today = timezone.localtime(timezone.now()).date()
        now_time = timezone.localtime(timezone.now()).time()

        if self.date and self.date < today:
            errors['date'] = 'The date cannot be in the past.'

        if self.date and self.date == today and self.start_time and self.start_time < now_time:
            errors['start_time'] = 'Start time cannot be in the past for today\'s date.'

        if self.start_time and self.end_time and self.end_time < self.start_time:
            errors['end_time'] = 'End time cannot be before start time.'

        if errors:
            raise ValidationError(errors)