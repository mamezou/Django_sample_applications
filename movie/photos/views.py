from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .forms import PhotoCreateForm
from .models import Photo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST


class IndexView(generic.ListView):
    model = Photo


class CreateView(generic.CreateView):
    model = Photo
    form_class = PhotoCreateForm
    success_url = reverse_lazy('photos:photo')


# def users_detail(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     return render(request, 'photos/users_detail.html', {'user': user})
#
#
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST) # ユーザーインスタンスを作成
#         if form.is_valid():
#             new_user = form.save() # ユーザーインスタンスを保存
#             input_username = form.cleaned_data['username']
#             input_password = form.cleaned_data['password1']
#             # フォームの入力値で認証できればユーザーオブジェクト、できなければNoneを返す
#             new_user = authenticate(username=input_username, password=input_password)
#             # 認証成功時のみ、ユーザーをログインさせる
#             if new_user is not None:
#                 # loginメソッドは、認証ができてなくてもログインさせることができる。→上のauthenticateで認証を実行する
#                 login(request, new_user)
#                 return redirect('app:users_detail', pk=new_user.pk)
#     else:
#         form = UserCreationForm()
#     return render(request, 'app/signup.html', {'form': form})
#
#
# def photos_detail(request, pk):
#     photo = get_object_or_404(Photo, pk=pk)
#     return render(request, 'app/photos_detail.html', {'photo': photo})
#
#
# @require_POST
# def photos_delete(request, pk):
#     photo = get_object_or_404(Photo, pk=pk)
#     photo.delete()
#     return redirect('app:users_detail', request.user.id)
