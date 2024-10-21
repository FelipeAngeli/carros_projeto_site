from django import forms 
from cars.models import Car



class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__' 
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor do carro deve ser maior que 20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1960:
            self.add_error('factory_year', 'O ano de fabricação do carro deve ser maior que 1960')
        return factory_year
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            self.add_error('photo', 'O carro deve ter uma foto')
        return photo