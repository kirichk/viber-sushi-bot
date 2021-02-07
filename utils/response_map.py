from .resources import rich_media_content as rm

RICH_RESPONSE_MAP = {
    'sets': ['Выбор сетов', rm.RICH_MEDIA_SETS],
    'rolls': ['Выбор роллов', rm.RICH_MEDIA_ROLLS],
    'guncans': ['Выбор гунканов', rm.RICH_MEDIA_GUNCANS],
    'sushi': ['Выбор суши', rm.RICH_MEDIA_SUSHI],
    'pizza': ['Выбор пиццы', rm.RICH_MEDIA_PIZZA],
    'combo': ['Выбор комбо', rm.RICH_MEDIA_COMBO],
    'nuggets_wings': ['Выбор наггетсов и крылишек', rm.RICH_MEDIA_NUGGETS_WINGS],
    'mussils': ['Выбор мидий', rm.RICH_MEDIA_MUSSILS],
    'sauces': ['Выбор соусов', rm.RICH_MEDIA_SAUCES],
    'drinks': ['Выбор напитков', rm.RICH_MEDIA_DRINKS]
}
