from django.urls import path
from django.conf.urls.static import static
from .views import notification_view, notice_detail, home_view,message_view,Post_view,team_view,contact_view,donation_view,success_view, about_view,message_detail, hindi_view,search_view


urlpatterns = [
    path('',home_view,name='home'),
    path('notice/',notification_view,name= 'notice'),
    path('notice/<int:pk>',notice_detail,name='notice'),
    path('about/',about_view,name='about'),
    path('search/',search_view,name='search'),
    path('typing/',hindi_view,name='typing'),
    path('donation/',donation_view,name='donation'),
    path('payment_status/',success_view,name='payment_status'),
    path('post/',Post_view,name='post'),
    path('message/',message_view,name='message'),
    path('team/',team_view,name='team'),
    path('contact/',contact_view,name='contact'),
    path('message/<int:pk>',message_detail,name='message')

]