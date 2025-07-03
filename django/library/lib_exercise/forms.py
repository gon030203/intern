from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import BookLoan

class UserRegistrationForm(forms.ModelForm):
    password         = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cd = super().clean()
        pw = cd.get("password")
        pc = cd.get("password_confirm")
        if pw and pc and pw != pc:
            raise forms.ValidationError("Passwords do not match.")
        return cd

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class BookLoanForm(forms.ModelForm):
    class Meta:
        model  = BookLoan
        fields = ['book', 'loan_date', 'return_date']

    def clean(self):
        cd    = super().clean()
        start = cd.get('loan_date')
        end   = cd.get('return_date')
        if start and end and end <= start:
            raise forms.ValidationError("Return date must be after loan date.")
        return cd
