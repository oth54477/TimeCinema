from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@require_http_methods(["GET", "POST"])
def signup2(request):
    if request.user.is_authenticated:
        return redirect("community:index")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("community:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def signup(request):
    # if request.user.is_authenticated:
    #     return redirect("community:index")

    if request.method == "POST":
        a = json.loads(request.body)
        form = CustomUserCreationForm(a)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("community:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    # return render(request, "accounts/signup.html", context)


@require_http_methods(["GET", "POST"])
def login2(request):
    if request.user.is_authenticated:
        return redirect("community:index")

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "community:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def login(request):
    # if request.user.is_authenticated:
    #     return redirect("community:index")
    a = json.loads(request.body)
    if request.method == "POST":
        form = AuthenticationForm(request, a)
        print(form.is_valid)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "community:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    # return render(request, "accounts/login.html", context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect("community:index")


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        "person": person,
    }
    return render(request, "accounts/profile.html", context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                is_followed = False
            else:
                person.followers.add(user)
                is_followed = True
            context = {
                "is_followed": is_followed,
                "followers_count": person.followers.count(),
                "followings_count": person.followings.count(),
            }
        return JsonResponse(context)
