from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(OnBoarding)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')