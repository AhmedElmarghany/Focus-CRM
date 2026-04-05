from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

# Register form
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Jane'
            # 'class': 'add classes here if needed'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Doe'
        })
        self.fields['username'].widget.attrs.update({
            'placeholder': 'janeDoe123'
        })
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.fields['password1'].widget.attrs.update({
            'placeholder': '8+ characters',
            'autocomplete': 'new-password',
            'id': 'password',
            'oninput': 'updateStrength(this.value); checkMatch()'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Re-enter your password',
            'autocomplete': 'new-password',
            'id': 'confirm-password',
            'oninput': 'checkMatch()'
        })

        
        for field in self.fields.values():
            field.help_text = None


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password =forms.CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'janeDoe123'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': '••••••',
            'autocomplete': 'new-password',
            'id': 'password',
        })
        
        for field in self.fields.values():
            field.help_text = None


class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'category', 'phone', 'tall', 'weight', 'address']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Jane'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Doe'
        })
        self.fields['phone'].widget.attrs.update({
            'placeholder': '+201000000000',
        })
        self.fields['tall'].widget.attrs.update({
            'placeholder': '170',
        })
        self.fields['weight'].widget.attrs.update({
            'placeholder': '70.0',
        })
        self.fields['address'].widget.attrs.update({
            'placeholder': 'Street, City',
        })
