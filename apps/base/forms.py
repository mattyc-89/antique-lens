from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    name = forms.CharField(label='Your Name', max_length=150, required=True)
    email = forms.EmailField(label='Email Address', max_length=254, required=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
    
    base_input_classes = (
        "form-input mt-3 w-full py-2 px-3 h-10 "
        "bg-transparent dark:bg-slate-900 dark:text-slate-200 "
        "rounded outline-none border border-gray-200 "
        "focus:border-primary dark:border-gray-800 dark:focus:border-primary focus:ring-0"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for fname, field in self.fields.items():
            # set class
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing + " " + self.base_input_classes).strip()
            # placeholder
            field.widget.attrs.setdefault("placeholder", field.label)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email'].lower()  # Set username to email in lowercase
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'class': 'form-input mt-3 w-full py-2 px-3 h-10 bg-transparent dark:bg-slate-900 dark:text-slate-200 rounded outline-none border border-gray-200 focus:border-primary dark:border-gray-800 dark:focus:border-primary focus:ring-0', 'placeholder': 'name@example.com'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-input mt-3 w-full py-2 px-3 h-10 bg-transparent dark:bg-slate-900 dark:text-slate-200 rounded outline-none border border-gray-200 focus:border-primary dark:border-gray-800 dark:focus:border-primary focus:ring-0', 'placeholder': 'Password:'})
    )


