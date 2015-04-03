from django import forms
from access.forms import HexNumberInput

from access.models import Zone, Tool


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

from asgard.forms import BootstrapForm



class LoginForm(BootstrapForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
