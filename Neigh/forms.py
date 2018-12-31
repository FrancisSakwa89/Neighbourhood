from django import forms

from .models import Profile, Neighbourhood,Comment,Business,Post, Contact

class NeighForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    exclude = ['owner','neighbourhood', 'pub_date']

class NewBusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ['pub_date']





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
    exclude = ['pub_date']      

class NewPostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['poster', 'pub_date']

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    exclude = ['post','postername','pub_date']