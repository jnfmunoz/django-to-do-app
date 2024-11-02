from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    if field.errors:
        css_class += " is-invalid"
    return field.as_widget(attrs={"class": css_class})
