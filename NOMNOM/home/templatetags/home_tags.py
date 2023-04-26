from django import template

register = template.Library()

from ..models import Restaurant, Item
