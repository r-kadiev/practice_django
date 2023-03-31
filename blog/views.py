from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Category,Tag,Post,Comment


class HomeView(View):

    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.all()
        context = {
            "categories": category_list,
            "posts": post_list,
        }
        return render(request, 'blog/home.html', context=context)


class CategoryView(View):

    def get(self, request, slug):
        category_post = Category.objects.get(slug=slug)
        return render(request, 'blog/post_list.html', {"category": category_post})