import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.sane_lists',
        'markdown.extensions.toc',
    ]
    
    html = markdown.markdown(text, extensions=extensions)
    return mark_safe(html)