from django import forms

from .models import Profile, Neighbourhood,Comment,Post

class NeighForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    exclude = ['owner','neighbourhood', 'pub_date']

class BusinessForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    exclude = ['User','neighbourhood', 'pub_date']





class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class NeighLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email') 

class NewCommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['neighbourhood','postername','pub_date']      

class NewPostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['poster','postername','neighborhood', 'pub_date']
