from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Checkout
import datetime

class CustomPaymentForm(forms.ModelForm):
    credit_card_number = forms.CharField(
        label='Credit Card Number',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234 5678 9012 3456'})
    )
    expiry_date = forms.DateField(
        label='Expiry Date (Month/Year)',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YYYY'}),
        input_formats=['%m/%Y', '%m/%y']  # Accepts MM/YYYY and MM/YY formats
    )
    security_code = forms.IntegerField(
        label='Security Code (CVV)',
        required=True,
        validators=[MinValueValidator(100), MaxValueValidator(999)],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVV'})
    )

    class Meta:
        model = Checkout
        fields = ['delivery_address', 'payment_option', 'credit_card_number', 'expiry_date', 'security_code']
        widgets = {
            'delivery_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Your Address'}),
            'payment_option': forms.Select(choices=[
                ('credit', 'Credit Card'),
                ('visa', 'Visa'),
                ('debit', 'Debit Card')
            ], attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomPaymentForm, self).__init__(*args, **kwargs)
        self.fields['delivery_address'].label = "Delivery Address"
        self.fields['credit_card_number'].widget.attrs.update({'autocomplete': 'off'})  # Disabling autocomplete for security
        self.fields['expiry_date'].validators.append(self.validate_expiry_date)

    def validate_expiry_date(self, value):
        if value < datetime.date.today():
            raise forms.ValidationError("The expiration date cannot be in the past.")

    def clean_credit_card_number(self):
        credit_card_number = self.cleaned_data['credit_card_number']
        # Validate the length of the credit card number
        if len(credit_card_number) < 16 or len(credit_card_number) > 16:
            raise forms.ValidationError("The credit card number must be 16 digits.")
        return credit_card_number
   