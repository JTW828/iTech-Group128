from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_backends
from django.contrib import messages
from .forms import RegisterForm
from .models import Store, Like, Favourite, Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def login_view(request):
    if request.method == "POST":
        login_input = request.POST.get("login")  
        password = request.POST.get("password")  
        
        # 进行身份验证
        user = authenticate(request, username=login_input, password=password) 

        if user is not None:
            login(request, user) 
            return redirect("home") 
        else:
            messages.error(request, "Invalid username/email or password.") 
    return render(request, "login.html")



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = get_backends()[0].__module__ + "." + get_backends()[0].__class__.__name__
            login(request, user)
            return redirect('login')  # 注册成功后跳转到 home 页面
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')



def store_list(request):
    city_query = request.GET.get('city')
    stores = Store.objects.filter(city__icontains=city_query) if city_query else []
    return render(request, 'store_list.html', {
        'stores': stores,
        'city': city_query
    })


def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    user = request.user

    liked = Like.objects.filter(store=store, user=user).exists()
    favourited = Favourite.objects.filter(store=store, user=user).exists()

    like_count = Like.objects.filter(store=store).count()
    favourite_count = Favourite.objects.filter(store=store).count()

    return render(request, 'store_detail.html', {
        'store': store,
        'liked': liked,
        'favourited': favourited,
        'like_count': like_count,
        'favourite_count': favourite_count})


@login_required
def profile_view(request):
    profile = request.user
    favourites = Favourite.objects.filter(user=request.user)

    if request.method == 'POST':
        location = request.POST.get('location')
        avatar = request.FILES.get('avatar')

        if location:
            profile.location = location
        if avatar:
            profile.avatar = avatar

        profile.save()
        return redirect('profile')

    return render(request, 'profile.html')



def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    user = request.user

    # 获取点赞和收藏的状态
    liked = Like.objects.filter(store=store, user=user).exists() if user.is_authenticated else False
    favourited = Favourite.objects.filter(store=store, user=user).exists() if user.is_authenticated else False

    like_count = Like.objects.filter(store=store).count()
    favourite_count = Favourite.objects.filter(store=store).count()
    
    #comment
    comments = Comment.objects.filter(store=store).order_by('-created_at')  # 按时间倒序排列
    
    return render(request, 'store_detail.html', {
        'store': store,
        'liked': liked,
        'favourited': favourited,
        'like_count': like_count,
        'favourite_count': favourite_count,
        'comments': comments,
    })



@login_required
def like_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    user = request.user

    like = Like.objects.filter(store=store, user=user).first()
    
    if like:
        like.delete()
        liked = False
    else:
        Like.objects.create(store=store, user=user)
        liked = True

    like_count = Like.objects.filter(store=store).count()
    return JsonResponse({"liked": liked, "like_count": like_count})



@login_required
def favourite_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    user = request.user

    favourite = Favourite.objects.filter(store=store, user=user).first()

    if favourite:
        favourite.delete()
        favourited = False
    else:
        Favourite.objects.create(store=store, user=user)
        favourited = True

    favourite_count = Favourite.objects.filter(store=store).count()
    return JsonResponse({"favourited": favourited, "favourite_count": favourite_count})


@login_required
def add_comment(request, store_id):
    if request.method == "POST":
        store = get_object_or_404(Store, id=store_id)
        content = request.POST.get("content")

        if content:
            comment = Comment.objects.create(user=request.user, store=store, content=content)
            return JsonResponse({
                "username": request.user.username,
                "content": comment.content,
                "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M")
            })

    return JsonResponse({"error": "Invalid request"}, status=400)
