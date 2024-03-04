from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Reply

class UserRegisteration(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields = ['username','email','password1','password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']

from django import forms
from .models import Post

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': '4'})

