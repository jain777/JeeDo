from django import forms
from django.contrib.auth.models import User
from .models import Resume
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile, StudentProfile
from student.models import ProgramAndBranch
from .validators import check_file_size, regex_validators

class AspirantRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        strip = False,
        widget = forms.PasswordInput(attr={'class' :'form-control'}),
        help_text = password_validation.password_validators.help_text_html(),

    )
    password2 = forms.CharField(
        label = 'Password Confirmation',
        strip = False,
        widget = forms.PasswordInput(attrs={'class':'form-control'}),
        help_text='Enter the same password as before',

    )
    username = forms.CharField(max_length = 13,help_text='Username can only take aplphabets,numbers and special characters',
                label='Username',
                validators=[regex_validators],
                required =True)
    dob = forms.DateField(required =True,label='Date of Birth',widget= forms.SelectDateWidget(years=range(2015,2020))),
    phone_no = forms.CharField(max_length=12,required=True,label = 'Contact Number'),
    profile_image =forms.ImageField(required = False,label ='Upload your profile image',validators=[check_file_size, ])

    def clean_email(self):
        email = self.cleaned_data['email']
        if(email.endswith('@gmail.com') or email.endswith('ac.in')) iS False:
            raise forms.ValidationError('Enter a valid email address.')
        return email

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2','email']
        required=(
            'last_name',
            'email',
        )

class ExpertRegistraionForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Enter the same password as before.',
    )
    username = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'maxlength': '254'}),
        label="Username",,required=True)
    educ_qual = forms.TextField(max_length = 250,required = True
                label ='Educational Qualifications')
    presently_working = forms.TextField(max_length = 100,required =True,
                label =' Work at Present')
    dob =   forms.DateField(required=True,widgets=forms.SelectDateWidget(1990,2020) ) 
    phone_no = forms.CharField(label ='contact number',max_length=12)
    profile_image =forms.ImageField(required = False,label ='Upload your profile image',validators=[check_file_size, ])
    linkedin_profile = forms.CharField(required=False,label = 'LinkedIn Profile Link')

    def clean_email(self):
        email = self.cleaned_data['email']
        if(email.endswith('@gmail.com') or email.endswith('ac.in')) iS False:
            raise forms.ValidationError('Enter a valid email address.')
        return email

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = User
        fields=('username','password1','password2','first_name','last_name','email') 
        required=('email','last_name')           