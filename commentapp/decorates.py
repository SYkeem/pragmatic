
from django.http import HttpResponseForbidden


from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Comment.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden
        return func(request ,*args,**kwargs)

    return decorated