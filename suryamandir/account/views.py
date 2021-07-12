from django.shortcuts import render
from .models import SuryamandirExpenses
# Create your views here.
def ExpenseView(request):

	if request.method == "POST":
		partyname = request.POST.getlist('partyname')
		itemname = request.POST.getlist('itemname')
		quantity = request.POST.getlist('quantity')
		rate = request.POST.getlist('rate')
		amount = request.POST.getlist('amount')
		plen = len(partyname)
		
		for i in range(0,plen):
			SuryamandirExpenses.objects.create(PartyName=partyname[i],ItemName=itemname[i],Quantity=quantity[i],Rate=rate[i],Amount=amount[i])

	return render(request,"expenses.html",{})