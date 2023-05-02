from typing import Any, Dict
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
                'author': forms.HiddenInput(attrs={'readonly':'readonly'}),
                'date_created':forms.DateInput(attrs={'type': 'date'})            
                }
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('A'):
            raise ValidationError('The title should not starts with \'A\'')
        return title
    
    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()
        print(cleaned_data)
        author = cleaned_data['author']
        title = cleaned_data['title']
        if author.user.username.lower() == 'bob':
            if title == 'test':
                raise ValidationError('Bob has banned to write test posts')
            
            return cleaned_data
        
        
        return super().clean()