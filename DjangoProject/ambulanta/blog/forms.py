from django import forms
from .models import Post, Comment

class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title', 'title_tag', 'author', 'body', 'header_image')
        
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-controll','type' : 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control',}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
                
        }
        
        
class EditFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title', 'title_tag', 'author', 'body', 'header_image')
        
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'id':'title_tag'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title Placeholder'}),
            'author': forms.TextInput(attrs={'class': 'form-controll','value':'', 'id':'irena', 'type' : 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'This is body Placeholder'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),

                
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'body')
        widgets={
            'user': forms.HiddenInput(),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }