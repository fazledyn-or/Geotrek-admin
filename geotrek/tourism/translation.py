from django.conf import settings

from modeltranslation.translator import translator, TranslationOptions

from geotrek.tourism import models as tourism_models


class DataSourceTO(TranslationOptions):
    fields = ('title',)

translator.register(tourism_models.DataSource, DataSourceTO)


class InformationDeskTO(TranslationOptions):
    fields = ('name', 'description')

translator.register(tourism_models.InformationDesk, InformationDeskTO)


class InformationDeskTypeTO(TranslationOptions):
    fields = ('label',)

translator.register(tourism_models.InformationDeskType, InformationDeskTypeTO)


class TouristicContentTO(TranslationOptions):
    fields = ('name',) + (('published',) if settings.PUBLISHED_BY_LANG else tuple())
    fallback_undefined = {'published': None}

translator.register(tourism_models.TouristicContent, TouristicContentTO)


class TouristicContentCategoryTO(TranslationOptions):
    fields = ('label',)

translator.register(tourism_models.TouristicContentCategory,
                    TouristicContentCategoryTO)


class TouristicEventUsageTO(TranslationOptions):
    fields = ('usage',)

translator.register(tourism_models.TouristicEventUsage, TouristicEventUsageTO)


class TouristicEventPublicTO(TranslationOptions):
    fields = ('public',)

translator.register(tourism_models.TouristicEventPublic, TouristicEventPublicTO)


class TouristicEventTO(TranslationOptions):
    fields = ('name', 'description_teaser', 'description', 'meeting_point',
              'accessibility', 'booking', 'practical_info')

translator.register(tourism_models.TouristicEvent, TouristicEventTO)
