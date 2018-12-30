from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import NeighForm, NewBusinessForm, ProfileForm,NewCommentForm, ContactForm
from .models import Neighbourhood, Business, Profile,NeighLetterRecipients,Post,Comment
from .email import send_welcome_email
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import NeighbourhoodSerializer, ProfileSerializer
from .forms import NeighLetterForm
from .models import Profile, Post, Comment, Business, Neighbourhood, Contact

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  # neighbourhoods = Neighbourhood.objects.all().order_by()

  return render(request, 'index.html',{'profile':profile})


@login_required(login_url='/accounts/login/')
def myneighbourhood(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)
  neighbourhoods = Neighbourhood.objects.all().order_by()

#   try:
#     posts = Post.objects.filter(neighbourhood=profile.neighbourhood).order_by()

#   except ObjectDoesNotExist:
#     posts = []

  return render(request, 'myneigh.html',{'profile':profile,'neighbourhoods':neighbourhoods})

@login_required(login_url='/accounts/login/')
def password(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  # neighbourhoods = Neighbourhood.objects.all().order_by()

  return render(request, 'password.html',{'profile':profile})



class BusinessList(APIView):
  def get(self, request, format=None):
    all_neighbourhoods = neighbourhood.objects.all()
    serializers = neighbourhoodserializer(all_neighbourhoods, many=True)
    return Response(serializers.data)

def mail(request):
  name = request.user.username
  email = request.user.email
  
  send_welcome_email(name,email)

  return HttpResponseRedirect(reverse('welcome'))

@login_required(login_url='/accounts/login/')
def newbusiness(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  if request.method == 'POST':
    form = NewBusinessForm(request.POST)
    if form.is_valid():
      business = form.save(commit=False)
      business.neighbourhood = profile.neighbourhood
      business.save()
    return redirect('business')

  else:
    form = NewBusinessForm()

  return render(request, 'newbusiness.html',{'form':form,'profile':profile})


@login_required(login_url='/accounts/login/')
def newneighbourhood(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = NeighForm(request.POST, request.FILES)
    if form.is_valid():
      neighbourhood = form.save(commit=False)
      neighbourhood.owner = current_user
      neighbourhood.neighbourhood = current_username
      neighbourhood.save()
    return redirect('welcome')

  else:
    form = NeighForm()

  return render(request, 'newneigh.html',{'form':form,'profile':profile})



# @login_required(login_url='/accounts/login/')
# def newrating(request,id):
#   frank = request.user.id
#   profile = Profile.objects.get(user=frank)
#   id = id

#   current_username = request.user.username

#   if request.method == 'POST':
#     form = RatingForm(request.POST)
#     if form.is_valid():
#       rating = form.save(commit=False)

#       design_rating = form.cleaned_data['design']
#       usability_rating = form.cleaned_data['usability']
#       content_rating = form.cleaned_data['content']

#       avg = ((design_rating + usability_rating + content_rating)/3)

#       rating.average = avg
#       rating.ownername = current_username
#       rating.neighbourhood = neighbourhood.objects.get(pk=id)

#       rating.save()
#     return redirect('neighbourhood',id)

#   else:
#     form = RatingForm()

#   return render(request, 'rating.html',{'form':form,'profile':profile,'id':id})

@login_required(login_url='/accounts/login/')
def profile(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  user = request.user
  

  neighbourhoods = Neighbourhood.objects.filter(post=frank).order_by()
  neighbourhoodcount=neighbourhoods.count()


  return render(request, 'photos/profile.html',{'profile':profile,'user':user,'neighbourhoodcount':neighbourhoodcount,'neighbourhoods':neighbourhoods})


@login_required(login_url='/accounts/login/')
def neighbourhood(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  
  neighbourhoods = Neighbourhood.objects.get(pk=id)
#   neighbourhoods = Neighbourhood.objects.get(pk=id)
  # comments = Comment.objects.filter(neighbourhood=id).order_by()

  return render(request, 'photos/neigh.html',{'profile':profile,'neighbourhood':neighbourhood})



@login_required(login_url='/accounts/login/')
def post(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  
  post = Post.objects.get(pk=id)
  comments = Comment.objects.filter(post=id).order_by()

  return render(request, 'post.html',{'profile':profile,'post':post,'comments':comments})



@login_required(login_url='/accounts/login/')
def newprofile(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  # current_user = request.user
  # current_username = request.user.username
  
  if request.method == 'POST':
    instance = get_object_or_404(Profile, user=frank)
    form = ProfileForm(request.POST, request.FILES,instance=instance)
    if form.is_valid():
      form.save()
      # u_profile = form.save(commit=False)
      # u_profile.user = current_user
      # u_profile.save()

    return redirect('profile', frank)

  else:
    form = ProfileForm()

  return render(request, 'newprofile.html',{'form':form,'profile':profile})


@login_required(login_url='/accounts/login/')
def contacts(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  try:
    contacts = Contact.objects.filter(neighbourhood=profile.neighbourhood)

  except ObjectDoesNotExist:
    contacts = []

  return render(request, 'contacts.html',{'contacts':contacts,'profile':profile})


@login_required(login_url='/accounts/login/')
def newcontacts(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = ContactForm(request.POST, request.FILES)
    if form.is_valid():
      contacts = form.save(commit=False)
      contacts.owner = current_user
      contacts.contacts = current_username
      contacts.save()
    return redirect('welcome')

  else:
    form = ContactForm()

  return render(request, 'newcontacts.html',{'form':form,'profile':profile})



@login_required(login_url='/accounts/login/')
def subscribe(request):
    id = request.user.id
    profile = Profile.objects.get(user=id)
    if request.method == 'POST':
        form = NeighLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NeighLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('index.html')
    else:
        form = NeighLetterForm()
    return render(request, 'subscribe.html', {'letterForm':form,'profile':profile})    

@login_required(login_url='/accounts/login/')
def newpost(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = NewPostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.poster = current_user
      post.postername = current_username
      post.neighbourhood = profile.neighbourhood
      post.save()
    return redirect('welcome')

  else:
    form = NewPostForm()

  return render(request, 'newpost.html',{'form':form,'profile':profile})




@login_required(login_url='/accounts/login/')
def newcomment(request,id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  id = id

  current_username = request.user.username
  if request.method == 'POST':
    form = NewCommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.postername = current_username
      comment.neighbourhood = neighbourhood.objects.get(pk=id)
      comment.save()
    return redirect('neighbourhood',id)

  else:
    form = NewCommentForm()

  return render(request, 'newcomment.html',{'form':form,'profile':profile,'id':id})


@login_required(login_url='/accounts/login/')
def business(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)
  # return redirect('welcome')

  try:
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

  except ObjectDoesNotExist:
    businesses = []
  # return redirect('welcome')

  return render(request, 'business.html',{'businesses':businesses,'profile':profile})

@login_required(login_url='/accounts/login/')
def search_results(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)


  if 'business' in request.GET and request.GET['business']:
    search_term = request.GET.get('business')
    message = f'{search_term}'
    title = 'Search Results'

    try:
      no_ws = search_term.strip()
      searched_business = Business.objects.filter(name__icontains = no_ws)
      searched_businesses = searched_business.filter(neighbourhood=profile.neighbourhood)

    except ObjectDoesNotExist:
      searched_businesses = []

    return render(request, 'search.html',{'message':message ,'title':title, 'searched_businesses':searched_businesses,'profile':profile})

  else:
    message = 'You haven\'t searched for any business'
    
    title = 'Search Error'
    return render(request,'search.html',{'message':message,'title':title,'profile':profile})
