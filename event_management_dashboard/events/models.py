from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    attendees = models.ManyToManyField('Attendee', related_name='events', blank=False)

    def __str__(self):
        return self.name


class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_attendees')

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')
    assigned_attendee = models.ForeignKey(Attendee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
