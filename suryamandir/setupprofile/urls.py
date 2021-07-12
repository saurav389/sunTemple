from django.urls import path
from django.conf.urls.static import static
from .views import (Personal_view,
					Qualification_view,
					Location_view,
					Profile_view,
					PerUpdate,
					QualUpdate,
					LocUpdate,
					ProfileView
					)


urlpatterns = [
    path('',Personal_view,name= 'personal'),
    path('qualification/',Qualification_view,name='qualification'),
    path('location/',Location_view,name='location'),
    path('setimage/',Profile_view,name='setimage'),
    path('profile/',ProfileView,name='profile'),
    path('perupdate',PerUpdate,name='perupdate'),
    path('qualupdate',QualUpdate,name='qualupdate'),
    path('locupdate',LocUpdate,name='locupdate')

]