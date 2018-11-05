from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm, UserSignupForm
from .models import Post


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        response = [
            "{id}: {title} by {author} <br>".format(id=p.id, title=p.title, author=p.author)
            for p in posts
        ]
        return HttpResponse(response)


class PostDetailView(TemplateView):
    template_name = 'blog/detail.html'
    def get(self, request, id):
        try:
            p = Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404()
        else:
            context = {
                'title': p.title,
                'author': p.author,
                'body': p.body
            }
            # response = """
            # {title} by {author}
            # <br>
            # ---
            # <br><br>
            # {body}
            # """.format(title=p.title, author=p.author, body=p.body)
            # return HttpResponse(response)
            return self.render_to_response(context)


class PostCreateView(TemplateView):
    template_name = 'blog/create.html'

    def get(self, request):
        form = PostForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = PostForm(data=request.POST)
        if not form.is_valid():
            return self.render_to_response({'errors': form.errors})

        post = form.save()
        return HttpResponseRedirect(reverse('blog:posts-detail', kwargs={'id': post.id}))


class PostEditView(TemplateView):
    template_name = 'blog/edit.html'
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        form = PostForm(instance=post)

        return self.render_to_response({'form': form, 'id': id})

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        form = PostForm(data=request.POST, instance=post)
        if not form.is_valid():
            return self.render_to_response({'errors': form.errors})

        post = form.save()
        return HttpResponseRedirect(reverse('blog:posts-detail', kwargs={'id': post.id}))


class SignupView(TemplateView):
    template_name = 'blog/signup.html'

    def get(self, request):
        form = UserSignupForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = UserSignupForm(data=request.POST)
        if not form.is_valid():
            return self.render_to_response({'form': form})

        user = form.save()

        return HttpResponseRedirect(reverse('blog:posts'))
