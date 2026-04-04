from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
