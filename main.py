import telebot
from telebot import types
import sqlite3



bot = telebot.TeleBot('5943446610:AAED2hJ7xEUU-TtygGs_6kdcdep0eQUDNMs')




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    menu_button = types.InlineKeyboardButton('Меню', callback_data='menu')
    markup.add(menu_button)
    bot.send_message(message.chat.id, "Выберите один из вариантов:", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def handle_menu(callback_query):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('• Информация о курсе Amazon 👨🏻💻 ', callback_data='introduction')
    btn2 = types.InlineKeyboardButton('• Что необходимо для курса? 📌', callback_data='sales_strategy')
    btn3 = types.InlineKeyboardButton('• Как записаться? 📩', callback_data='language_barriers')
    btn4 = types.InlineKeyboardButton('• Записаться на консультацию', callback_data='registration')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(btn4)
    bot.send_message(callback_query.from_user.id, "Выберите один из вариантов:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'introduction')
def handle_menu(callback_query):
    markup = types.InlineKeyboardMarkup()

    # Кнопки внутри раздела "Информация о курсе Amazon"
    introduction_btn = types.InlineKeyboardButton('Онлайн формат:', callback_data='introduction_btn')
    sales_strategy_btn = types.InlineKeyboardButton('Оффлайн формат:', callback_data='sales_strategy_btn')
    language_barriers_btn = types.InlineKeyboardButton('Индивидуальное обучение:', callback_data='language_barriers_btn')

    # Добавление кнопок в разметку
    markup.row(introduction_btn)
    markup.row(sales_strategy_btn)
    markup.row(language_barriers_btn)

    bot.send_message(callback_query.from_user.id, "Выберите один из вариантов:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'introduction_btn')
def handle_introduction(callback_query):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Программа обучения', callback_data='button1')
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    btn2 = types.InlineKeyboardButton('График обучения', callback_data='button2')
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    # btn3 = types.InlineKeyboardButton('Обратная связь', callback_data='button3')
    # back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    btn4 = types.InlineKeyboardButton('Длительность обучения', callback_data='button4')
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    btn6 = types.InlineKeyboardButton('Стоимость курса', callback_data='button6')
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')

    markup.row(btn1)
    markup.row(btn2)
    # markup.row(btn3)
    markup.row(btn4)
    markup.row(btn6)
    markup.row(back_button)

    bot.send_message(callback_query.from_user.id, "Выберите один из вариантов онлайн формата:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'button1')
def handle_button(callback_query):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.row(back_button)
    # bot.send_message(callback_query.from_user.id, "Программа обучения:", reply_markup=markup)
    program_description = '''
        Программа обучения: 

Курс бизнес в AMAZON💵

✔️ Ознакомление с бизнес моделями работы в Амазон;
✔️ Обучение стратегии FLIPPING с нуля;
✔️ Как можно работать из любой точки мира открыв бизнес в Амазон;
✔️ Алгоритм запуска продаж в Амазон;
✔️ Регистрация аккаунта в Амазон;
✔️ Как правильно проводить аналитику и использовать сервисы по аналитике;
✔️ Инструменты по поиску товаров и выход на продажу;
✔️ Вывод средств с аккаунта Амазон на свой банковский счет;
✔️ Также все инструменты по запуску бизнеса в Амазон и поделимся всеми знаниями которыми обладаем;
        '''

    bot.send_message(callback_query.from_user.id, program_description, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'button2')
def handle_button(callback_query):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.row(back_button)
    # bot.send_message(callback_query.from_user.id, "Привет, График обучения", reply_markup=markup)
    graph_description = '''
        📅График обучения:

График обучения онлайн курса, рассчитано на ваше удобство. 
Курс проходит на специальной платформе, где вам даётся доступ к урокам. 
Также будет создана группа в телеграмм для обратной связи от меня и кураторов.
        '''

    bot.send_message(callback_query.from_user.id, graph_description, reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: call.data == 'button3')
# def handle_button(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, Обратная связь", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'button4')
def handle_button(callback_query):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.row(back_button)
    # bot.send_message(callback_query.from_user.id, "Привет, Длительность обучения", reply_markup=markup)
    duration_description = '''
        Длительность обучения:
    
Длительность обучения 2 месяца. 
После окончания курса, сопровождение после окончания курса будет длиться до 6 месяцев. 

При возникновении вопросов можете писать в группу👍
        '''

    bot.send_message(callback_query.from_user.id, duration_description, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'button6')
def handle_button(callback_query):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.row(back_button)
    # bot.send_message(callback_query.from_user.id, "Привет, Стоимость курса", reply_markup=markup)
    cost_description = '''
Стоимость онлайн курса - 250$
(В сомах можно перевести по актуальному курсу)
       '''

    bot.send_message(callback_query.from_user.id, cost_description, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'sales_strategy_btn')
def handle_sales_strategy(callback_query):
    markup = types.InlineKeyboardMarkup()

    # Кнопки внутри раздела "Что необходимо для курса?"
    button1 = types.InlineKeyboardButton('Программа обучения', callback_data='sales_strategy_btn1')
    button2 = types.InlineKeyboardButton('График обучения', callback_data='sales_strategy_btn2')
    # button3 = types.InlineKeyboardButton('Обратная связь', callback_data='sales_strategy_btn3')
    button4 = types.InlineKeyboardButton('Длительность обучения', callback_data='sales_strategy_btn4')
    button6 = types.InlineKeyboardButton('Стоимость курса', callback_data='sales_strategy_btn6')
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')

    markup.row(button1)
    markup.row(button2)
    # markup.row(button3)
    markup.row(button4)
    markup.row(button6)
    markup.row(back_button)

    bot.send_message(callback_query.from_user.id, "Выберите один из вариантов Оффлайн формата:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'sales_strategy_btn1')
def handle_sales_strategy_btn1(callback_query):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.row(back_button)
    # bot.send_message(callback_query.from_user.id, "Привет, Программа курса", reply_markup=markup)
    course_program = '''
        Курс бизнес в AMAZON💵

✔️ Ознакомление с бизнес моделями работы в Амазон;
✔️ Обучение стратегии FLIPPING с нуля;
✔️ Как можно работать из любой точки мира открыв бизнес в Амазон;
✔️ Алгоритм запуска продаж в Амазон;
✔️ Регистрация аккаунта в Амазон;
✔️ Как правильно проводить аналитику и использовать сервисы по аналитике;
✔️ Инструменты по поиску товаров и выход на продажу;
✔️ Вывод средств с аккаунта Амазон на свой банковский счет;
✔️ Также все инструменты по запуску бизнеса в Амазон и поделимся всеми знаниями которыми обладаем;
        '''

    bot.send_message(callback_query.from_user.id, course_program, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'sales_strategy_btn2')
def handle_sales_strategy_btn2(callback_query):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.row(back_button)
    # bot.send_message(callback_query.from_user.id, "Привет, График обучения", reply_markup=markup)
    schedule_description = '''
        График обучения оффлайн курса

Уроки проходят 3 раза в неделю, по 2 часа. 
По вторникам, четвергам и субботам. 

Утренняя группа: с 9:00-11:00 
Дневная группа: с 14:00 - 16:00
Вечерняя группа: с 19:00 - 21:00 

В зависимости от своего графика, можете выбрать удобное для вас время!
        '''

    bot.send_message(callback_query.from_user.id, schedule_description, reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: call.data == 'sales_strategy_btn3')
# def handle_sales_strategy_btn2(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, Обратная связь", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'sales_strategy_btn4')
def handle_sales_strategy_btn2(callback_query):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.row(back_button)
    # bot.send_message(callback_query.from_user.id, "Привет, Длительность обучения", reply_markup=markup)
    duration_description = '''
Длительность обучения 2 месяца. 
Сопровождение после окончания курса, до 6 месяцев. 

При возникновении вопросов можете писать в группу или же подойти к нам в офис👍
        '''

    bot.send_message(callback_query.from_user.id, duration_description, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'sales_strategy_btn6')
def handle_sales_strategy_btn2(callback_query):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.row(back_button)
    # bot.send_message(callback_query.from_user.id, "Привет, Стоимость курса", reply_markup=markup)
    cost_description = '''
Стоимость оффлайн курса - 350$ 
(В сомах можно перевести по актуальному курсу)
        '''

    bot.send_message(callback_query.from_user.id, cost_description, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'language_barriers_btn')
def handle_sales_strategy(callback_query):
    markup = types.InlineKeyboardMarkup()

    # Кнопки внутри раздела "Что необходимо для курса?"
    # button1 = types.InlineKeyboardButton('Программа курса', callback_data='language_barriers_btn1')
    # button2 = types.InlineKeyboardButton('График обучения', callback_data='language_barriers_btn2')
    # button3 = types.InlineKeyboardButton('Обратная связь', callback_data='language_barriers_btn3')
    # button4 = types.InlineKeyboardButton('Длительность обучения', callback_data='language_barriers_btn4')
    # button6 = types.InlineKeyboardButton('Стоимость курса', callback_data='language_barriers_btn6')
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')

    # markup.row(button1)
    # markup.row(button2)
    # markup.row(button3)
    # markup.row(button4)
    # markup.row(button6)
    markup.row(back_button)

    # bot.send_message(callback_query.from_user.id, "Выберите один из вариантов индивидуального обучения:", reply_markup=markup)
    individual_training_description = '''
        Индивидуальное обучение со мной 💸

Преимущество Индивидуального обучения заключается в предоставлении ГОТОВОГО АККАУНТА на Амазон, что позволяет выйти на результат намного быстрее✅

График обучения согласовывается индивидуально, исходя из вашего графика.

Длительность обучения 1-2 месяца, в зависимости от графика и от Вашей успеваемости.

Стоимость обучения 1000$
        '''

    bot.send_message(callback_query.from_user.id, individual_training_description, reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers_btn1')
# def handle_sales_strategy_btn1(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, Программа курса", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers_btn2')
# def handle_sales_strategy_btn2(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, График обучения", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers_btn3')
# def handle_sales_strategy_btn2(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, Обратная связь", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers_btn4')
# def handle_sales_strategy_btn2(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, Длительность обучения", reply_markup=markup)
#
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers_btn6')
# def handle_sales_strategy_btn2(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, Стоимость курса", reply_markup=markup)







# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers')
# def handle_sales_strategy(callback_query):
#     markup = types.InlineKeyboardMarkup()
#
#     # Кнопки внутри раздела "Что необходимо для курса?"
#     button1 = types.InlineKeyboardButton('Программа курса', callback_data='language_barriers1')
#     button2 = types.InlineKeyboardButton('График обучения', callback_data='language_barriers2')
#     button3 = types.InlineKeyboardButton('Записаться на консультацию', callback_data='language_barriers3')
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#
#     markup.row(button1)
#     markup.row(button2)
#     markup.row(button3)
#     markup.row(back_button)
#
#     bot.send_message(callback_query.from_user.id, "Выберите один из вариантов Как Записаться:", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers1')
# def handle_sales_strategy_btn1(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, Программа курса", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers2')
# def handle_sales_strategy_btn2(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, График обучения", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers3')
# def handle_sales_strategy_btn2(callback_query):
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.row(back_button)
#     bot.send_message(callback_query.from_user.id, "Привет, Записаться на консультацию", reply_markup=markup)






# D:/SQLiteStudio/db_amazon_2023
# D:/SQLiteStudio/database.db_amazon_2023

@bot.callback_query_handler(func=lambda call: call.data == 'sales_strategy')
def handle_sales_strategy(callback_query):
    requirements_and_investments = '''
    Для обучения необходимо:

- Наличие ноутбука 💻
- Умение пользоваться ноутбуком на уровне уверенного пользователя 🧑‍💻
- 3-4 часа времени в день ⏳
( знание английского языка - необязательно)

Также для старта, вложения в размере 500$ на товарооборот
    '''

    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.add(back_button)

    bot.send_message(callback_query.from_user.id, requirements_and_investments, reply_markup=markup)






@bot.callback_query_handler(func=lambda call: call.data == 'language_barriers')
def handle_sales_strategy(callback_query):
    requirements_and_investments11 = '''
Для того, чтобы записаться на курс, необходимо внести предоплату в размере 100$ на следующие реквизиты: 

✅Реквизиты для оплаты курса💳

4169585347460833 -Optima bank. Шаршенов Чубак
 
+996702120001 M bank 
0555577001 Элсом

⚠️Не забудьте отправить чек после проведения оплаты🧾
    '''

    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
    markup.add(back_button)

    bot.send_message(callback_query.from_user.id, requirements_and_investments11, reply_markup=markup)






# @bot.callback_query_handler(func=lambda call: call.data == 'language_barriers')
# def handle_language_barriers(callback_query):
#     bot.send_message(callback_query.from_user.id, "Привет это Ближайший курс /Предоплата /Реквизиты")
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.add(back_button)
#      bot.send_message(callback_query.from_user.id, "Нажмите кнопку, чтобы вернуться в меню.", reply_markup=markup)

# conn = sqlite3.connect('D:/SQLiteStudio/db_amazon_2023', check_same_thread=False)
# cursor = conn.cursor()
#
# def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
#     cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
#                     (user_id, user_name, user_surname, username))
#     conn.commit()
#
# @bot.callback_query_handler(func=lambda call: call.data == 'registration')
# def handle_registration(callback_query):
#     @bot.message_handler(func=lambda message: True)
#     def get_text_messages(message):
#         if message.text.lower() == 'привет':
#             bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')
#
#             user_id = message.from_user.id
#             user_name = message.from_user.first_name
#             user_surname = message.from_user.last_name
#             username = message.from_user.username
#
#             db_table_val(user_id=user_id, user_name=user_name, user_surname=user_surname, username=username)
#
#     markup = types.InlineKeyboardMarkup()
#     back_button = types.InlineKeyboardButton('Back to menu', callback_data='menu')
#     markup.add(back_button)
#     bot.send_message(callback_query.from_user.id, "Нажмите кнопку, чтобы вернуться в меню.", reply_markup=markup)




import re
import sqlite3
from telebot import types

conn = sqlite3.connect('D:/SQLiteStudio/db_agit push -u origin maingit push -u origin mainn_2023', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, email: str, phone_number: str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username, email, phone_number) VALUES (?, ?, ?, ?, ?, ?)',
                    (user_id, user_name, user_surname, username, email, phone_number))
    conn.commit()

@bot.callback_query_handler(func=lambda call: call.data == 'registration')
def handle_registration(callback_query):
    @bot.message_handler(func=lambda message: True)
    def get_text_messages(message):
        if message.text.lower() == 'REG':
            bot.send_message(message.chat.id, 'Привет! Введите свой адрес электронной почты.')

        elif re.match(r'\S+@\S+', message.text):
            email = re.findall(r'\S+@\S+', message.text)[0]
            bot.send_message(message.chat.id, 'Введите свое имя.')

            @bot.message_handler(func=lambda message: True)
            def get_name(message):
                name = message.text.strip()
                bot.send_message(message.chat.id, 'Введите свою фамилию.')

                @bot.message_handler(func=lambda message: True)
                def get_surname(message):
                    surname = message.text.strip()
                    bot.send_message(message.chat.id, 'Введите свой номер телефона.')

                    @bot.message_handler(func=lambda message: True)
                    def get_phone_number(message):
                        phone_number = message.text.strip()

                        user_id = message.from_user.id
                        user_name = name
                        user_surname = surname
                        username = message.from_user.username

                        db_table_val(user_id=user_id, user_name=user_name, user_surname=user_surname, username=username,
                                     email=email, phone_number=phone_number)

                        bot.send_message(message.chat.id, 'Данные сохранены успешно.')

                    bot.register_next_step_handler(message, get_phone_number)

                bot.register_next_step_handler(message, get_surname)

            bot.register_next_step_handler(message, get_name)

        else:
            bot.send_message(message.chat.id, 'Не правильный формат почты.')

    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('Отменить регистрацию', callback_data='menu')
    markup.add(back_button)
    bot.send_message(callback_query.from_user.id, "Введите свой адрес электронной почты.", reply_markup=markup)













bot.infinity_polling(none_stop = True)
