from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import stripe
from django.http import JsonResponse
from django.utils import timezone
from .models import contactus, SearchQuery, notification
from .form import contactForm
from blog.models import BlogPost
import razorpay


client = razorpay.Client(auth=("rzp_test_qYYiCzlYVkVDVy", "1Dkk0dcZcaDs0AKWUSbawW71"))
# Create your views here.


msgcount = 0
noticount = 0
msg = contactus.objects.all()
noti = notification.objects.all()
for lookup in msg:
    if lookup.Status is False:
        msgcount = msgcount+1

for lookup in noti:
    if lookup.Status is False:
        noticount = noticount+1


stripe.api_key = "sk_test_YFmrMupANYmRGjc2ly9g99gm00rdFQBuwg"

def home_view(request):

    context = {"newMessage":msgcount,
                "newNotification":noticount,
              }

    return render(request,"base.html",context)

def notice_detail(request,pk):
    notice = notification.objects.get(id=pk)
    notice.Status=True
    notice.save(update_fields=['Status'])
    context = {"notice":notice,
                "newMessage":msgcount,
                "newNotification":noticount,}

    return render(request,"notice.html",context)
def notification_view(request):
    

    notiurl = "/notification"

    context = {"newMessage":msgcount,
                "newNotification":noticount,
                "notification":noti}

    return render(request,"notification.html",context)

def message_view(request):
    allMessage = contactus.objects.all()
    context = {"message":allMessage,
                "newMessage":msgcount,
                "newNotification":noticount,
                }
    return render(request,"home.html",context)

def message_detail(request, pk):
    message = contactus.objects.get(id=pk)
    message.Status=True
    # message.publish_date = timezone.now
    message.save(update_fields=['Status'])
    # message.save(update_fields=['publish_date'])
    # contactus.objects.filter(id=pk).update(Status=True)

    context ={"message":message,
              "newMessage":msgcount,
              "newNotification":noticount,}
    return render(request,"message.html",context)


def donation_view(request):
    #DATA should contain these keys:    
    #amount           : amount of order    
    #currency         : currency of order    
    #receipt          : receipt id of order    
    #payment_capture  : 1 if capture should be done automatically or else 0    
    #notes(optional)  : notes for order (optional)

    DATA={
        "amount":2000*100,
        "currency":'INR',
        "receipt":'order_receipt_0389',
        "payment_capture":0,
        "notes":{'Donation':'For Suryamandir'}
        }
    responce = client.order.create(data=DATA)
    #client.customer.create(data=DATA)
    order_id = responce['id']
    order_status = responce['status']
    product = "Donation"
    price = 2000
    name = "Anonymous"
    phone = 7979815545
    email = "anonymous@gmail.com"
    if order_status == 'created':
        context = {
                'product_id':product,
                'price':price,
                'name':name,
                'phone':phone,
                'email':email,
                'order_id':order_id
            }
        return render(request,"donation.html",context)
    else:
        return render(request,"donation.html",{})

def hindi_view(request):

    return render(request,"hindi.html",{})
def success_view(request):
    responce = request.POST
    print("payment id:",responce['razorpay_payment_id'],"order id:",responce['razorpay_order_id'],"signature:",responce['razorpay_signature'])
    params_dict = {
        'razorpay_payment_id':responce['razorpay_payment_id'],
        'razorpay_order_id':responce['razorpay_order_id'],
        'razorpay_signature':responce['razorpay_signature']
    }
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request,"donation.html",{"msg":"Payment Successfull !"})
    except:
        return render(request,"donation.html",{"msg":"Payment Failed"})

    return render(request,"success.html",{})
def team_view(request):

	return render(request, "team.html",{})


def contact_view(request):
    form = contactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            form.publish_date = timezone.now()
            form.save()
            form = contactForm

    context = {
        'form':form,
        "contact":"active"
    }
    return render(request,"contact.html",context)


def about_view(request):

    return render(request,"about.html",{})

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context =  {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request, 'search.html',context)


@login_required
def Post_view(request):
	qs = BlogPost.objects.filter(user= request.user)
	context = {"object_list":qs}
	return render(request,"post.html",context)
