from django import forms
# from django.contrib import auth
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Account


##this is a form for creating new user
class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = Account
        fields = ('name', 'phone','email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['name'], self.fields['phone'], self.fields['email'], self.fields['password1'], self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control' })


#this class is for login user
class LoginForm(forms.ModelForm):
    password = forms.CharField(label= 'Password', widget=forms.PasswordInput)


    class Meta:
        model = Account
        fields = ('phone', 'password')
        widgets = {
                  'phone':forms.TextInput(attrs={'class':'form-control'}),
                  'password':forms.TextInput(attrs={'class':'form-control'}),
                  
        }

    def __init__(self, *args, **kwargs):
        
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in (self.fields['phone'], self.fields['password']):
            field.widget.attrs.update({'class':'form-control'})

    def clean(self):
        if self.is_valid():

            phone = self.cleaned_data.get('phone')
            password = self.cleaned_data.get('password')
            if not authenticate(phone=phone, password=password):
                raise forms.ValidationError('Invalid Login')

# #this is for upadating the user Info
# class AccountUpdateform(forms.ModelForm):

#     class Meta:
#         model = Account
#         fields = ('email', 'username')
#         widgets = {
#                   'email':forms.TextInput(attrs={'class':'form-control'}),
#                   'password':forms.TextInput(attrs={'class':'form-control'}),

#         }

#     def __init__(self, *args, **kwargs):
#         super(AccountUpdateform, self).__init__(*args,**kwargs)
#         for field in (self.fields['email'], self.fields['username']):
#             field.widgets.attrs.update({'class':'form-control'})

#     def clean_email(self):
#         if self.is_valid():
#             email = self.cleaned_data['email']
#             try:
#                 account = Account.objects.exclude(pk= self.instance.pk).get(email=email)
#             except Account.DoesNotExist:
#                 return email
#             raise forms.ValidationError("Email '%s' already in use." %email)

#     def clean_username(self):
#         if self.is_valid():
#             username = self.cleaned_data['username']
#             try:
#                 username = self.cleaned_data['username']
#             except Account.DoesNotExist:
#                 return username 
#             raise forms.ValidationError("Username '%s' already in use." %username)








