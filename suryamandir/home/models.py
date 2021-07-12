from django.db import models
from django.conf import settings
# Create your models here.
class contactus(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField(max_length=254)
    Number = models.IntegerField()
    Query = models.TextField(max_length=500)
    Status = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']


    def __str__(self):
        return f"{self.Query}................................from:{self.Name}      Date:{self.updated}"

    def get_absolute_url(self):
        return f"message/{self.id}"

    def get_msg_url(self):
        return f"/message"

class notification(models.Model):
    notification = models.TextField(max_length=300)
    Status = models.BooleanField(default=False)  
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-updated']


    def get_notice_url(self):
        return f"/notice/{self.id}"  




class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)