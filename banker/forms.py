from django import forms
from banker.models import Transaction

class TransferForm(forms.ModelForm):
    class Meta:
        fields = ("account",)
        model = Transaction
