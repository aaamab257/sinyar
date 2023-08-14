from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(OnBoarding)
class OnBoardingTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')


# @register(OffersSlider)
# class OffersTranslationOptions(TranslationOptions):
#     fields = ('title',)