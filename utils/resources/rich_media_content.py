"""Rich Media Content for Viber bot messages."""
from .tools import rich_message_consctructor


INFO_SETS = [
    ('Топовый сет',
     'https://966.ua/upload/iblock/219/21901567c5b5a926131ad04f793134dd.jpg',
     '1270 грамм 50 кусочек',
     '439₴'),
    ('Якудза сет',
     'https://966.ua/upload/iblock/357/3573b07b30d3e885ec1dc88c7c87a864.jpg',
     '1270 грамм 50 кусочек',
     '539₴'),
    ('Камикадзе сет',
     'https://966.ua/upload/iblock/dca/dcaa6c8d5a2b9ea54c0709d44cd91d5e.png',
     '1200 грамм 52 кусочек',
     '429₴'),
    ('Фуне сет',
     'https://966.ua/upload/iblock/c10/c10f907d2f24b8d5f0c1da35eff28717.jpg',
     '790 грамм 30 кусочек',
     '419₴'),
]

INFO_ROLLS = [
    ('Самая большая Филадельфия',
     'https://966.ua/upload/iblock/dc2/dc2d57cccd7939c68eb43928377517fb.jpg',
     'Лосось, сыр "Филадельфия", огурец, авокадо',
     '155₴'),
    ('Филадельфия с тунцом',
     'https://966.ua/upload/iblock/4ad/4adbe0d8be8513d3b7fc72cd6474f151.jpg',
     'Сыр "Филадельфия", тунец, огурец, авокадо, икра тобико',
     '159₴'),
    ('Филадельфия с угрем',
     'https://966.ua/upload/iblock/f36/f36f644eb2968efc5335b702d55b5133.jpg',
     'Сыр "Филадельфия", угорь, огурец, авокадо, соус "Унаги", кунжут',
     '188₴'),
    ('Туна и трюфель ролл',
     'https://966.ua/upload/iblock/f83/f83cb109939346523b40704eee0cb3ad.jpg',
     'Лосось, тунец, авокадо, японский майонез, икра тобико, лук шнитт, '
     'трюфельный соус, цедра лайма',
     '199₴'),
]

INFO_PIZZA = [
    ('Эмилия',
     'https://images.pizza33.ua/products/product/acTh5RRPNUmiFvNiFIcivb7XUp9Uq4P4.jpg',
     '425 грамм',
     '179₴'),
    ('Грибная с ветчиной',
     'https://images.pizza33.ua/products/product/Oz6dEhM7zH3S76ksiSgHb3WCRIZZwWej.jpg',
     '455 грамм',
     '169₴'),
    ('Гавайская Премиум',
     'https://images.pizza33.ua/products/product/pe6RV4SEkqlbqqUb0R1r2mFrfGCFFkNT.jpg',
     '500 грамм',
     '199₴'),
]

INFO_SNACKS = [
    ('Кальмары по-корейски',
     'https://966.ua/upload/iblock/2e4/2e4713d3acbcf82f4560fb03452dcd92.jpg',
     '210 грамм',
     '43₴'),
    ('Чука с ореховым соусом',
     'https://966.ua/upload/iblock/e89/e891ad5e2fe6b029f160da44e98430af.jpg',
     '100 грамм',
     '48₴'),
    ('Тайский овощной салат',
     'https://966.ua/upload/iblock/9a4/9a4cbb11a117aa85733957edb0972e73.jpg',
     '210 грамм',
     '59₴'),
]

RICH_MEDIA_SETS = rich_message_consctructor(INFO_SETS)
RICH_MEDIA_ROLLS = rich_message_consctructor(INFO_ROLLS)
RICH_MEDIA_PIZZA = rich_message_consctructor(INFO_PIZZA)
RICH_MEDIA_SNACKS = rich_message_consctructor(INFO_SNACKS)
