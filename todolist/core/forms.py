from django import forms
from django.core.exceptions import ValidationError

from todolist.core.models import ToDo


class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ['title', 'description']

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get("title"):
            raise ValidationError("The title is required.")

        return self.cleaned_data