from django import template

from blog.models import Post

register = template.Library()


@register.filter(name='formal_name')
def formal_name(value):
    words = str(value).split()
    if len(words) <= 1:
        return str(value)
    return f"{str(words.pop(0)[0])}. {' '.join(words)}"


@register.inclusion_tag('blog/more_about.html', takes_context=True)
def more_about(context, *args, **kwargs):
    field = args[0]
    post_id = context['post'].pk

    filter = {
        field: getattr(context['post'], field)
    }
    
    custom_title_text = "More about"
    if 'custom_title_text' in kwargs:
        custom_title_text = kwargs['custom_title_text']

    return {
        'title': kwargs['title'],
        'list': Post.objects.filter(**filter).exclude(pk=post_id),
        'custom_title_text': custom_title_text
    }
