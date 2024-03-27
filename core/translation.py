from modeltranslation.translator import translator,TranslationOptions
from core.models import Blog,FAQ

class BlogTranslationOptions(TranslationOptions):
    fields=('title','description')

translator.register(Blog,BlogTranslationOptions)

class FAQTranslationOptions(TranslationOptions):
    fields=('question','answer')
translator.register(FAQ,FAQTranslationOptions)