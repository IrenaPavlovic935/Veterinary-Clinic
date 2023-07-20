

from django import forms
from .models import GalleryImage, CommentGallery

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('image',)
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentGallery
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Reply

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        