from django import template

register = template.Library()

@register.filter('can_be_viewed_by')
def can_be_viewed_by(obj, user):
    return obj.can_be_viewed_by(user)

@register.filter('can_be_edited_by')
def can_be_edited_by(obj, user):
    return obj.can_be_edited_by(user)

@register.filter('can_be_deleted_by')
def can_be_deleted_by(obj, user):
    return obj.can_be_deleted_by(user)

@register.filter('can_be_copied_by')
def can_be_copied_by(obj, user):
    return obj.can_be_copied_by(user)
