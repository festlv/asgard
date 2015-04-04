from django import forms
from asgard.forms import BootstrapForm

from access.forms import HexNumberInput

from access.models import Zone, Tool, Card
from django.contrib.auth.models import User


class CreateUserForm(forms.Form):
    first_name = forms.CharField(min_length=2)
    last_name = forms.CharField(min_length=2)
    email = forms.EmailField()
    phone_number = forms.CharField(min_length=7)

    card_serial_number = forms.CharField(widget=HexNumberInput())

    zone_access = forms.ModelMultipleChoiceField(
        Zone.objects.all(), required=False)
    tool_access = forms.ModelMultipleChoiceField(
        Tool.objects.all(), required=False)

    def clean_email(self):
        """
        Validates e-mail for uniqueness, since django.contrib.auth
        doesn't have unique constraint on e-mail.
        """
        v = self.cleaned_data['email'].strip()
        if len(User.objects.filter(email__iexact=v)) > 0:
            raise forms.ValidationError(
                "User with this e-mail address already exists")
        return v

    def clean_card_serial_number(self):
        """
        Validates card serial number for uniqueness.
        """
        v = self.cleaned_data['card_serial_number']

        if len(Card.objects.filter(serial_number=v)) > 0:
            raise forms.ValidationError(
                "Access card with this serial number already exists")
        return v


class LoginForm(BootstrapForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
