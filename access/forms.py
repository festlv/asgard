from django import forms
from access.models import Card


class HexNumberInput(forms.widgets.TextInput):
    """Widget which allows user input in hex and converts it to
    decimal representation and vice versa"""

    def _format_value(self, value):
        """Takes number from model, formats it in hex, removes
        leading 0x"""
        return "%X" % value

    def value_from_datadict(self, data, files, name):
        v = super(HexNumberInput, self).value_from_datadict(data, files, name)
        try:
            v = int(v, 16)
        except ValueError:
            v = None

        return v


class CardForm(forms.ModelForm):

    class Meta:
        exclude = []
        model = Card
        widgets = {
            'serial_number': HexNumberInput(),
        }
