from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q
from django.shortcuts import get_list_or_404


def questions_filter(request, model):
    request = request.GET

    if 'q' in request:
        query = request['q']
        return model.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    elif 'popular' in request:
        return model.objects.annotate(
            num_likes=Count('likes'),
            num_replies=Count('replies')
        ).order_by('-num_replies', '-num_likes')

    elif 'solved' in request and request['solved'] == '1':
        try:
            return model.objects.filter(solved=1)
        except ObjectDoesNotExist:
            return False

    elif 'solved' in request and request['solved'] == '0':
        try:
            return model.objects.filter(solved=0)
        except ObjectDoesNotExist:
            return False

    elif 'noreplies' in request:
        return model.objects.annotate(num_replies=Count('replies')).filter(num_replies=0)

    return reversed(get_list_or_404(model))