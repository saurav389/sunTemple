from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PersonalDetails, QualificationDetails, LocationDetails, ProfileDetails
class DateInput(forms.DateInput):
    input_type = 'date'


class UserUpdationForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = '__all__'


class PersonalSetupForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ['FirstName','LastName','Father','Gender','Dob']
        widgets = {
        	'Dob':DateInput()
        	}

class QualificationSetupForm(forms.ModelForm):
    class Meta:
        model = QualificationDetails
        fields = ['Matric','Inter','Gradute','Other','College']
        labels = {
                  "Matric":"Matric School Name",
                  "Inter":"Inter School/College Name",
                  "Gradute":"Graduation College Name",
                  "Other":"Other Specialization",
                  "College":"Specialization Done From"
        }

class LocationSetupForm(forms.ModelForm):
    class Meta:
        model = LocationDetails
        fields = ['State','City','District','Village']

class ProfileSetupForm(forms.ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ['image','MobileNo']