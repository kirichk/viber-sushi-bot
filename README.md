# VIBER SUSHI BOT

## Tasks completed:
1. При запуске бота отображается приветствие
2. После приветствия пользователь шарит свой номер телефона
3. Пользователю отображаются три кнопки "Сеты", "Ролы","Пиццы" и "Закуски"
4. После выбора категории отображаются названия блюд
5. После выбора интересующее блюдо попадает в корзину.
  Но этом шаге пользователю отображается 2 кнопки "Оформить заказ" и "Меню".
6. После нажатия кнопки оформления заказа, информация отправляется в 
  вайбер менеджера (к-во блюд, имя и номер клиента
7. У клиента есть возможность оставлять комментарии к заказу

+ Добавлена возможность отправлять локацию для доставки

## How to install
1. Clone repository `git clone https://github.com/kirichk/viber-sushi-bot.git`
2. Enter repository `cd viber-sushi-bot`
3. Create virtual environment `python -m venv env`
4. Activate virtual environment `source env/bin/activate`
5. Install packages `pip install -r requirements.txt`
6. Enter utils folder `cd utils`
7. Create .env file with creadentials such as *TOKEN* and *ADMIN*. 
  Also add *URL* variable which should comtain webhook address.
8. Set webhook `python set_webhook.py`
9. To launch a bot just return to main directory `cd ..` and run `python go.py`
