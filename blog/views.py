from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, Http404
from .models import Post


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        response = [
            "{id}: {title} by {author} <br>".format(id=p.id, title=p.title, author=p.author)
            for p in posts
        ]
        return HttpResponse(response)


class PostDetailView(View):
    def get(self, request, id):
        try:
            p = Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404()
        else:
            response = """
            {title} by {author}
            <br>
            ---
            <br><br>
            {body}
            """.format(title=p.title, author=p.author, body=p.body)
            return HttpResponse(response)
