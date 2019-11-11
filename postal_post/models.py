from django.db import models

# Create your models here.
DropOffto = (
    ("neighbour", "neighbour"),
    ("Security Guard", "Security Guard"),
    ("mailbox", "mailbox"),
    ("Any of the above", "Any of the above")
)


weightrate = (
    ("10", "10"),
    ("20", "20"),
    
)

Postal_rate = (
    ("10", "10"),
    ("20", "20"),
    
)

typeofdel = (
    ("paper", "paper"),
    ("parcel", "parcel"),
)
class Postal(models.Model):
    From = models.CharField(max_length=255)
    To = models.CharField(max_length=255)
    typeofdel = models.CharField(max_length=255, choices=typeofdel)

    Postal_rate = models.CharField(max_length=255, choices=Postal_rate)
    weightrate = models.CharField(max_length=255, choices=weightrate)
    del_pin_no = models.IntegerField(max_length=255)
    Describe_del = models.CharField(max_length=255)
    Full_area_address = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)    

    def __unicode__(self):
        return self.typeofdel

