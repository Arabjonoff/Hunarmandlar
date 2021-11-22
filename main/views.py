from django.shortcuts import render
from django.views.generic import View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.http import JsonResponse

# Create your views here.
class HomeView(ListView):
    def get(self,request):
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            'cat':categories,
            'pro':products
        }
        return render(request,'index.html',context)
    def post(self,request):
        return render(request,'index.html')

def profile(request):
    user = request.user
    s_user = user.socialaccount_set.all()[0]
    d = s_user.extra_data   
    data = {
    'data':d
    }
    return render(request, 'account/profile.html', {'data':data})

def like(request):
    user_id = request.GET.get('user_id')
    post_id = request.GET.get('post_id')
    user = User.objects.get(id=user_id)
    post = Product.objects.get(id=post_id)
    if user in post.like.all():
        post.like.add(user)
        post.save()
        return JsonResponse({'status':'like'})
    else:
        post.like.remove(user)
        post.save()
        return JsonResponse({'status':'dislike'})
    
