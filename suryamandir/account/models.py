from django.db import models

# Create your models here.
class SuryamandirDonation(models.Model):
	Name = models.CharField(max_length=120)
	Email = models.EmailField(max_length=254)
	Number = models.IntegerField()
	Amount = models.IntegerField()
		
class SuryamandirExpenses(models.Model):
	"""docstring for SuryamandirExpenses"""
	PartyName = models.CharField(max_length=120)
	ItemName = models.CharField(max_length=120)
	Quantity = models.IntegerField()
	Rate = models.IntegerField()
	Amount = models.IntegerField()

		