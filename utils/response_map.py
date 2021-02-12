from .resources import rich_media_content as rm
from .resources import keyboards_content as kb
from .resources import texts as txt


RICH_RESPONSE_MAP = {
    'sets': ['Выбор сетов',
             rm.RICH_MEDIA_SETS],
    'rolls': ['Выбор роллов',
              rm.RICH_MEDIA_ROLLS],
    'guncans': ['Выбор гунканов',
                rm.RICH_MEDIA_GUNCANS],
    'sushi': ['Выбор суши',
              rm.RICH_MEDIA_SUSHI],
    'pizza': ['Выбор пиццы',
              rm.RICH_MEDIA_PIZZA],
    'combo': ['Выбор комбо',
              rm.RICH_MEDIA_COMBO],
    'nuggets_wings': ['Выбор наггетсов и крылишек',
                      rm.RICH_MEDIA_NUGGETS_WINGS],
    'mussils': ['Выбор мидий',
                rm.RICH_MEDIA_MUSSILS],
    'noodles': ['Выбор лапшы',
                rm.RICH_MEDIA_NOODLES],
    'shrimps': ['Выбор креветок',
                rm.RICH_MEDIA_SHRIMPS],
    'sauces': ['Выбор соусов',
               rm.RICH_MEDIA_SAUCES],
    'drinks': ['Выбор напитков',
               rm.RICH_MEDIA_DRINKS]
}

KEYBOARD_RESPONSE_MAP = {
    'sets_rolls': ['Выберите интересующую Вас подкатегорию.',
                   kb.SETS_ROLLS_KEYBOARD],
    'guncans_sushi': ['Выберите интересующую Вас подкатегорию.',
                      kb.GUNCANS_SUSHI_KEYBOARD],
    'pizza_snacks': ['Выберите интересующую Вас подкатегорию.',
                     kb.PIZZA_SNACKS_KEYBOARD],
    'other': ['Выберите интересующую Вас подкатегорию.',
              kb.OTHER_KEYBOARD],
    'offers': [txt.OFFERS,
               kb.GO_TO_MENU_KEYBOARD],
    'delivery': [txt.DELIVERY,
                 kb.GO_TO_MENU_KEYBOARD],
    'menu': ['Выберите интересующую Вас категорию.',
             kb.MENU_KEYBOARD],
    'address': ['Укажите адрес доставки заказа. '\
                     'Для этого нажмите Отправить Локацию.',
                     kb.SHARE_LOCATION_KEYBOARD],
    'confirmation': ['Выберите желаемый способ забрать заказ.',
                     kb.DELIVERY_TYPE_KEYBOARD]
}
