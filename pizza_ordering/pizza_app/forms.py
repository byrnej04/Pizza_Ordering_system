from django import forms
from .models import Pizza, Order

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
        widgets = {'toppings': forms.CheckboxSelectMultiple()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].queryset = self.fields['size'].queryset.all()
        self.fields['size'].label_from_instance = lambda obj: f"{obj.name} (€{obj.price})"
        self.fields['crust'].queryset = self.fields['crust'].queryset.all()
        self.fields['crust'].label_from_instance = lambda obj: f"{obj.name} (€{obj.price})"
        self.fields['sauce'].queryset = self.fields['sauce'].queryset.all()
        self.fields['sauce'].label_from_instance = lambda obj: f"{obj.name} (€{obj.price})"
        self.fields['cheese'].queryset = self.fields['cheese'].queryset.all()
        self.fields['cheese'].label_from_instance = lambda obj: f"{obj.name} (€{obj.price})"
        self.fields['toppings'].queryset = self.fields['toppings'].queryset.all()
        self.fields['toppings'].label_from_instance = lambda obj: f"{obj.name} (€{obj.price})"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'address', 'card_number', 'card_expiry_month', 'card_expiry_year', 'card_cvv']
    def clean_card_number(self):
        cn = self.cleaned_data.get('card_number', '').strip()
        if len(cn) != 16 or not cn.isdigit():
            raise forms.ValidationError("Card number must be 16 digits.")
        return cn
    def clean_card_expiry_month(self):
        m = self.cleaned_data.get('card_expiry_month', '').strip()
        try:
            m_int = int(m)
        except:
            raise forms.ValidationError("Expiry month must be a number between 1 and 12.")
        if m_int < 1 or m_int > 12:
            raise forms.ValidationError("Expiry month must be between 1 and 12.")
        return m_int
    def clean_card_expiry_year(self):
        y = self.cleaned_data.get('card_expiry_year', '').strip()
        try:
            y_int = int(y)
        except:
            raise forms.ValidationError("Expiry year must be a number between 2025 and 9999.")
        if y_int < 2025 or y_int > 9999:
            raise forms.ValidationError("Expiry year must be between 2025 and 9999.")
        return y_int
    def clean_card_cvv(self):
        cvv = self.cleaned_data.get('card_cvv', '').strip()
        if len(cvv) != 3 or not cvv.isdigit():
            raise forms.ValidationError("CVV must be 3 digits.")
        return cvv
