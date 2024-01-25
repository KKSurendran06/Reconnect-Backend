from django.db import models


class EventPage(models.Model):
    heading = models.CharField(max_length=20)
    description = models.CharField(max_length = 250)
    pass_out_year = models.DateField()
    event_date = models.DateField()


class RaiseHand(models.Model):
    raisehand = models.BooleanField()

class RequestInsitute(models.Model):
    requestInsituteName = models.CharField(max_length = 20)

class InstituteDetails(models.Model):
    department = models.CharField(max_length = 20)
    graduationyear = models.DateField()

class EditProfile(models.Model):
    imageurl = models.CharField(max_length = 20 )
    aboutus = models.CharField(max_length = 200)
    
    
