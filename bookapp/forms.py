from django import forms
from bookapp.models import Book, Author


class AuthorForm(forms.ModelForm):
    class Meta:

        model = Author
        fields = ['name']

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Author'}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter the book title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the author name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book price'})
        }
