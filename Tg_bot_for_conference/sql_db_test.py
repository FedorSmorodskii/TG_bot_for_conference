"""
Задачи:

9) Исправить проблему с дублем сообщений от бота ПРОВЕРИТЬ С П8 + добавить такую же защиту на логин и пароль
10) При вводе неправильной эл почты в добавить соавтора и научника он перестает отвечать
13) настроить удаление фото и доков из папок
14) Исправить ошибку с перекидыванием нас в меню когда загружаем научную работу
15) Провеси тесты многопользовательской работы в главном меню
"""

import time
import threading
from multiprocessing import freeze_support
import os
import random
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# import sched
from threading import Thread
import base64
import codecs
import glob


from pytz import timezone
import telebot
from telebot import types
import pymysql

global password_from_db, Incorrect_login_or_password, Correct_login_or_password, scr, scr_2, d2, science_work_is_ok, scr_3, all_inf, number_page_invitation, user_name, new_file, all_inf, main_total_back_to_start, kol_inf


def main_start():
    token = "token"
    bot = telebot.TeleBot(token)

    def send_ya_mail(recipients_emails: list, msg_text: str):
        login = 'login'
        password = 'password'

        msg = MIMEText(f'{msg_text}', 'plain', 'utf-8')
        msg['Subject'] = Header('Уведомление от СНИИ2024', 'utf-8')
        msg['From'] = login
        msg['To'] = ', '.join(recipients_emails)

        s = smtplib.SMTP('host', 587, timeout=10)

        try:
            s.starttls()
            s.login(login, password)
            s.sendmail(msg['From'], recipients_emails, msg.as_string())
        except Exception as ex:
            print(ex)
        finally:
            s.quit()

    # Чат для пользователя
    def task1():
        @bot.message_handler(content_types=['text'])
        def text_handler(message):
            if message.text == '/start':
                global d2
                chat_id = message.chat.id
                user_name = message.from_user.username
                print(user_name)
                if str(user_name) == 'None':
                    print('change user_name')
                    user_name = message.from_user.first_name
                    print(user_name)
                user_id = message.from_user.id
                d = {'chat_id': f'{chat_id}'}
                print(d)
                while True:
                    try:
                        print(d2)
                        d4 = {f'{user_name}': d}
                        d4.items()
                        d2.update(d4)
                        print(d2)
                        break
                    except:
                        d2 = {f'{user_name}': d}
                        d2.items()
                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        print(d2[f'{user_name}']['chat_id'])
                        print(d2)
                        break
                v = {'id': f'{user_id}'}
                d2[f'{user_name}'].update(v)
                v = {'start_message_bool': 'False'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                d2[f'{user_name}'].update(v)
                start(message)
            elif message.text == '/error':
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                main_total_back_to_start = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                            'Что-то пошло не так!\nВозвращаю вас в раздел авторизации')
                time.sleep(2)
                start(message)
            else:
                def clear_chat(message):
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], user_is_not_found_co.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], time_1.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], send_is_ok.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], total_back_4.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], work_is_ok.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], local2.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], not_db.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            local6 = 0
                            while local6 != 30:
                                number_id = message.id
                                bot.delete_message(d2[f'{user_name}']['chat_id'], number_id)
                                number_id -= 1
                                local6 += 1
                            break
                        except:
                            break

                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                global not_db
                not_db = bot.send_message(d2[f'{user_name}']['chat_id'],
                                          'Неизвестная команда\nПереношу вас в меню авторизации')
                print(message.message_id)
                print(not_db.message_id)
                time.sleep(3)
                clear_chat(message)
                start(message)

        def start(message):
            global message_to_delete_to_main_menu, d2
            while True:
                try:
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['start_message_bool'],
                                               main_total_back_to_start.message_id)
                            break
                        except:
                            break
                    print(d2[f'{user_name}']['start_message_bool'])
                    if d2[f'{user_name}']['start_message_bool'] == 'False':
                        v = {'start_message_bool': 'True'}
                        d2[f'{user_name}'].update(v)
                        print('start_bot')

                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        s = len(d2[f'{user_name}'])
                        print(s)
                        # if s > 2:
                        #     print(d2)
                        #     (d2[f'{user_name}']).clear()
                        #     chat_id = message.chat.id
                        #     user_name = message.from_user.username
                        #     user_id = message.from_user.id
                        #     d = {'chat_id': f'{chat_id}'}
                        #     d2 = {f'{user_name}': d}
                        #     d2.items()
                        #     user_name = message.from_user.username

                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        start_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                         "Добрый день! Авторизируйтесь в системе для доступа к "
                                                         "возможностям этого бота\nВ случае проблем, обратитесь "
                                                         "в поддержку srdi.tsu@yandex.ru")

                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                        btn1 = types.KeyboardButton('Регистрация')
                        btn2 = types.KeyboardButton('Вход в аккаунт')
                        markup.row(btn1, btn2)

                        choice_message = bot.send_message(d2[f'{user_name}']['chat_id'], 'Выберите действие',
                                                          reply_markup=markup)

                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], not_db.message_id)
                                break
                            except:
                                break
                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], what_email.message_id)
                                break
                            except:
                                break
                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], total_back_message.message_id)
                                break
                            except:
                                break
                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                break
                            except:
                                break
                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], full_information.message_id)
                                break
                            except:
                                break
                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], refund.message_id)
                                break
                            except:
                                break

                        while True:
                            try:
                                if message_to_delete_to_main_menu == 'Incorrect_login_or_password':
                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                       Incorrect_login_or_password.message_id)
                                elif message_to_delete_to_main_menu == '/start':
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                elif message_to_delete_to_main_menu == 'Prohibited_character':
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], Prohibited_character.message_id)
                                elif message_to_delete_to_main_menu == '/back':
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], bake_to_start.message_id)
                                break
                            except:
                                break

                        bot.register_next_step_handler(message, choice, start_message, choice_message, bot)
                        break
                    elif d2[f'{user_name}']['start_message_bool'] == 'True':
                        break
                except:
                    print('Error 444')
                    break

        def main_menu_for_user(message):
            global message_to_delete_to_main_menu
            while True:
                try:
                    with connection.cursor() as cursor:
                        insert_querty_1_co = f"""SELECT * FROM login_and_password WHERE login='{login}' and password ='{password.text}'"""
                        cursor.execute(insert_querty_1_co)
                    while True:
                        try:
                            global unical_id_from_login_and_password_db
                            local_3 = cursor.fetchall()[0]
                            unical_id_from_login_and_password_db = local_3['unique_id']
                            break
                        except:
                            break
                    break
                except Exception as ex:
                    print(ex)
                    break

            menu_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

            btn1 = types.KeyboardButton('Загрузить научную работу')
            btn2 = types.KeyboardButton('Отправленные работы(просмотреть\редактировать)')
            btn3 = types.KeyboardButton('Выйти из аккаунта')
            btn4 = types.KeyboardButton('Входящие приглашения')

            menu_buttons.row(btn1, btn2)
            menu_buttons.row(btn3, btn4)
            user_name = message.from_user.username
            if str(user_name) == 'None':
                user_name = message.from_user.first_name
            choice_message = bot.send_message(d2[f'{user_name}']['chat_id'], 'Выберите действие',
                                              reply_markup=menu_buttons)

            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], user_is_not_found_co.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], time_1.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], send_is_ok.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], total_back_4.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], work_is_ok.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local2.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], you_have_not_works.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], total_back_155.message_id)
                    break
                except:
                    break

            if message_to_delete_to_main_menu == 'Correct_login_or_password':
                bot.delete_message(d2[f'{user_name}']['chat_id'], Correct_login_or_password.message_id)
                message_to_delete_to_main_menu = ''

            bot.register_next_step_handler(message, main_menu_check, choice_message)

        def main_menu_check(message, choice_message):
            global bake_to_start, message_to_delete_to_main_menu, upload
            user_name = message.from_user.username
            if str(user_name) == 'None':
                user_name = message.from_user.first_name
            while True:
                try:
                    bot.delete_message(d2[f'{user_name}']['chat_id'], choice_message.message_id)
                    break
                except:
                    break

            if message.text == 'Загрузить научную работу':
                def expert_opinion(message):
                    global expert_opinion_from_user
                    expert_opinion_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                              'Пришлите скан - копию экспертного заключения о возможности открытого опубликования материалов конференции в формате.pdf')
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            break
                        except:
                            break

                    def local_function(message, expert_opinion_message):
                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        bot.delete_message(d2[f'{user_name}']['chat_id'], expert_opinion_message.message_id)

                        def convert_to_Binary(filename):
                            with open(filename, 'rb') as file:
                                binarydata = file.read()
                                file.close()
                                return binarydata

                        while True:
                            try:
                                global expert_opinion_from_user
                                while True:
                                    try:
                                        file_name_for_last_letter = message.document.file_name[-1]
                                        v = {'file_name_for_last_letter': f'{file_name_for_last_letter}'}
                                        user_name = message.from_user.username
                                        if str(user_name) == 'None':
                                            user_name = message.from_user.first_name
                                        d2[f'{user_name}'].update(v)
                                        break
                                    except:
                                        break
                                last_letter = d2[f'{user_name}']['file_name_for_last_letter']
                                file_info = bot.get_file(message.document.file_id)
                                downloaded_file = bot.download_file(file_info.file_path)
                                random_number = random.randint(0, 10000)
                                if last_letter == 'f':  # pdf файл
                                    src = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/expert_opinions' + f'/Экспертное заключение {random_number}.pdf';
                                with open(src, 'wb') as new_file:
                                    new_file.write(downloaded_file)
                                expert_opinion_from_user = convert_to_Binary(f'{src}')
                                v = {'expert_opinion_from_user': f'{expert_opinion_from_user}'}
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name
                                d2[f'{user_name}'].update(v)
                                v = {'src': f'{src}'}
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name
                                d2[f'{user_name}'].update(v)
                                file_uploaded_successfully = bot.reply_to(message, "Файл успешно загружен")
                                time.sleep(2)
                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                new_file.close()
                                upload_a_scientific_work(message, file_uploaded_successfully)
                                break

                            except Exception as ex:
                                (f'Error 47 - {ex}')
                                global local2
                                local2 = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                          f'Что то пошло не так\nПереносим вас в главное меню')
                                time.sleep(3)
                                main_menu_for_user(message)
                                break

                    bot.register_next_step_handler(message, local_function, expert_opinion_message)

                def upload_a_scientific_work(message, file_uploaded_successfully):
                    global upload
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], file_uploaded_successfully.message_id)
                            break
                        except:
                            break

                    upload = bot.send_message(d2[f'{user_name}']['chat_id'],
                                              'Загрузите научную работу (перетащите файл pdf/docx в чат)')
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            break
                        except:
                            break
                    bot.register_next_step_handler(message, file_check)

                def work_name(message):
                    enter_work_name = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Введите название научной работы')
                    bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                    bot.register_next_step_handler(message, section_selection, enter_work_name)

                def section_selection(message, enter_work_name):
                    global the_name_of_the_scientific_work
                    the_name_of_the_scientific_work = message.text
                    v = {'the_name_of_the_scientific_work': f'{the_name_of_the_scientific_work}'}
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    d2[f'{user_name}'].update(v)

                    def section_selection_check_choice(message):
                        if message.text == 'Пленарная секция':
                            print('aaa')
                            section_of_the_work = "Пленарная секция"
                            v = {'section_of_the_work': f'{section_of_the_work}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], sect.message_id)
                            print('vvv')
                            expert_opinion(message)
                        elif message.text == 'Секция 1. Радиофизика и электроника':
                            section_of_the_work = "Секция 1. Радиофизика и электроника"
                            v = {'section_of_the_work': f'{section_of_the_work}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], sect.message_id)
                            expert_opinion(message)
                        elif message.text == 'Секция 2. Оптика, фотоника и оптоинформатика':
                            section_of_the_work = "Секция 2. Оптика, фотоника и оптоинформатика"
                            v = {'section_of_the_work': f'{section_of_the_work}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], sect.message_id)
                            expert_opinion(message)
                        elif message.text == 'Секция 3. Информационные технологии и телекоммуникационные системы':
                            section_of_the_work = "Секция 3. Информационные технологии и телекоммуникационные системы"
                            v = {'section_of_the_work': f'{section_of_the_work}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], sect.message_id)
                            expert_opinion(message)
                        elif message.text == 'Секция 4. Шаг в науку':
                            section_of_the_work = "Секция 4. Шаг в науку"
                            v = {'section_of_the_work': f'{section_of_the_work}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], sect.message_id)
                            expert_opinion(message)
                        elif message.text == 'Секция 5. Recent Developments in Radiophysics,  Optics, Photonics, Optoinformatics and  Information Technologies':
                            section_of_the_work = "Секция 5. Recent Developments in Radiophysics,  Optics, Photonics, Optoinformatics and  Information Technologies"
                            v = {'section_of_the_work': f'{section_of_the_work}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], sect.message_id)
                            expert_opinion(message)

                    sections = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                    btn1 = types.KeyboardButton('Пленарная секция')
                    btn2 = types.KeyboardButton('Секция 1. Радиофизика и электроника')
                    btn3 = types.KeyboardButton('Секция 2. Оптика, фотоника и оптоинформатика')
                    btn4 = types.KeyboardButton('Секция 3. Информационные технологии и телекоммуникационные системы')
                    btn5 = types.KeyboardButton('Секция 4. Шаг в науку')
                    btn6 = types.KeyboardButton(
                        'Секция 5. Recent Developments in Radiophysics,  Optics, Photonics, Optoinformatics and  Information Technologies')

                    sections.row(btn1)
                    sections.row(btn2)
                    sections.row(btn3)
                    sections.row(btn4)
                    sections.row(btn5)
                    sections.row(btn6)

                    global sect

                    sect = bot.send_message(d2[f'{user_name}']['chat_id'],
                                            'Выберите секцию, в которую подается доклад:\nПленарная секция\nСекция 1. Радиофизика и электроника\nСекция 2. Оптика, фотоника и оптоинформатика\nСекция 3. Информационные технологии и телекоммуникационные системы\nСекция 4. Шаг в науку\nСекция 5. Recent Developments in Radiophysics,  Optics, Photonics, Optoinformatics and  Information Technologies',
                                            reply_markup=sections)
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            break
                        except:
                            break
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], enter_work_name.message_id)
                            break
                        except:
                            break

                    bot.register_next_step_handler(message, section_selection_check_choice)

                work_name(message)

            elif message.text == 'Отправленные работы(просмотреть\редактировать)':
                def submitted_works2():
                    def submitted_works():
                        global science_work_is_ok, block

                        def submitted_works_check_choice(message, kol_inf):
                            global kol
                            if message.text == 'Предыдущая работа':
                                global change, block
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name
                                change = True

                                if kol > 0:
                                    kol -= 1
                                else:
                                    pass
                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                submitted_works2()
                            elif message.text == 'Следующая работа':
                                change = True
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name

                                if kol < len(kol_inf) - 1:
                                    kol += 1
                                else:
                                    pass
                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                submitted_works2()
                            elif message.text == 'Редактировать работу':
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name
                                def submitted_works_check_choic(message):
                                    if message.text == 'Добавить соавтора':
                                        def add_co_author_check(message):
                                            global user_is_not_found_co, email_from_user_co
                                            email_from_user_co = message.text
                                            user_name = message.from_user.username
                                            if str(user_name) == 'None':
                                                user_name = message.from_user.first_name

                                            with connection.cursor() as cursor:
                                                insert_querty_1_co = f"""SELECT * FROM login_and_password WHERE email='{email_from_user_co}'"""
                                                cursor.execute(insert_querty_1_co)

                                                def localdef(message):
                                                    global user_is_not_found_co

                                                    def localdef_choice_check4(message):
                                                        if message.text == 'Отправить приглашение':
                                                            while True:
                                                                try:
                                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                       message.message_id)
                                                                    break
                                                                except:
                                                                    break
                                                            global send_is_ok, email_from_user_co
                                                            while True:
                                                                try:
                                                                    with connection.cursor() as cursor_5:
                                                                        wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Соавтор'"""
                                                                        cursor_5.execute(wait_1_co)
                                                                        try:
                                                                            v_co = cursor_5.fetchall()[0]
                                                                            already_co = bot.send_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                'Вы уже отправили приглашение этому пользователю')
                                                                            bot.delete_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                user_is_not_found_co.message_id)
                                                                            time.sleep(3)
                                                                            bot.delete_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                already_co.message_id)
                                                                            submitted_works()
                                                                            break

                                                                        except:
                                                                            try:
                                                                                send_ya_mail(
                                                                                    recipients_emails=[
                                                                                        f'{email_from_user_co}'],
                                                                                    msg_text=f'Добрый день!\n{full_name} отправил вам приглашение стать соавтором его работы на конференции СНИИ 2024\nЧто бы подтвердить свое участие в проекте необходимо перейти по ссылке ниже и авторизироваться на сервисе\nСсылка: https://t.me/Test_Conf21_bot')
                                                                                with connection.cursor() as cursor_5:
                                                                                    print(email, unical_id_from_login_and_password_db, {all_inf['name_scientific_work']}, email_from_user_co, 'Соавтор')

                                                                                    wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                                                    value_co = (
                                                                                        email,
                                                                                        unical_id_from_login_and_password_db,
                                                                                        {all_inf[
                                                                                             'name_scientific_work']},
                                                                                        email_from_user_co,
                                                                                        'Соавтор')
                                                                                    cursor_5.execute(wait_co, value_co)
                                                                                    connection.commit()

                                                                                    send_is_ok = bot.send_message(
                                                                                        d2[f'{user_name}']['chat_id'],
                                                                                        'Приглашение отправленно на указанную электронную почту\nМы пришлем вам электронное письмо, когда пользователь зарегистрируется\nПереносим вас в главное меню')
                                                                                    time.sleep(7)
                                                                                    bot.delete_message(
                                                                                        d2[f'{user_name}']['chat_id'],
                                                                                        user_is_not_found_co.message_id)
                                                                                    main_menu_for_user(message)
                                                                                    break
                                                                            except:
                                                                                send_is_ok = bot.send_message(
                                                                                    d2[f'{user_name}']['chat_id'],
                                                                                    'Не удалось отправить сообщение по указанной электронной почте')
                                                                                bot.delete_message(
                                                                                    d2[f'{user_name}']['chat_id'],
                                                                                    user_is_not_found_co.message_id)
                                                                                time.sleep(4)
                                                                                submitted_works()
                                                                                break
                                                                except Exception as ex:
                                                                    send_is_ok = bot.send_message(
                                                                        d2[f'{user_name}']['chat_id'],
                                                                        'Не удалось выполнить действие\nОшибка 28\nОбратитесь в поддержку')
                                                                    print(f'Error 78 - {ex}')
                                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                       user_is_not_found_co.message_id)
                                                                    time.sleep(4)
                                                                    submitted_works()
                                                                    break
                                                        elif message.text == 'Вернуться в меню редактирования':
                                                            global time_1

                                                            time_1_co = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                         'Возвращаем вас раздел редактирования')
                                                            while True:
                                                                try:
                                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                       message.message_id)
                                                                    break
                                                                except:
                                                                    break
                                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                               user_is_not_found_co.message_id)
                                                            time.sleep(3)
                                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                               time_1_co.message_id)
                                                            submitted_works()

                                                    invitation_to_co_author = types.ReplyKeyboardMarkup(
                                                        resize_keyboard=True,
                                                        one_time_keyboard=True)

                                                    btn1 = types.KeyboardButton('Отправить приглашение')
                                                    btn2 = types.KeyboardButton('Вернуться в меню редактирования')

                                                    invitation_to_co_author.row(btn1)
                                                    invitation_to_co_author.row(btn2)

                                                    user_is_not_found_co = bot.send_message(
                                                        d2[f'{user_name}']['chat_id'],
                                                        text='Пользователь не '
                                                             'найден\nОтправить '
                                                             'приглашение на указанную '
                                                             'электронную почту?\nКогда '
                                                             'пользователь '
                                                             'зарегестрируется, '
                                                             'мы пришлем вам уведомление',
                                                        reply_markup=invitation_to_co_author)
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       add_co_author_message.message_id)
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       message.message_id)

                                                    bot.register_next_step_handler(message, localdef_choice_check4)

                                                while True:
                                                    try:
                                                        all_from_db = cursor.fetchall()[0]
                                                        with connection.cursor() as cursor_5:
                                                            wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Соавтор'"""
                                                            cursor_5.execute(wait_1_co)
                                                            try:
                                                                user_name = message.from_user.username
                                                                if str(user_name) == 'None':
                                                                    user_name = message.from_user.first_name
                                                                v_co = cursor_5.fetchall()[0]
                                                                already_co = bot.send_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    'Вы уже отправили приглашение этому пользователю')
                                                                time.sleep(3)
                                                                print('go to file check 0')
                                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                   already_co.message_id)
                                                                while True:
                                                                    try:
                                                                        user_name = message.from_user.username
                                                                        if str(user_name) == 'None':
                                                                            user_name = message.from_user.first_name
                                                                        bot.delete_message(
                                                                            d2[f'{user_name}']['chat_id'],
                                                                            add_co_author_message.message_id)
                                                                        break
                                                                    except:
                                                                        break
                                                                print('go tot file check')
                                                                while True:
                                                                    try:
                                                                        bot.delete_message(
                                                                            d2[f'{user_name}']['chat_id'],
                                                                            message.message_id)
                                                                        break
                                                                    except:
                                                                        break
                                                                submitted_works()
                                                                break
                                                            except:
                                                                if email_from_user_co == all_from_db['email']:
                                                                    global send_is_ok
                                                                    send_ya_mail(
                                                                        recipients_emails=[
                                                                            f'{email_from_user_co}'],
                                                                        msg_text=f'Добрый день!\n{full_name} отправил вам приглашение стать соавтором его работы на конференции СНИИ 2024\nЧто бы подтвердить свое участие в проекте необходимо перейти по ссылке ниже и авторизироваться на сервисе\nСсылка: https://t.me/Test_Conf21_bot')
                                                                    send_is_ok = bot.send_message(
                                                                        d2[f'{user_name}']['chat_id'],
                                                                        'Приглашение отправленно\nПосле подтверждения пользователем причастия к работе, мы отправим вам электронное письмо')
                                                                    with connection.cursor() as cursor_5:
                                                                        wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                                        value_co = (
                                                                            email,
                                                                            unical_id_from_login_and_password_db,
                                                                            {all_inf[
                                                                                 'name_scientific_work']},
                                                                            email_from_user_co,
                                                                            'Соавтор')
                                                                        cursor_5.execute(wait_co, value_co)
                                                                        connection.commit()
                                                                    while True:
                                                                        try:
                                                                            bot.delete_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                add_co_author_message.message_id)
                                                                            break
                                                                        except:
                                                                            break
                                                                    while True:
                                                                        try:
                                                                            bot.delete_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                message.message_id)
                                                                            break
                                                                        except:
                                                                            break
                                                                    time.sleep(5)
                                                                    submitted_works()

                                                                break
                                                    except IndexError:
                                                        localdef(message)
                                                        break

                                        add_co_author_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                 'После того как владелец данной электронной почты подтвердит свою причастность к этой работе, мы пришлем вам уведомление\nЕсли ваш соавтор не зарегестрирован в системе, то мы отправим ему ссылку приглашение на электронную почту\nВведите электронную почту вашего соавтора:',
                                                                                 reply_markup=None)
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                break
                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                           science_work_is_ok_2.message_id)
                                        bot.register_next_step_handler(message, add_co_author_check)

                                    elif message.text == 'Добавить научного руководителя':
                                        def add_supervisor_2_check(message):
                                            global user_is_not_found_co, email_from_user_co
                                            email_from_user_co = message.text

                                            with connection.cursor() as cursor:
                                                insert_querty_1_co = f"""SELECT * FROM login_and_password WHERE email='{email_from_user_co}'"""
                                                cursor.execute(insert_querty_1_co)

                                                def localdef(message):
                                                    global user_is_not_found_co

                                                    def localdef_choice_check3(message):
                                                        if message.text == 'Отправить приглашение':
                                                            global send_is_ok, email_from_user_co
                                                            while True:
                                                                try:
                                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                       message.message_id)
                                                                    break
                                                                except:
                                                                    break
                                                            while True:
                                                                try:
                                                                    with connection.cursor() as cursor_5:
                                                                        wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Научный руководитель'"""
                                                                        cursor_5.execute(wait_1_co)
                                                                        try:
                                                                            v_co = cursor_5.fetchall()[0]
                                                                            already_co = bot.send_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                'Вы уже отправили приглашение этому пользователю')
                                                                            bot.delete_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                user_is_not_found_co.message_id)
                                                                            time.sleep(3)
                                                                            bot.delete_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                already_co.message_id)
                                                                            submitted_works()
                                                                            break

                                                                        except:
                                                                            try:

                                                                                send_ya_mail(
                                                                                    recipients_emails=[
                                                                                        f'{email_from_user_co}'],
                                                                                    msg_text=f'Добрый день!\n{full_name} отправил вам приглашение стать его научным руководителем на конференции СНИИ 2024\nЧто бы подтвердить свое участие в проекте необходимо перейти по ссылке ниже и авторизироваться на сервисе\nСсылка: https://t.me/Test_Conf21_bot')
                                                                                with connection.cursor() as cursor_5:
                                                                                    wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                                                    value_co = (
                                                                                        email,
                                                                                        unical_id_from_login_and_password_db,
                                                                                        {all_inf[
                                                                                             'name_scientific_work']},
                                                                                        email_from_user_co,
                                                                                        'Научный руководитель')
                                                                                    cursor_5.execute(wait_co,
                                                                                                     value_co)
                                                                                    connection.commit()

                                                                                    send_is_ok = bot.send_message(
                                                                                        d2[f'{user_name}'][
                                                                                            'chat_id'],
                                                                                        'Приглашение отправленно на указанную электронную почту\nМы пришлем вам электронное письмо, когда пользователь зарегистрируется\nПереносим вас в главное меню')
                                                                                    time.sleep(7)
                                                                                    bot.delete_message(
                                                                                        d2[f'{user_name}'][
                                                                                            'chat_id'],
                                                                                        user_is_not_found_co.message_id)
                                                                                    main_menu_for_user(message)
                                                                                    break
                                                                            except:
                                                                                send_is_ok = bot.send_message(
                                                                                    d2[f'{user_name}']['chat_id'],
                                                                                    'Не удалось отправить сообщение по указанной электронной почте')
                                                                                bot.delete_message(
                                                                                    d2[f'{user_name}']['chat_id'],
                                                                                    user_is_not_found_co.message_id)
                                                                                time.sleep(4)
                                                                                submitted_works()
                                                                                break
                                                                except:
                                                                    send_is_ok = bot.send_message(
                                                                        d2[f'{user_name}']['chat_id'],
                                                                        'Не удалось выполнить действие\nОшибка 28\nОбратитесь в поддержку')
                                                                    bot.delete_message(
                                                                        d2[f'{user_name}']['chat_id'],
                                                                        user_is_not_found_co.message_id)
                                                                    time.sleep(4)
                                                                    submitted_works()
                                                                    break
                                                        elif message.text == 'Вернуться в меню редактирования':
                                                            global time_1
                                                            time_1_co = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                         'Возвращаем вас раздел редактирования')
                                                            while True:
                                                                try:
                                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                       message.message_id)
                                                                    break
                                                                except:
                                                                    break
                                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                               user_is_not_found_co.message_id)
                                                            time.sleep(3)
                                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                               time_1_co.message_id)
                                                            submitted_works()

                                                    invitation_to_co_author = types.ReplyKeyboardMarkup(
                                                        resize_keyboard=True,
                                                        one_time_keyboard=True)

                                                    btn1 = types.KeyboardButton('Отправить приглашение')
                                                    btn2 = types.KeyboardButton('Вернуться в меню редактирования')

                                                    invitation_to_co_author.row(btn1)
                                                    invitation_to_co_author.row(btn2)

                                                    user_is_not_found_co = bot.send_message(
                                                        d2[f'{user_name}']['chat_id'],
                                                        text='Пользователь не '
                                                             'найден\nОтправить '
                                                             'приглашение на указанную '
                                                             'электронную почту?\nКогда '
                                                             'пользователь '
                                                             'зарегестрируется, '
                                                             'мы пришлем вам уведомление',
                                                        reply_markup=invitation_to_co_author)
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       add_co_author_message.message_id)
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       message.message_id)

                                                    bot.register_next_step_handler(message, localdef_choice_check3)

                                                while True:
                                                    try:
                                                        all_from_db = cursor.fetchall()[0]
                                                        with connection.cursor() as cursor_5:
                                                            wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Научный руководитель'"""
                                                            cursor_5.execute(wait_1_co)
                                                            try:
                                                                v_co = cursor_5.fetchall()[0]
                                                                already_co = bot.send_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    'Вы уже отправили приглашение этому пользователю')
                                                                time.sleep(3)
                                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                   already_co.message_id)
                                                                while True:
                                                                    try:
                                                                        bot.delete_message(
                                                                            d2[f'{user_name}']['chat_id'],
                                                                            add_co_author_message.message_id)
                                                                        break
                                                                    except:
                                                                        break
                                                                while True:
                                                                    try:
                                                                        bot.delete_message(
                                                                            d2[f'{user_name}']['chat_id'],
                                                                            message.message_id)
                                                                        break
                                                                    except:
                                                                        break
                                                                submitted_works()
                                                                break
                                                            except:
                                                                if email_from_user_co == all_from_db['email']:
                                                                    global send_is_ok
                                                                    send_is_ok = bot.send_message(
                                                                        d2[f'{user_name}']['chat_id'],
                                                                        'Приглашение отправленно\nПосле подтверждения пользователем причастия к работе, мы отправим вам электронное письмо')
                                                                    with connection.cursor() as cursor_5:
                                                                        wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                                        value_co = (
                                                                            email,
                                                                            unical_id_from_login_and_password_db,
                                                                            {all_inf[
                                                                                 'name_scientific_work']},
                                                                            email_from_user_co,
                                                                            'Научный руководитель')
                                                                        cursor_5.execute(wait_co, value_co)
                                                                        connection.commit()
                                                                    while True:
                                                                        try:
                                                                            bot.delete_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                add_co_author_message.message_id)
                                                                            break
                                                                        except:
                                                                            break
                                                                    while True:
                                                                        try:
                                                                            bot.delete_message(
                                                                                d2[f'{user_name}']['chat_id'],
                                                                                message.message_id)
                                                                            break
                                                                        except:
                                                                            break
                                                                    time.sleep(5)
                                                                    submitted_works()

                                                                break
                                                    except IndexError:
                                                        localdef(message)
                                                        break

                                        add_co_author_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                 'После того как владелец данной электронной почты подтвердит свою причастность к этой работе, мы пришлем вам уведомление\nЕсли ваш научный руководитель не зарегестрирован в системе, то мы отправим ему ссылку приглашение на электронную почту\nВведите электронную почту вашего научного руководителя:',
                                                                                 reply_markup=None)
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                break
                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                           science_work_is_ok_2.message_id)
                                        bot.register_next_step_handler(message, add_supervisor_2_check)

                                    elif message.text == 'Удалить работу':
                                        global local2
                                        try:
                                            local2 = bot.send_message(d2[f'{user_name}']['chat_id'], 'Удалить работу',
                                                                      reply_markup=None)
                                            while True:
                                                try:
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       message.message_id)
                                                    break
                                                except:
                                                    break
                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                               science_work_is_ok_2.message_id)
                                            with connection.cursor() as cursor_1:
                                                insert_querty = f"""DELETE FROM scientific_work WHERE name_scientific_work = '{all_inf['name_scientific_work']}' and unique_id = '{all_inf['unique_id']}'"""
                                                cursor_1.execute(insert_querty)
                                                connection.commit()
                                        except:
                                            bot.send_message(d2[f'{user_name}']['chat_id'],
                                                             'Не удалось удалить работу\nОшибка 19\nОбратитесь в поддержку')
                                            time.sleep(3)
                                        submitted_works()

                                    elif message.text == 'Вернуться назад':
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                   science_work_is_ok_2.message_id)
                                                break
                                            except:
                                                break
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                break

                                        local2 = bot.send_message(d2[f'{user_name}']['chat_id'], 'Возвращаем вас назад',
                                                                  reply_markup=None)

                                        time.sleep(2)
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], local2.message_id)
                                                break
                                            except:
                                                break
                                        submitted_works()

                                menu_buttons_3 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                                btn1 = types.KeyboardButton('Добавить соавтора')
                                btn2 = types.KeyboardButton('Добавить научного руководителя')
                                btn3 = types.KeyboardButton('Удалить работу')
                                btn4 = types.KeyboardButton('Вернуться назад')

                                menu_buttons_3.row(btn1)
                                menu_buttons_3.row(btn2)
                                menu_buttons_3.row(btn3)
                                menu_buttons_3.row(btn4)

                                with connection.cursor() as cursor_1:
                                    wait_1 = f"""SELECT * FROM scientific_work WHERE unique_id='{unique_id_from_db['unique_id']}' """
                                    cursor_1.execute(wait_1)
                                    while True:
                                        try:
                                            def convert(work):
                                                with open(
                                                        "C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works" + f"/{id_scientific_work}",
                                                        "wb") as f:
                                                    f.write(codecs.decode(work, "base64"))

                                            kol_inf = cursor_1.fetchall()

                                            all_inf = kol_inf[kol]

                                            id_scientific_work = all_inf['id_scientific_work']
                                            work = all_inf['work']
                                            convert(work)
                                            break
                                        except Exception as ex:
                                            print(ex)
                                            break

                                print('send1')

                                science_work_is_ok_2 = bot.send_document(d2[f'{user_name}']['chat_id'], open(f'{d2[f'{user_name}']['work_doc']}', 'rb'),
                                                                         caption=f"Научная работа {kol + 1}/{len(kol_inf)}\nФИО: {full_name}\nУниверситет: {university}\nEmail: {email}\nНазвание работы: {all_inf['name_scientific_work']}\nНаучный руководитель: {all_inf['supervisor']}\nСоавторы: {all_inf['co_author']}\nДата публикации: {all_inf['date_of_publication']}",
                                                                         reply_markup=menu_buttons_3)
                                while True:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                        break
                                    except:
                                        break
                                while True:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], science_work_is_ok.message_id)
                                        break
                                    except:
                                        try:
                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                               science_work_is_ok_2.message_id)
                                        except:
                                            break
                                bot.register_next_step_handler(message, submitted_works_check_choic)
                            elif message.text == 'Вернуться в главное меню':
                                global local2
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name
                                local2 = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                          'Возвращаем вас в главное меню', reply_markup=None)
                                while True:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], science_work_is_ok.message_id)
                                        break
                                    except:
                                        break
                                time.sleep(3)
                                main_menu_for_user(message)

                        menu_buttons_2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                        btn1 = types.KeyboardButton('Предыдущая работа')
                        btn2 = types.KeyboardButton('Следующая работа')
                        btn3 = types.KeyboardButton('Редактировать работу')
                        btn4 = types.KeyboardButton('Вернуться в главное меню')

                        menu_buttons_2.row(btn1, btn2)
                        menu_buttons_2.row(btn4, btn3)

                        with connection.cursor() as cursor:
                            wait_2 = f"""SELECT unique_id, full_name, university_full, email FROM login_and_password WHERE login='{login}' and password='{password.text}'"""
                            cursor.execute(wait_2)
                            while True:
                                try:
                                    o = cursor.fetchall()[0]
                                    unique_id_from_db = o
                                    break

                                except:
                                    user_name = message.from_user.username
                                    if str(user_name) == 'None':
                                        user_name = message.from_user.first_name
                                    bot.send_message(d2[f'{user_name}']['chat_id'],
                                                     'Ошибка №114\nОбратитесь в поддержку')
                                    break



                        with connection.cursor() as cursor_1:
                            wait_1 = f"""SELECT * FROM scientific_work WHERE unique_id='{unique_id_from_db['unique_id']}'"""
                            cursor_1.execute(wait_1)
                            while True:
                                try:
                                    kol_inf = cursor_1.fetchall()

                                    all_inf = kol_inf[kol]
                                    full_name = all_inf['full_name']
                                    university = all_inf['university']
                                    email = all_inf['email']

                                    break
                                except:
                                    user_name = message.from_user.username
                                    if str(user_name) == 'None':
                                        user_name = message.from_user.first_name
                                    global you_have_not_works
                                    you_have_not_works = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                          'У вас нет загруженных работ\nВозвращаем вас в главное меню')
                                    while True:
                                        try:
                                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                            break
                                        except:
                                            break
                                    while True:
                                        try:
                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                               message.message_id)
                                            break
                                        except:
                                            break
                                    while True:
                                        try:
                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                               local2.message_id)
                                            break
                                        except:
                                            break
                                    time.sleep(3)
                                    main_menu_for_user(message)
                                    break

                        def binary_to_file(binarydata, filename):
                            filename = filename
                            with open(filename, 'wb') as file:
                                file.write(binarydata)

                        name = all_inf['name_scientific_work']
                        # while True:
                        #     global scr
                        #     try:
                        #         print('send0')
                        #         if name[-1] == 'f':
                        #             scr = binary_to_file(all_inf['work'],
                        #                                  f'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works' + f'/{all_inf["name_scientific_work"]}.pdf')
                        #             scr = f'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works' + f'/{all_inf["name_scientific_work"]}.pdf'
                        #             break
                        #         else:
                        #             scr = binary_to_file(all_inf['work'],
                        #                                  f'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works' + f'/{all_inf["name_scientific_work"]}.pdf')
                        #             scr = f'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works' + f'/{all_inf["name_scientific_work"]}.pdf'
                        #             break
                        #     except:
                        #         break
                        while True:
                            try:
                                global src_2
                                while True:
                                    try:
                                        file_name_for_last_letter = message.document.file_name[-1]
                                        v = {'file_name_for_last_letter': f'{file_name_for_last_letter}'}
                                        user_name = message.from_user.username
                                        if str(user_name) == 'None':
                                            user_name = message.from_user.first_name
                                        d2[f'{user_name}'].update(v)
                                        break
                                    except:
                                        break
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name
                                last_letter = d2[f'{user_name}']['file_name_for_last_letter']
                                file_info = bot.get_file(message.document.file_id)
                                downloaded_file = bot.download_file(file_info.file_path)
                                random_number = random.randint(0, 10000)
                                if last_letter == 'f':  # pdf файл
                                    src = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works' + f'/Научная работа {random_number}.pdf';
                                    src_2 = src
                                elif last_letter == 'x':  # docx файл
                                    src = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works' + f'/Научная работа {random_number}.docx';
                                    src_2 = src
                                v = {'src': f'{src}'}
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name
                                d2[f'{user_name}'].update(v)
                                with open(src, 'wb') as new_file:
                                    new_file.write(downloaded_file)
                                file_uploaded_successfully = bot.reply_to(message, "Файл успешно загружен")
                                time.sleep(2)
                                user_name = message.from_user.username
                                if str(user_name) == 'None':
                                    user_name = message.from_user.first_name
                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                bot.delete_message(d2[f'{user_name}']['chat_id'], upload.message_id)

                                break
                            except Exception as e:
                                print(f'Error 49 - {e}')
                                while True:
                                    try:
                                        src = src_2
                                        break
                                    except:
                                        break
                                while True:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                        break
                                    except:
                                        break

                                break
                        print('0.5')
                        print('0.6')
                        with connection.cursor() as cursor_1:
                            wait_1 = f"""SELECT * FROM scientific_work WHERE unique_id='{unique_id_from_db['unique_id']}' """
                            cursor_1.execute(wait_1)
                            while True:
                                try:
                                    def convert(work):
                                        with open(
                                                "C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works" + f"/{id_scientific_work}",
                                                "wb") as f:
                                            f.write(codecs.decode(work, "base64"))

                                    kol_inf = cursor_1.fetchmany(size=10)
                                    print(len(kol_inf))
                                    all_inf = kol_inf[kol]
                                    id_scientific_work = all_inf['id_scientific_work']
                                    work = all_inf['work']
                                    convert(work)
                                    break
                                except Exception as ex:
                                    print(ex)
                                    break
                        scr_3 = "C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works" + f"/{id_scientific_work}"
                        v = {'work_doc': f'{scr_3}'}
                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        d2[f'{user_name}'].update(v)
                        print(d2)
                        print('update work_doc')
                        while True:
                            try:
                                if block == False:

                                    if change == False:
                                        print('send2')
                                        print(d2[f'{user_name}']['work_doc'])
                                        science_work_is_ok = bot.send_document(d2[f'{user_name}']['chat_id'], open(f'{d2[f'{user_name}']['work_doc']}', 'rb'),
                                                                               caption=f"Научная работа {kol + 1}/{len(kol_inf)}\nФИО: {full_name}\nУниверситет: {university}\nEmail: {email}\nНазвание работы: {all_inf['name_scientific_work']}\nНаучный руководитель: {all_inf['supervisor']}\nСоавторы: {all_inf['co_author']}\nДата публикации: {all_inf['date_of_publication']}",
                                                                               reply_markup=menu_buttons_2)
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                while True:
                                                    try:
                                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                           send_is_ok.message_id)
                                                        break
                                                    except:
                                                        break
                                                while True:
                                                    try:
                                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                           local2.message_id)
                                                        break
                                                    except:
                                                        break
                                                break
                                    else:

                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                   science_work_is_ok.message_id)
                                                break
                                            except:
                                                break
                                        print('send3')
                                        science_work_is_ok = bot.send_document(d2[f'{user_name}']['chat_id'],
                                                                               open(f'{d2[f'{user_name}']['work_doc']}', 'rb'),
                                                                               caption=f"Научная работа {kol + 1}/{len(kol_inf)}\nФИО: {full_name}\nУниверситет: {university}\nEmail: {email}\nНазвание работы: {all_inf['name_scientific_work']}\nНаучный руководитель: {all_inf['supervisor']}\nСоавторы: {all_inf['co_author']}\nДата публикации: {all_inf['date_of_publication']}",
                                                                               reply_markup=menu_buttons_2)
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], local2.message_id)
                                                break
                                            except:
                                                break
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], send_is_ok.message_id)
                                                break
                                            except:
                                                break
                                else:
                                    global space
                                    if space == '':
                                        space = ' '
                                    elif space == ' ':
                                        space = ''
                                    bot.edit_message_caption(chat_id=science_work_is_ok.chat.id,
                                                             message_id=science_work_is_ok.message_id,
                                                             caption=f"Научная работа {kol + 1}/{len(kol_inf)} {space}\nФИО: {full_name}\nУниверситет: {university}\nEmail: {email}\nНазвание работы: {all_inf['name_scientific_work']}\nНаучный руководитель: {all_inf['supervisor']}\nСоавторы: {all_inf['co_author']}\nДата публикации: {all_inf['date_of_publication']}",
                                                             reply_markup=menu_buttons_2)
                                    while True:
                                        try:
                                            bot.delete_message(d2[f'{user_name}']['chat_id'], local2.message_id)
                                            break
                                        except:
                                            break
                                    while True:
                                        try:
                                            bot.delete_message(d2[f'{user_name}']['chat_id'], send_is_ok.message_id)
                                            break
                                        except:
                                            break
                                    block = False

                                while True:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                        break
                                    except:
                                        break
                                break
                            except Exception as ex:
                                print(f'Error 009 - {ex}')
                                while True:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                        break
                                    except:
                                        break
                                break

                        bot.register_next_step_handler(message, submitted_works_check_choice, kol_inf)

                    submitted_works()

                submitted_works2()

            elif message.text == 'Выйти из аккаунта':
                bake_to_start = bot.send_message(d2[f'{user_name}']['chat_id'], 'Переносим вас в меню авторизации',
                                                 reply_markup=None)
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                time.sleep(3)
                message_to_delete_to_main_menu = '/back'
                start(message)

            elif message.text == 'Входящие приглашения':
                global message_loc
                message_loc = message
                message = message
                print(f'login - {login}')
                print(f'password - {password.text}')
                global all_info_about_user_profile
                with connection.cursor() as cursorr:  # проверка всех данных пользователя
                    insert_querty_1_cor = f"""SELECT * FROM login_and_password WHERE login='{login}' and password ='{password.text}'"""
                    cursorr.execute(insert_querty_1_cor)
                all_info_about_user_profile = cursorr.fetchall()[0]
                print(all_info_about_user_profile)
                email = all_info_about_user_profile['email']

                print(f'email - {email}')

                def availability(message):
                    while True:
                        try:
                            with connection.cursor() as cursor_7:  # проверка есть ли у пользователя приглашения
                                wait_7_co = f"SELECT * FROM waiting_for_registration WHERE email_for_registration='{email}'"
                                cursor_7.execute(wait_7_co)

                            all_all_info = cursor_7.fetchall()
                            print(f'all_all_info - {all_all_info}')
                            print(f'number_page_invitation - {number_page_invitation}')
                            all_info_about = all_all_info[number_page_invitation]
                            print(f'all_info_about - {all_info_about}')

                            def incoming_invitations(message, all_info_about, all_info_about_user_profile):
                                while True:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], inv_is_ok.message_id)
                                        break
                                    except:
                                        break
                                with connection.cursor() as cursor_7:
                                    wait_7_co = f"SELECT * FROM waiting_for_registration WHERE email_for_registration='{email}'"
                                    cursor_7.execute(wait_7_co)

                                all_all_info = cursor_7.fetchall()
                                print(f'all_all_info - {all_all_info}')
                                print(f'number_page_invitation - {number_page_invitation}')
                                all_info_about = all_all_info[number_page_invitation]
                                print(f'all_info_about - {all_info_about}')

                                def incoming_invitations_choice_check(message):
                                    if message.text == 'Прошлое приглашение':
                                        global number_page_invitation
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                break
                                        if number_page_invitation + 1 > 1:
                                            number_page_invitation -= 1
                                            while True:
                                                try:
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       invitation_text.message_id)
                                                    break
                                                except:
                                                    break
                                            incoming_invitations(message, all_info_about, all_info_about_user_profile)
                                    elif message.text == 'Следующее приглашение':
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                break
                                        if number_page_invitation + 1 < len(all_all_info):
                                            number_page_invitation += 1
                                            while True:
                                                try:
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       invitation_text.message_id)
                                                    break
                                                except:
                                                    break
                                            incoming_invitations(message, all_info_about, all_info_about_user_profile)
                                    elif message.text == 'Принять приглашение':
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                break
                                        while True:
                                            try:
                                                with connection.cursor() as cursor:
                                                    wait_7_co = f"SELECT * FROM login_and_password WHERE email='{all_info_about['email_for_registration']}'"
                                                    cursor.execute(wait_7_co)

                                                all_from_log_and_pass = cursor.fetchall()[0]
                                                break
                                            except:
                                                break

                                        while True:
                                            try:
                                                global inf_co_author
                                                with connection.cursor() as cursor_1:
                                                    wait_7_co = f"SELECT * FROM scientific_work WHERE email='{all_info_about['email_waiting_users']}'"
                                                    cursor_1.execute(wait_7_co)

                                                    all_from_log_and_pass = cursor_1.fetchall()[0]
                                                    inf_supervisor = all_from_log_and_pass['supervisor']
                                                    inf_co_author = all_from_log_and_pass['co_author']
                                                break
                                            except Exception as ex:
                                                print(f'Error r6 - {ex}')
                                                break
                                        global inv_is_ok
                                        if all_info_about['expected_user_status'] == 'Научный руководитель':
                                            if inf_supervisor != None:
                                                sup_ent = f'{inf_supervisor}\n{all_from_log_and_pass['full_name']}'
                                            else:
                                                sup_ent = f'{all_from_log_and_pass['full_name']}'
                                            with connection.cursor() as cursor_1:
                                                wait_1 = f"UPDATE scientific_work SET supervisor = '{sup_ent}' WHERE unique_id = '{all_info_about['id_waiting_users']}' and name_scientific_work = '{all_info_about['name_scientific_work']}'"
                                                cursor_1.execute(wait_1)
                                                connection.commit()
                                            inv_is_ok = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                         'Приглашение успешно принято')
                                            send_ya_mail(recipients_emails=[f'{all_info_about['email_waiting_users']}'],
                                                         msg_text=f'Добрый день!\n{all_from_log_and_pass['full_name']} зарегестрировался на сервере и подтвердил свое участие в научной работе\nСсылка: https://t.me/Test_Conf21_bot')

                                            with connection.cursor() as cursor_7:
                                                invitation_no_ = f"""DELETE FROM waiting_for_registration WHERE id_waiting_users = '{all_info_about['id_waiting_users']}' and name_scientific_work = '{all_info_about['name_scientific_work']}' """
                                                cursor_7.execute(invitation_no_)
                                                connection.commit()

                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                               invitation_text.message_id)
                                            time.sleep(2)
                                            availability(message)
                                        elif all_info_about['expected_user_status'] == 'Соавтор':
                                            if inf_co_author != None:
                                                co_ent = f'{inf_co_author}\n{all_from_log_and_pass['full_name']}'
                                            else:
                                                co_ent = f'{all_from_log_and_pass['full_name']}'
                                            with connection.cursor() as cursor_1:
                                                wait_1 = f"UPDATE scientific_work SET co_author = '{co_ent}' WHERE unique_id = '{all_info_about['id_waiting_users']}' and name_scientific_work = '{all_info_about['name_scientific_work']}'"
                                                cursor_1.execute(wait_1)
                                                connection.commit()
                                            inv_is_ok = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                         'Приглашение успешно принято')

                                            send_ya_mail(recipients_emails=[f'{all_info_about['email_waiting_users']}'],
                                                         msg_text=f'Добрый день!\n{all_from_log_and_pass['full_name']} зарегестрировался на сервере и подтвердил свое участие в научной работе\nСсылка: https://t.me/Test_Conf21_bot')
                                            print(
                                                f'all_info_about_user_profile[unique_id] - {all_info_about_user_profile['unique_id']}')
                                            print(
                                                f'all_info_about[name_scientific_work] - {all_info_about["name_scientific_work"]}')
                                            with connection.cursor() as cursor_77:
                                                invitation_no_1 = f"""DELETE FROM waiting_for_registration WHERE id_waiting_users = '{all_info_about['id_waiting_users']}' and name_scientific_work = '{all_info_about['name_scientific_work']}' """
                                                cursor_77.execute(invitation_no_1)
                                                connection.commit()

                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                               invitation_text.message_id)
                                            time.sleep(2)
                                            availability(message)
                                    elif message.text == 'Отклонить приглашение':
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                break
                                        while True:
                                            try:
                                                print(all_info_about_user_profile['unique_id'])
                                                print(all_info_about['name_scientific_work'])
                                                with connection.cursor() as cursor_7:
                                                    invitation_no = f"""DELETE FROM waiting_for_registration WHERE id_waiting_users = '{all_info_about['id_waiting_users']}' and name_scientific_work = '{all_info_about['name_scientific_work']}' """
                                                    cursor_7.execute(invitation_no)
                                                    connection.commit()
                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                   invitation_text.message_id)
                                                incoming_invitations(message, all_info_about,
                                                                     all_info_about_user_profile)
                                                break
                                            except Exception as ex:
                                                print(f'Error t67 - {ex}')
                                                break
                                    elif message.text == 'Вернуться в главное меню':
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                break
                                            except:
                                                break
                                        global local2
                                        local2 = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                  'Возвращаем вас в главное меню')
                                        time.sleep(1)
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], invitation_text.message_id)
                                        while True:
                                            try:
                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                   message_loc.message_id)
                                                break
                                            except:
                                                break
                                        time.sleep(2)
                                        main_menu_for_user(message)

                                all_info_about_button = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                                                  one_time_keyboard=True)

                                btn1 = types.KeyboardButton('Прошлое приглашение')
                                btn2 = types.KeyboardButton('Следующее приглашение')
                                btn3 = types.KeyboardButton('Принять приглашение')
                                btn4 = types.KeyboardButton('Отклонить приглашение')
                                btn5 = types.KeyboardButton('Вернуться в главное меню')

                                all_info_about_button.row(btn1, btn2)
                                all_info_about_button.row(btn3, btn4)
                                all_info_about_button.row(btn5)

                                global invitation_text
                                invitation_text = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                   f'Приглашение {number_page_invitation + 1}/{len(all_all_info)}\nОт кого: {all_info_about['email_waiting_users']}\nНазвание научной работы: {all_info_about['name_scientific_work']}\nВы приглашены в роли: {all_info_about['expected_user_status']}',
                                                                   reply_markup=all_info_about_button)
                                while True:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], inv_is_ok.message_id)
                                        break
                                    except:
                                        break

                                bot.register_next_step_handler(message, incoming_invitations_choice_check)

                            incoming_invitations(message, all_info_about, all_info_about_user_profile)
                            break
                        except Exception as ex:
                            print(f'Error y66 - {ex}')
                            global total_back_155
                            total_back_155 = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                              'У вас нет приглашений\nВозвращаем вас в главное меню')
                            time.sleep(3)
                            main_menu_for_user(message)
                            break

                availability(message)

        def file_check(message):
            while True:
                try:
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    print('file check')
                    global scientific_work_report

                    def binary(src):
                        with open(
                                f'{src}',
                                'rb') as f:
                            blob = base64.b64encode(f.read())
                            return blob

                    while True:
                        try:
                            while True:
                                try:
                                    file_name_for_last_letter = message.document.file_name[-1]
                                    v = {'file_name_for_last_letter': f'{file_name_for_last_letter}'}
                                    user_name = message.from_user.username
                                    if str(user_name) == 'None':
                                        user_name = message.from_user.first_name
                                    d2[f'{user_name}'].update(v)
                                    break
                                except:
                                    break
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            last_letter = d2[f'{user_name}']['file_name_for_last_letter']
                            file_info = bot.get_file(message.document.file_id)
                            downloaded_file = bot.download_file(file_info.file_path)
                            random_number = random.randint(0, 10000)
                            if last_letter == 'f':  # pdf файл
                                src = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works' + f'/Научная работа {random_number}.pdf';
                                src_2 = src
                            elif last_letter == 'x':  # docx файл
                                src = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works' + f'/Научная работа {random_number}.docx';
                                src_2 = src
                            v = {'src': f'{src}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)
                            with open(src, 'wb') as new_file:
                                new_file.write(downloaded_file)

                            # with connection.cursor() as cursor_1:
                            #     insert_querty = f"""INSERT INTO scientific_work(unique_id, work) VALUES (%s, %s)"""
                            #     value = ('111', binary(src))
                            #     cursor_1.execute(insert_querty, value)
                            #     connection.commit()




                            file_uploaded_successfully = bot.reply_to(message, "Файл успешно загружен")
                            time.sleep(2)
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], upload.message_id)

                            break
                        except Exception as e:
                            print(f'Error 49 - {e}')
                            while True:
                                try:
                                    src = src_2
                                    break
                                except:
                                    break
                            while True:
                                try:
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                    break
                                except:
                                    break

                            break
                    print('file check after error')
                    work_for_exemple = binary(f'{src}')
                    print('file check 5')
                    v = {'work_for_exemple': f'{work_for_exemple}'}
                    print('file check 6')
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    print('file check 6.5')
                    d2[f'{user_name}'].update(v)
                    print('file check 7')
                    with (connection.cursor() as cursor_1):
                        create_table_query = "CREATE TABLE IF NOT EXISTS scientific_work(id int AUTO_INCREMENT," \
                                             " unique_id varchar(7)," \
                                             " full_name varchar(50)," \
                                             " university varchar(50)," \
                                             " email varchar(50)," \
                                             " name_scientific_work varchar(300)," \
                                             " id_scientific_work varchar(50)," \
                                             " supervisor varchar(50)," \
                                             " co_author varchar(50)," \
                                             " date_of_publication varchar(50)," \
                                             " work LONGBLOB," \
                                             " expert_opinions LONGBLOB," \
                                             " section_of_the_work varchar(200)," \
                                             " PRIMARY KEY (id));"
                        cursor_1.execute(create_table_query)

                    with connection.cursor() as cursor:
                        wait_2 = f"""SELECT unique_id, full_name, university_full, email FROM login_and_password WHERE login='{login}' and password='{password.text}'"""
                        cursor.execute(wait_2)
                        while True:
                            try:
                                o = cursor.fetchall()[0]
                                unique_id_from_db = o
                                break
                            except:
                                bot.send_message(d2[f'{user_name}']['chat_id'], 'Ошибка №114\nОбратитесь в поддержку')
                                break

                    with connection.cursor() as cursor_1:
                        wait_1 = f"""SELECT * FROM scientific_work WHERE unique_id='{unique_id_from_db['unique_id']}'"""
                        cursor_1.execute(wait_1)
                        while True:
                            try:
                                kol_inf = cursor_1.fetchall()
                                all_inf = kol_inf[kol]
                                full_name = all_inf['full_name']
                                university = all_inf['university']
                                email = all_inf['email']

                                break
                            except:
                                break

                    def file_check_choice_check(message):
                        if message.text == 'Отправить на оценивание':

                            global work_is_ok
                            with (connection.cursor() as cursor_1):
                                create_table_query_1 = "CREATE TABLE IF NOT EXISTS scientific_work(id int AUTO_INCREMENT," \
                                                       " unique_id varchar(7)," \
                                                       " full_name varchar(50)," \
                                                       " university varchar(50)," \
                                                       " email varchar(50)," \
                                                       " name_scientific_work varchar(300)," \
                                                       " id_scientific_work varchar(50)," \
                                                       " supervisor varchar(50)," \
                                                       " co_author varchar(50)," \
                                                       " date_of_publication varchar(50)," \
                                                       " work LONGBLOB," \
                                                       " expert_opinions LONGBLOB," \
                                                       " section_of_the_work varchar(200)," \
                                                       " PRIMARY KEY (id));"
                                cursor_1.execute(create_table_query_1)

                            def binary():
                                with open(
                                        f'{scr.name}',
                                        'rb') as f:
                                    blob = base64.b64encode(f.read())
                                    return blob
                            with connection.cursor() as cursor_1:
                                insert_querty = f"""INSERT INTO scientific_work(unique_id, full_name, university, email, name_scientific_work, id_scientific_work, date_of_publication, work, expert_opinions, section_of_the_work) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                                value = (
                                    a['unique_id'], {d2[f'{user_name}']['full_name']},
                                    {d2[f'{user_name}']['university']},
                                    {d2[f'{user_name}']['email']},
                                    {d2[f'{user_name}']['the_name_of_the_scientific_work']},
                                    os.path.basename(new_file.name), {d2[f'{user_name}']['date_of_publication']},
                                    {binary()},
                                    {binary()},
                                    {d2[f'{user_name}']['section_of_the_work']})
                                cursor_1.execute(insert_querty, value)
                                connection.commit()

                            work_is_ok = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                          'Работа отправлена на оценивание\nПереносим вас в главное меню',
                                                          reply_markup=None)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], scientific_work_report.message_id)




                            time.sleep(3)
                            print('11')
                            # dir = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/works'  # Удаление работ
                            # for f in os.listdir(dir):
                            #     os.remove(os.path.join(dir, f))
                            #
                            # dir = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/expert_opinions'  # Удаление работ
                            # for f in os.listdir(dir):
                            #     os.remove(os.path.join(dir, f))
                            # print('12')
                            main_menu_for_user(message)
                        elif message.text == 'Добавить научного руководителя':
                            def add_a_supervisor_check(message):
                                global user_is_not_found_co, email_from_user_co
                                email_from_user_co = message.text

                                with connection.cursor() as cursor:
                                    insert_querty_1_co = f"""SELECT * FROM login_and_password WHERE email='{email_from_user_co}'"""
                                    cursor.execute(insert_querty_1_co)

                                    @bot.callback_query_handler(
                                        func=lambda call: call.data == 'send_invitation_to_co_author')
                                    def send_invitation_to_supervisor(call):

                                        global send_is_ok, email_from_user_co
                                        while True:
                                            try:
                                                with connection.cursor() as cursor_5:
                                                    wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Научный руководитель'"""
                                                    cursor_5.execute(wait_1_co)
                                                    try:
                                                        v_co = cursor_5.fetchall()[0]
                                                        already_co = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                      'Вы уже отправили приглашение этому пользователю')
                                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                           user_is_not_found_co.message_id)
                                                        time.sleep(3)
                                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                           already_co.message_id)
                                                        test_def(message)
                                                        break

                                                    except:
                                                        try:
                                                            send_ya_mail(recipients_emails=[f'{email_from_user_co}'],
                                                                         msg_text=f'Добрый день!\n{full_name} отправил вам приглашение стать соавтором его работы на конференции СНИИ 2024\nЧто бы подтвердить свое участие в проекте необходимо перейти по ссылке ниже и авторизироваться на сервисе\nСсылка: https://t.me/Test_Conf21_bot')
                                                            print(email)
                                                            print(unical_id_from_login_and_password_db)
                                                            print({all_inf['name_scientific_work']})
                                                            print(email_from_user_co)
                                                            print(email, unical_id_from_login_and_password_db,
                                                                  {all_inf['name_scientific_work']},
                                                                  email_from_user_co, 'Научный руководитель')
                                                            with connection.cursor() as cursor_5:
                                                                wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                                value_co = (email, unical_id_from_login_and_password_db,
                                                                            {all_inf['name_scientific_work']},
                                                                            email_from_user_co, 'Научный руководитель')
                                                                cursor_5.execute(wait_co, value_co)
                                                                connection.commit()

                                                                send_is_ok = bot.send_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    'Приглашение отправленно на указанную электронную почту\nМы пришлем вам электронное письмо, когда пользователь зарегистрируется\nПереносим вас назад')
                                                                time.sleep(7)
                                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                   user_is_not_found_co.message_id)
                                                                test_def(message)
                                                                break
                                                        except:
                                                            print(email)
                                                            print(unical_id_from_login_and_password_db)
                                                            print({all_inf['name_scientific_work']})
                                                            print(email_from_user_co)
                                                            send_is_ok = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                          'Не удалось отправить сообщение по указанной электронной почте')
                                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                               user_is_not_found_co.message_id)
                                                            time.sleep(4)
                                                            test_def(message)
                                                            break
                                            except:
                                                send_is_ok = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                              'Не удалось выполнить действие\nОшибка 28\nОбратитесь в поддержку')
                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                   user_is_not_found_co.message_id)
                                                time.sleep(4)
                                                test_def(message)
                                                break

                                    @bot.callback_query_handler(
                                        func=lambda call: call.data == 'total_back_from_invitation_to_supervisor_1')
                                    def total_back_from_invitation_to_supervisor_1(call):
                                        global time_1
                                        time_1_co = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                     'Возвращаем вас раздел редактирования')
                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                           user_is_not_found_co.message_id)
                                        time.sleep(3)
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], time_1_co.message_id)
                                        test_def(message)

                                    def localdef(message):
                                        global user_is_not_found_co

                                        def localdef_choice_check_2(message):
                                            if message.text == 'Отправить приглашение':
                                                global send_is_ok, email_from_user_co
                                                while True:
                                                    try:
                                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                           message.message_id)
                                                        break
                                                    except:
                                                        break
                                                while True:
                                                    try:
                                                        with connection.cursor() as cursor_5:
                                                            wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Научный руководитель'"""
                                                            cursor_5.execute(wait_1_co)
                                                            try:
                                                                v_co = cursor_5.fetchall()[0]
                                                                already_co = bot.send_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    'Вы уже отправили приглашение этому пользователю')
                                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                   user_is_not_found_co.message_id)
                                                                time.sleep(3)
                                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                   already_co.message_id)
                                                                test_def(message)
                                                                break

                                                            except:
                                                                try:
                                                                    send_ya_mail(
                                                                        recipients_emails=[f'{email_from_user_co}'],
                                                                        msg_text=f'Добрый день!\n{full_name} отправил вам приглашение стать соавтором его работы на конференции СНИИ 2024\nЧто бы подтвердить свое участие в проекте необходимо перейти по ссылке ниже и авторизироваться на сервисе\nСсылка: https://t.me/Test_Conf21_bot')
                                                                    print(email)
                                                                    print(unical_id_from_login_and_password_db)
                                                                    print({all_inf['name_scientific_work']})
                                                                    print(email_from_user_co)
                                                                    with connection.cursor() as cursor_5:
                                                                        wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                                        value_co = (
                                                                            email, unical_id_from_login_and_password_db,
                                                                            {all_inf['name_scientific_work']},
                                                                            email_from_user_co, 'Научный руководитель')
                                                                        cursor_5.execute(wait_co, value_co)
                                                                        connection.commit()

                                                                        send_is_ok = bot.send_message(
                                                                            d2[f'{user_name}']['chat_id'],
                                                                            'Приглашение отправленно на указанную электронную почту\nМы пришлем вам электронное письмо, когда пользователь зарегистрируется\nПереносим вас назад')
                                                                        time.sleep(7)
                                                                        bot.delete_message(
                                                                            d2[f'{user_name}']['chat_id'],
                                                                            user_is_not_found_co.message_id)
                                                                        test_def(message)
                                                                        break
                                                                except:
                                                                    print(email)
                                                                    print(unical_id_from_login_and_password_db)
                                                                    print({all_inf['name_scientific_work']})
                                                                    print(email_from_user_co)
                                                                    send_is_ok = bot.send_message(
                                                                        d2[f'{user_name}']['chat_id'],
                                                                        'Не удалось отправить сообщение по указанной электронной почте')
                                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                       user_is_not_found_co.message_id)
                                                                    time.sleep(4)
                                                                    test_def(message)
                                                                    break
                                                    except:
                                                        send_is_ok = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                      'Не удалось выполнить действие\nОшибка 28\nОбратитесь в поддержку')
                                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                           user_is_not_found_co.message_id)
                                                        time.sleep(4)
                                                        test_def(message)
                                                        break
                                            elif message.text == 'Вернуться в меню редактирования':
                                                global time_1
                                                time_1_co = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                             'Возвращаем вас раздел редактирования')
                                                while True:
                                                    try:
                                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                           message.message_id)
                                                        break
                                                    except:
                                                        break
                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                   user_is_not_found_co.message_id)
                                                time.sleep(3)
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], time_1_co.message_id)
                                                test_def(message)

                                        invitation_to_co_author = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                                                            one_time_keyboard=True)

                                        btn1 = types.KeyboardButton('Отправить приглашение')
                                        btn2 = types.KeyboardButton('Вернуться в меню редактирования')

                                        invitation_to_co_author.row(btn1)
                                        invitation_to_co_author.row(btn2)

                                        user_is_not_found_co = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                text='Пользователь не '
                                                                                     'найден\nОтправить '
                                                                                     'приглашение на указанную '
                                                                                     'электронную почту?\nКогда '
                                                                                     'пользователь '
                                                                                     'зарегестрируется, '
                                                                                     'мы пришлем вам уведомление',
                                                                                reply_markup=invitation_to_co_author)
                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                           add_co_author_message.message_id)
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)

                                        bot.register_next_step_handler(message, localdef_choice_check_2)

                                    while True:
                                        try:
                                            all_from_db = cursor.fetchall()[0]
                                            with connection.cursor() as cursor_5:
                                                wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Научный руководитель'"""
                                                cursor_5.execute(wait_1_co)
                                                try:
                                                    v_co = cursor_5.fetchall()[0]
                                                    already_co = bot.send_message(
                                                        d2[f'{user_name}']['chat_id'],
                                                        'Вы уже отправили приглашение этому пользователю')
                                                    time.sleep(3)
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       already_co.message_id)
                                                    while True:
                                                        try:
                                                            bot.delete_message(
                                                                d2[f'{user_name}']['chat_id'],
                                                                add_co_author_message.message_id)
                                                            break
                                                        except:
                                                            break
                                                    while True:
                                                        try:
                                                            bot.delete_message(
                                                                d2[f'{user_name}']['chat_id'],
                                                                message.message_id)
                                                            break
                                                        except:
                                                            break
                                                    test_def(message)
                                                    break
                                                except:
                                                    if email_from_user_co == all_from_db['email']:
                                                        global send_is_ok
                                                        send_is_ok = bot.send_message(
                                                            d2[f'{user_name}']['chat_id'],
                                                            'Приглашение отправленно\nПосле подтверждения пользователем причастия к работе, мы отправим вам электронное письмо')
                                                        with connection.cursor() as cursor_5:
                                                            wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                            value_co = (
                                                                email,
                                                                unical_id_from_login_and_password_db,
                                                                {all_inf[
                                                                     'name_scientific_work']},
                                                                email_from_user_co,
                                                                'Научный руководитель')
                                                            cursor_5.execute(wait_co, value_co)
                                                            connection.commit()
                                                        while True:
                                                            try:
                                                                bot.delete_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    add_co_author_message.message_id)
                                                                break
                                                            except:
                                                                break
                                                        while True:
                                                            try:
                                                                bot.delete_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    message.message_id)
                                                                break
                                                            except:
                                                                break
                                                        time.sleep(5)
                                                        test_def(message)

                                                    break
                                        except IndexError:
                                            localdef(message)
                                            break

                            add_co_author_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                     'После того как владелец данной электронной почты подтвердит свою причастность к этой работе, мы пришлем вам уведомление\nЕсли ваш научный руководитель не зарегестрирован в системе, то мы отправим ему ссылку приглашение на электронную почту\nВведите электронную почту вашего научного руководителя:',
                                                                     reply_markup=None)
                            while True:
                                try:
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                    break
                                except:
                                    break
                            bot.delete_message(d2[f'{user_name}']['chat_id'], scientific_work_report.message_id)
                            bot.register_next_step_handler(message, add_a_supervisor_check)
                        elif message.text == 'Добавить соавтора':
                            def add_co_author_check(message):
                                global user_is_not_found_co, email_from_user_co
                                email_from_user_co = message.text

                                with connection.cursor() as cursor:
                                    insert_querty_1_co = f"""SELECT * FROM login_and_password WHERE email='{email_from_user_co}'"""
                                    cursor.execute(insert_querty_1_co)

                                    def localdef(message):
                                        global user_is_not_found_co

                                        def localdef_choice_check(message):
                                            if message.text == 'Отправить приглашение':
                                                global send_is_ok, email_from_user_co
                                                while True:
                                                    try:
                                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                           message.message_id)
                                                        break
                                                    except:
                                                        break
                                                while True:
                                                    try:
                                                        with connection.cursor() as cursor_5:
                                                            wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Соавтор'"""
                                                            cursor_5.execute(wait_1_co)
                                                            try:
                                                                v_co = cursor_5.fetchall()[0]
                                                                already_co = bot.send_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    'Вы уже отправили приглашение этому пользователю')
                                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                   user_is_not_found_co.message_id)
                                                                time.sleep(3)
                                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                   already_co.message_id)
                                                                file_check(message)


                                                            except:
                                                                try:
                                                                    send_ya_mail(
                                                                        recipients_emails=[f'{email_from_user_co}'],
                                                                        msg_text=f'Добрый день!\n{full_name} отправил вам приглашение стать соавтором его работы на конференции СНИИ 2024\nЧто бы подтвердить свое участие в проекте необходимо перейти по ссылке ниже и авторизироваться на сервисе\nСсылка: https://t.me/Test_Conf21_bot')

                                                                    with connection.cursor() as cursor_5:
                                                                        wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                                        value_co = (
                                                                            email, unical_id_from_login_and_password_db,
                                                                            {all_inf['name_scientific_work']},
                                                                            email_from_user_co, 'Соавтор')
                                                                        cursor_5.execute(wait_co, value_co)
                                                                        connection.commit()

                                                                        send_is_ok = bot.send_message(
                                                                            d2[f'{user_name}']['chat_id'],
                                                                            'Приглашение отправленно на указанную электронную почту\nМы пришлем вам электронное письмо, когда пользователь зарегистрируется\nПереносим вас в главное меню')
                                                                        time.sleep(7)
                                                                        bot.delete_message(
                                                                            d2[f'{user_name}']['chat_id'],
                                                                            user_is_not_found_co.message_id)
                                                                        test_def(message)
                                                                        break
                                                                except:
                                                                    send_is_ok = bot.send_message(
                                                                        d2[f'{user_name}']['chat_id'],
                                                                        'Не удалось отправить сообщение по указанной электронной почте')
                                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                       user_is_not_found_co.message_id)
                                                                    time.sleep(4)
                                                                    file_check(message)
                                                                    break
                                                    except:
                                                        send_is_ok = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                      'Не удалось выполнить действие\nОшибка 28\nОбратитесь в поддержку')
                                                        while True:
                                                            try:
                                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                                   user_is_not_found_co.message_id)
                                                                break
                                                            except:
                                                                break
                                                        time.sleep(4)
                                                        file_check(message)
                                                        break
                                            elif message.text == 'Вернуться в меню редактирования':
                                                global time_1
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                time_1_co = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                             'Возвращаем вас раздел редактирования')
                                                bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                   user_is_not_found_co.message_id)
                                                time.sleep(3)
                                                bot.delete_message(d2[f'{user_name}']['chat_id'], time_1_co.message_id)
                                                file_check(message)

                                        invitation_to_co_author = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                                                            one_time_keyboard=True)

                                        btn1 = types.KeyboardButton('Отправить приглашение')
                                        btn2 = types.KeyboardButton('Вернуться в меню редактирования')

                                        # btn4 = types.KeyboardButton(f'')

                                        invitation_to_co_author.row(btn1)
                                        invitation_to_co_author.row(btn2)

                                        user_is_not_found_co = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                                text='Пользователь не '
                                                                                     'найден\nОтправить '
                                                                                     'приглашение на указанную '
                                                                                     'электронную почту?\nКогда '
                                                                                     'пользователь '
                                                                                     'зарегестрируется, '
                                                                                     'мы пришлем вам уведомление',
                                                                                reply_markup=invitation_to_co_author)
                                        bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                           add_co_author_message.message_id)
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)

                                        bot.register_next_step_handler(message, localdef_choice_check)

                                    while True:
                                        try:
                                            all_from_db = cursor.fetchall()[0]
                                            with connection.cursor() as cursor_5:
                                                wait_1_co = f"""SELECT email_waiting_users FROM waiting_for_registration WHERE email_waiting_users='{email}' and id_waiting_users ='{unical_id_from_login_and_password_db}' and email_for_registration='{email_from_user_co}' and expected_user_status = 'Соавтор'"""
                                                cursor_5.execute(wait_1_co)
                                                try:
                                                    v_co = cursor_5.fetchall()[0]
                                                    already_co = bot.send_message(
                                                        d2[f'{user_name}']['chat_id'],
                                                        'Вы уже отправили приглашение этому пользователю')
                                                    time.sleep(3)
                                                    bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                                       already_co.message_id)
                                                    while True:
                                                        try:
                                                            bot.delete_message(
                                                                d2[f'{user_name}']['chat_id'],
                                                                add_co_author_message.message_id)
                                                            break
                                                        except:
                                                            break
                                                    while True:
                                                        try:
                                                            bot.delete_message(
                                                                d2[f'{user_name}']['chat_id'],
                                                                message.message_id)
                                                            break
                                                        except:
                                                            break
                                                    file_check(message)
                                                    break
                                                except:
                                                    if email_from_user_co == all_from_db['email']:
                                                        global send_is_ok
                                                        send_is_ok = bot.send_message(
                                                            d2[f'{user_name}']['chat_id'],
                                                            'Приглашение отправленно\nПосле подтверждения пользователем причастия к работе, мы отправим вам электронное письмо')
                                                        with connection.cursor() as cursor_5:
                                                            wait_co = f"""INSERT INTO waiting_for_registration(email_waiting_users, id_waiting_users, name_scientific_work, email_for_registration, expected_user_status) VALUES (%s, %s, %s, %s, %s)"""
                                                            value_co = (
                                                                email,
                                                                unical_id_from_login_and_password_db,
                                                                {all_inf[
                                                                     'name_scientific_work']},
                                                                email_from_user_co,
                                                                'Соавтор')
                                                            cursor_5.execute(wait_co, value_co)
                                                            connection.commit()
                                                        while True:
                                                            try:
                                                                bot.delete_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    add_co_author_message.message_id)
                                                                break
                                                            except:
                                                                break
                                                        while True:
                                                            try:
                                                                bot.delete_message(
                                                                    d2[f'{user_name}']['chat_id'],
                                                                    message.message_id)
                                                                break
                                                            except:
                                                                break
                                                        time.sleep(5)
                                                        file_check(message)

                                                    break

                                            break
                                        except IndexError:
                                            localdef(message)
                                            break

                            add_co_author_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                     'После того как владелец данной электронной почты подтвердит свою причастность к этой работе, мы пришлем вам уведомление\nЕсли ваш соавтор не зарегестрирован в системе, то мы отправим ему ссылку приглашение на электронную почту\nВведите электронную почту вашего соавтора:',
                                                                     reply_markup=None)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            bot.delete_message(d2[f'{user_name}']['chat_id'], scientific_work_report.message_id)
                            bot.register_next_step_handler(message, add_co_author_check)
                        elif message.text == 'Вернуться в главное меню':
                            global total_back_4
                            total_back_4 = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                            'Возвращаем вас в главное меню')
                            while True:
                                try:
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], scientific_work_report.message_id)
                                    break
                                except:
                                    break
                            time.sleep(3)
                            main_menu_for_user(message)

                    with connection.cursor() as cursor:
                        insert_querty_1 = f"""SELECT unique_id FROM login_and_password WHERE login='{login}' and password='{password.text}'"""
                        cursor.execute(insert_querty_1)
                        a = cursor.fetchall()[0]

                    with connection.cursor() as cursor:
                        all = f"SELECT full_name, university_full, email FROM login_and_password WHERE unique_id = '{a['unique_id']}'"
                        cursor.execute(all)
                        b = cursor.fetchall()[0]
                    scr = open(src, 'rb')
                    print('file check 8')
                    print(scr)
                    full_name = b['full_name']
                    university = b['university_full']
                    email = b['email']
                    v = {'full_name': f'{full_name}', 'university': f'{university}', 'email': f'{email}'}
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    d2[f'{user_name}'].update(v)

                    print('file check 9')
                    name_scientific_work = os.path.split(src)

                    south_africa = timezone('Asia/Novosibirsk')
                    sa_time = datetime.now(south_africa)
                    date_of_publication = sa_time.strftime('%d-%m-%Y_%H:%M')
                    v = {'date_of_publication': f'{date_of_publication}'}
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    d2[f'{user_name}'].update(v)
                    def test_def(message):
                        global scientific_work_report
                        is_work_alright = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                        btn1 = types.KeyboardButton('Отправить на оценивание')
                        btn2 = types.KeyboardButton('Добавить научного руководителя')
                        btn3 = types.KeyboardButton('Добавить соавтора')
                        btn4 = types.KeyboardButton('Вернуться в главное меню')

                        is_work_alright.row(btn1)
                        is_work_alright.row(btn2)
                        is_work_alright.row(btn3)
                        is_work_alright.row(btn4)
                        print('file check 10')

                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        scientific_work_report = bot.send_document(d2[f'{user_name}']['chat_id'], scr,
                                                                   caption=f'ФИО: {d2[f'{user_name}']['full_name']}\nУниверситет: {d2[f'{user_name}']['university']}\nEmail: {d2[f'{user_name}']['email']}\nНазвание работы: {d2[f'{user_name}']['the_name_of_the_scientific_work']}\n{d2[f'{user_name}']['section_of_the_work']}\nНаучный руководитель: {supervisor}\nСоавторы: {co_author}\nДата публикации: {d2[f'{user_name}']['date_of_publication']}',
                                                                   reply_markup=is_work_alright)
                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], file_uploaded_successfully.message_id)
                                break
                            except:
                                try:
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], send_is_ok.message_id)
                                    break
                                except:
                                    try:
                                        bot.delete_message(d2[f'{user_name}']['chat_id'], send_is_ok.message_id)
                                        break
                                    except:
                                        break
                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], upload.message_id)
                                break
                            except:
                                break
                        while True:
                            try:
                                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                break
                            except:
                                break

                        bot.register_next_step_handler(message, file_check_choice_check)

                    test_def(message)
                    break
                except Exception as ex:
                    print(f'Error ty99 - {ex}')
                    break

        def choice(message, start_message, choice_message, bot):
            user_name = message.from_user.username
            if str(user_name) == 'None':
                user_name = message.from_user.first_name
            bot.delete_message(d2[f'{user_name}']['chat_id'], start_message.message_id)
            bot.delete_message(d2[f'{user_name}']['chat_id'], choice_message.message_id)
            if message.text == 'Регистрация':
                registration(message, bot)
            elif message.text == 'Вход в аккаунт':
                login_to_account(message, bot)
            else:
                global refund
                refund = bot.send_message(d2[f'{user_name}']['chat_id'],
                                          'Неизвестная команда!\nВозвращаю вас в раздел авторизации')
                time.sleep(2)
                v = {'start_message_bool': 'False'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                d2[f'{user_name}'].update(v)
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                        break
                    except:
                        break

                start(message)

        def registration(message, bot):
            global login

            def login_request(message):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_login = bot.send_message(d2[f'{user_name}']['chat_id'], 'Придумайте логин:')
                v = {'start_message_bool': 'False'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                d2[f'{user_name}'].update(v)
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], request_to_registration.message_id)
                        break
                    except:
                        break
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], login_no.message_id)
                        break
                    except:
                        break
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                        break
                    except:
                        break
                if message.text == 'Регистрация':
                    while True:
                        try:
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            break
                        except:
                            break

                bot.register_next_step_handler(message, login_entry, what_login)

            def login_entry(message, what_login):
                global login, login_no
                login = message.text
                v = {'login': f'{login}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_login.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_login.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    with connection.cursor() as cursor:
                        unique_id_local = f"SELECT unique_id FROM login_and_password WHERE login='{login}'"
                        cursor.execute(unique_id_local)
                    try:
                        local_db_1 = (cursor.fetchall()[0])
                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        login_no = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                    'Этот логин уже занят другим человеком, придумайте другой\nПереносим вас назад')
                        bot.delete_message(d2[f'{user_name}']['chat_id'], what_login.message_id)
                        time.sleep(4)
                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                        login_request(message)
                    except:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], what_login.message_id)
                        password_request(message)

            def password_request(message):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_password = bot.send_message(d2[f'{user_name}']['chat_id'], 'Придумайте пароль:')
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                bot.register_next_step_handler(message, password_entry, what_password)

            def password_entry(message, what_password):
                global password
                password = message.text

                v = {'password': f'{password}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_password.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_password.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_password.message_id)

                    full_name_request(message)

            def full_name_request(message):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_full_name = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                  'Введите ФИО:\nПример: Петров Петр Петрович')
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                bot.register_next_step_handler(message, full_name_entry, what_full_name)

            def full_name_entry(message, what_full_name):
                global full_name
                full_name = message.text
                v = {'full_name': f'{full_name}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_full_name.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_full_name.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_full_name.message_id)

                    date_of_birth_request(message)

            def date_of_birth_request(message):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_date_of_birth = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                      'Введите дату рождения (в формате дд:мм:гггг):')
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                bot.register_next_step_handler(message, date_of_birth_entry, what_date_of_birth)

            def date_of_birth_entry(message, what_date_of_birth):
                global date_of_birth
                date_of_birth = message.text
                v = {'date_of_birth': f'{date_of_birth}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_date_of_birth.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_date_of_birth.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_date_of_birth.message_id)

                    phone_number_request(message)

            def phone_number_request(message):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_phone_number = bot.send_message(d2[f'{user_name}']['chat_id'], 'Введите номер телефона:')
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                bot.register_next_step_handler(message, phone_number_entry, what_phone_number)

            def phone_number_entry(message, what_phone_number):
                global phone_number
                phone_number = message.text
                v = {'phone_number': f'{phone_number}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_phone_number.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_phone_number.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_phone_number.message_id)

                    email_request(message)

            def email_request(message):
                global what_email
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_email = bot.send_message(d2[f'{user_name}']['chat_id'], 'Введите email:')
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], email_no.message_id)
                        break
                    except:
                        break
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                        break
                    except:
                        break

                bot.register_next_step_handler(message, email_entry, what_email)

            def email_entry(message, what_email):
                if message.text == 'Регистрация':
                    pass
                elif message.text == 'Вход в аккаунт':
                    pass
                else:
                    global email, email_no
                    email = message.text
                    v = {'email': f'{email}'}
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    if message.text == '/error':
                        local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                           'Возвращаю вас в меню авторизации')
                        time.sleep(3)
                        bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                        bot.delete_message(d2[f'{user_name}']['chat_id'], what_email.message_id)
                        start(message)
                    elif message.text == '/home':
                        local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                           'Возвращаю вас в меню авторизации')
                        time.sleep(3)
                        bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                        bot.delete_message(d2[f'{user_name}']['chat_id'], what_email.message_id)
                        start(message)
                    else:
                        d2[f'{user_name}'].update(v)
                        with connection.cursor() as cursor:
                            unique_id_local = f"SELECT unique_id FROM login_and_password WHERE email='{email}'"
                            cursor.execute(unique_id_local)
                        try:
                            local_db_1 = (cursor.fetchall()[0])
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            email_no = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                        'Эта электронная почта уже используется\nИспользуйте другую или войдите в аккаунт\nПереносим вас назад')
                            while True:
                                try:
                                    user_name = message.from_user.username
                                    if str(user_name) == 'None':
                                        user_name = message.from_user.first_name
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_email.message_id)
                                    time.sleep(4)
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                    email_request(message)
                                    break
                                except:
                                    email_request(message)
                                    break

                        except:
                            while True:
                                try:
                                    user_name = message.from_user.username
                                    if str(user_name) == 'None':
                                        user_name = message.from_user.first_name
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_email.message_id)
                                    break
                                except:
                                    break
                            while True:
                                try:
                                    random_code = random.randint(0, 1000000)
                                    print(f'randome - {random_code}')
                                    v = {'random_code': f'{random_code}'}
                                    user_name = message.from_user.username
                                    if str(user_name) == 'None':
                                        user_name = message.from_user.first_name
                                    d2[f'{user_name}'].update(v)
                                    send_ya_mail(recipients_emails=[f'{email}'],
                                                 msg_text=f'Добрый день!\n Данный адрес электронной почты был использован для регистрации на СНИИ2024\nКод потдтверждения электронной почты: {random_code}')
                                    code = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                            'Мы отправили код на указанную электронную почту\nВведите код из электронного письма:')
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                    bot.register_next_step_handler(message, checking_the_code, code)
                                    break
                                except Exception as ex:
                                    print(ex)
                                    global not_db
                                    not_db = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                              'Не получилось отправить письмо на указанную электронную почту\nПроверьте правильность введенной электронной почты\nВозвращаем вас в главное меню')
                                    time.sleep(7)
                                    start(message)
                                    break

            def checking_the_code(message, code):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], code.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], code.message_id)
                    start(message)
                else:
                    code_from_user = message.text
                    random_code = d2[f'{user_name}']['random_code']
                    print(f'code _from_user - {code_from_user}')
                    print(f'random_code - {random_code}')
                    if str(random_code) == code_from_user:
                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        bot.delete_message(d2[f'{user_name}']['chat_id'], code.message_id)
                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                        local_5 = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                   'Отлично! Электронная почта подтверждена\nПереносим вас дальше')
                        time.sleep(3)
                        university_request_full(message, local_5)
                    else:
                        global email_no
                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        bot.delete_message(d2[f'{user_name}']['chat_id'], code.message_id)
                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                        email_no = bot.send_message(d2[f'{user_name}']['chat_id'], 'Код неверный\nПереносим вас назад')
                        time.sleep(3)
                        email_request(message)

            def university_request_full(message, local_5):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_university = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                   'Введите  Полное наименование организации \n(Пример: Федеральное государственное автономное образовательное учреждение высшего образования «Национальный исследовательский Томский государственный университет»)')
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                        break
                    except:
                        break
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], local_5.message_id)
                        break
                    except:
                        break

                bot.register_next_step_handler(message, university_entry_full, what_university)

            def university_entry_full(message, what_university):
                global university_full
                university_full = message.text
                v = {'university_full': f'{university_full}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)

                    university_request_abbreviation(message)

            def university_request_abbreviation(message):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_university = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                   'Введите  аббревиатуру наименования организации \n(например, НИ ТГУ)')
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                bot.register_next_step_handler(message, university_entry_abbreviation, what_university)

            def university_entry_abbreviation(message, what_university):
                global university_abbreviation
                university_abbreviation = message.text
                v = {'university_abbreviation': f'{university_abbreviation}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)
                    university_request_abbreviation_en(message)

            def university_request_abbreviation_en(message):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                what_university = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                   'Введите аббревиатуру наименования организации на английском языке (например, NR TSU)')
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                bot.register_next_step_handler(message, university_entry_abbreviation_en, what_university)

            def university_entry_abbreviation_en(message, what_university):
                global university_abbreviation_en
                university_abbreviation_en = message.text
                v = {'university_abbreviation_en': f'{university_abbreviation_en}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_university.message_id)

                    user_status_info(message)

            def user_status_info(message):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name

                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                btn1 = types.KeyboardButton('Школьник')
                btn2 = types.KeyboardButton('Студент')
                btn3 = types.KeyboardButton('Аспирант')
                btn4 = types.KeyboardButton('Сотрудник')

                keyboard.row(btn1)
                keyboard.row(btn2)
                keyboard.row(btn3)
                keyboard.row(btn4)

                local_message = bot.send_message(d2[f'{user_name}']['chat_id'], text='Выберите свой статус',
                                                 reply_markup=keyboard)
                bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                bot.register_next_step_handler(message, user_status_info_check, local_message)

            def user_status_info_check(message, local_message):
                status1 = message.text
                v = {'user_status': f'{status1}'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_message.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_message.message_id)
                    start(message)
                else:
                    d2[f'{user_name}'].update(v)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_message.message_id)
                    consent_to_processing_request(message)

            def consent_to_processing_request(message):
                global for_deletion
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name

                if for_deletion == 'repeat_sending_photo':
                    # user_name = message.from_user.username
                    bot.delete_message(d2[f'{user_name}']['chat_id'], repeat_sending_photo.message_id)
                    for_deletion = ''
                # user_name = message.from_user.username
                what_consent_to_processing = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                              'Заполните согласие на обработку персональных данных и пришлите фотографию в чат (.jpg)')
                print(d2[f'{user_name}']['chat_id'])
                software_photo = bot.send_photo(d2[f'{user_name}']['chat_id'],
                                                'https://australianvisa.ru/wp-content/uploads/3/a/d/3ad6298c599e5270ce546464345b2c9e.jpeg')
                while True:
                    try:
                        bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                        break
                    except:
                        break
                bot.register_next_step_handler(message, consent_to_processing_entry, what_consent_to_processing,
                                               software_photo)

            def consent_to_processing_entry(message, what_consent_to_processing, software_photo):
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                if message.text == '/error':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_consent_to_processing.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], software_photo.message_id)
                    start(message)
                elif message.text == '/home':
                    local_a_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                       'Возвращаю вас в меню авторизации')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], local_a_message.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_consent_to_processing.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], software_photo.message_id)
                    start(message)
                else:
                    global full_information, application_sent
                    bot.delete_message(d2[f'{user_name}']['chat_id'], what_consent_to_processing.message_id)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], software_photo.message_id)
                    while True:
                        try:
                            global src, binary_photo, file_info
                            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                            downloaded_file = bot.download_file(file_info.file_path)

                            src = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/' + file_info.file_path;

                            with open(src, 'wb') as new_file:
                                new_file.write(downloaded_file)
                                new_file.close()

                            def convert_to_Binary_for_photo(filename):
                                with open(filename, 'rb') as file:
                                    binarydata = file.read()
                                    return binarydata
                                    file.close()

                            binary_photo = convert_to_Binary_for_photo(f'{src}')

                            v = {'src': f'{src}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)

                            v = {'binary_photo': f'{binary_photo}'}
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            d2[f'{user_name}'].update(v)

                            photo_added = bot.reply_to(message, "Фотография добавлена")



                            time.sleep(3)
                            break

                        except:
                            global repeat_sending_photo, for_deletion
                            repeat_sending_photo = bot.reply_to(message,
                                                                'Фотография не обнаружена\nПожалуйста, попробуйте еще раз через несколько секунд')
                            for_deletion = 'repeat_sending_photo'
                            time.sleep(4)
                            consent_to_processing_request(message)

                    try:
                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        bot.delete_message(d2[f'{user_name}']['chat_id'], photo_added.message_id)
                    except:
                        pass

                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                    btn1 = types.KeyboardButton('Все верно')
                    btn2 = types.KeyboardButton('Заполнить анкету заново')
                    btn3 = types.KeyboardButton('Вернуться в меню авторизации')
                    keyboard.row(btn1)
                    keyboard.row(btn2)
                    keyboard.row(btn3)



                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    full_information = bot.send_photo(chat_id=message.chat.id,
                                                      photo=open(d2[f'{user_name}']['src'], 'rb'),
                                                      caption=f'Логин: {d2[f'{user_name}']['login']}\nПароль: {d2[f'{user_name}']['password']}\nФИО: {d2[f'{user_name}']['full_name']}\nНомер телефона: {d2[f'{user_name}']['phone_number']}\nЭлектронная почта: {d2[f'{user_name}']['email']}\nУниверситет: {d2[f'{user_name}']['university_full']}',
                                                      reply_markup=keyboard)
                    bot.delete_message(message.chat.id, message.message_id)

                    bot.register_next_step_handler(message, consent_to_processing_check)

            def consent_to_processing_check(message):
                if message.text == 'Все верно':
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name

                    def convert_to_Binary_for_photo(filename):
                        with open(filename, 'rb') as file:
                            binarydata = file.read()
                            return binarydata
                    try:
                        with connection.cursor() as cursor:
                            insert_querty = f"INSERT INTO login_and_password (unique_id, login, password, full_name, date_of_birth, phone_number, email, university_full, university_abbreviation, university_abbreviation_en, user_status, consent, application_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            values_for_registration = (
                                random.randint(0, 1000000), {d2[f'{user_name}']['login']},
                                {d2[f'{user_name}']['password']},
                                {d2[f'{user_name}']['full_name']}, {d2[f'{user_name}']['date_of_birth']},
                                {d2[f'{user_name}']['phone_number']}, {d2[f'{user_name}']['email']},
                                {d2[f'{user_name}']['university_full']},
                                {d2[f'{user_name}']['university_abbreviation']},
                                {d2[f'{user_name}']['university_abbreviation_en']}, {d2[f'{user_name}']['user_status']},
                                binary_photo, 'Проверка')
                            cursor.execute(insert_querty, values_for_registration)
                            connection.commit()
                    except Exception as ex:
                        print(ex)

                        global not_db
                        not_db = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                  'Некорректные данные\nВозвращаю вас в главное меню')
                        bot.delete_message(d2[f'{user_name}']['chat_id'], full_information.message_id)
                        time.sleep(3)
                        start(message)


                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    application_sent = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                        'Ваша заявка на регистрацию успешно отправлена\nОжидайте одобрения заявки от организаторов в течении 24 часов\nМы пришлем вам электронное письмо, как только регистрация будет одобрена\nПереносим вас в главное меню',
                                                        reply_markup=None)
                    while True:
                        try:
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            bot.delete_message(d2[f'{user_name}']['chat_id'], full_information.message_id)
                            break
                        except:
                            pass
                    # test = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/photos'  # Удаление фото
                    # r = glob.glob(test)
                    # for i in r:
                    #     os.remove(i)

                    while True:
                        try:
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            bot.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                            break
                        except:
                            break
                    time.sleep(10)
                    while True:
                        try:
                            user_name = message.from_user.username
                            if str(user_name) == 'None':
                                user_name = message.from_user.first_name
                            bot.delete_message(d2[f'{user_name}']['chat_id'], application_sent.message_id)
                            break
                        except:
                            break

                    start(message)
                elif message.text == 'Заполнить анкету заново':
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    global request_to_registration
                    request_to_registration = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                               'Переносим вас в меню заполнения анкеты')
                    time.sleep(3)
                    bot.delete_message(d2[f'{user_name}']['chat_id'], full_information.message_id)
                    registration(message, bot)
                elif message.text == 'Вернуться в меню авторизации':
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    global total_back_message, message_to_delete_to_main_menu
                    total_back_message = bot.send_message(d2[f'{user_name}']['chat_id'], 'Возвращаю вас в главное меню',
                                                          reply_markup=None)
                    message_to_delete_to_main_menu = 'total_back_True'
                    time.sleep(3)
                    start(message)
                elif message.text == '/error':
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    bot.send_message(d2[f'{user_name}']['chat_id'], 'Возвращаю вас в меню авторизации')
                    start(message)
                elif message.text == '/home':
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    bot.send_message(d2[f'{user_name}']['chat_id'], 'Возвращаю вас в меню авторизации')
                    start(message)

            login_request(message)

        def login_to_account(message, bot):
            global login, password

            def log_in(message):
                global login
                login = message.text
                bot.delete_message(message.chat.id, what_is_the_login_1.id)

                what_is_the_password(message)

            def password_1(message):
                global password
                password = message

                check(password.text, message)

            def what_is_the_login(message):
                global what_is_the_login_1
                what_is_the_login_1 = bot.send_message(message.chat.id, 'Введите логин:')
                v = {'start_message_bool': 'False'}
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                d2[f'{user_name}'].update(v)
                bot.delete_message(message.chat.id, message.message_id)
                bot.register_next_step_handler(message, log_in)

            def what_is_the_password(message):
                global what_is_the_password_1
                what_is_the_password_1 = bot.send_message(message.chat.id, 'Введите пароль:')
                bot.delete_message(message.chat.id, message.message_id)
                bot.register_next_step_handler(message, password_1)

            def check(password, message):
                global Incorrect_login_or_password, Correct_login_or_password, password_from_db, Prohibited_character, message_to_delete_to_main_menu
                password_from_db = ''
                for i in login:
                    if i == "'":
                        Prohibited_character = bot.send_message(message.chat.id,
                                                                'Введен запрещенный сивол!\nВозвращаю вас в меню авторизации')
                        message_to_delete_to_main_menu = 'Prohibited_character'
                        time.sleep(3)
                        bot.delete_message(message.chat.id, what_is_the_password_1.id)
                        bot.delete_message(message.chat.id, message.id)

                        start(message)
                for i in password:
                    if i == "'":
                        Prohibited_character = bot.send_message(message.chat.id,
                                                                'Введен запрещенный сивол!\nВозвращаю вас в меню авторизации')
                        message_to_delete_to_main_menu = 'Prohibited_character'
                        time.sleep(3)
                        bot.delete_message(message.chat.id, what_is_the_password_1.id)
                        start(message)
                with connection.cursor() as cursor:
                    all = f"SELECT password FROM login_and_password WHERE login='{login}'"
                    cursor.execute(all)
                try:
                    password_from_db_1 = (cursor.fetchall()[0])
                    password_from_db = password_from_db_1['password']

                except IndexError:  # Неверный логин или логин и пароль!!
                    print('IndexError1')

                if password_from_db == password:
                    print('start0')
                    tables()
                    with connection.cursor() as cursor:
                        application_status = f"SELECT application_status FROM login_and_password WHERE login='{login}' and password='{password}'"
                        cursor.execute(application_status)
                    print('start1')
                    application_status_1 = (cursor.fetchall()[0])
                    application_status = application_status_1['application_status']
                    print('start2')
                    if application_status == 'Проверка':
                        global not_db
                        not_db = bot.send_message(message.chat.id,
                                                  'Ваша заявка на регистрацию просматривается модерацией\nМы пришлем вам письмо на электронную почту когда заявку примут/отклонят\nПереносим вас в главное меню')
                        bot.delete_message(message.chat.id, what_is_the_password_1.id)
                        bot.delete_message(message.chat.id, message.message_id)
                        time.sleep(7)
                        start(message)
                    elif application_status == 'Одобрено':
                        Correct_login_or_password = bot.send_message(message.chat.id,
                                                                     'Вы успешно вошли в аккаунт\nПереносим вас в главное меню')
                        bot.delete_message(message.chat.id, what_is_the_password_1.id)
                        bot.delete_message(message.chat.id, message.message_id)
                        message_to_delete_to_main_menu = 'Correct_login_or_password'
                        time.sleep(3)
                        main_menu_for_user(message)
                    elif application_status == 'Удалено':
                        try:
                            with connection.cursor() as cursor:
                                com = f"SELECT сomment FROM login_and_password WHERE login='{login}' and password='{password}'"
                                cursor.execute(com)

                            def local_message_check(message):
                                if message.text == 'Вернуться в меню авторизации':
                                    user_name = message.from_user.username
                                    if str(user_name) == 'None':
                                        user_name = message.from_user.first_name
                                    global total_back_message
                                    total_back_message = bot.send_message(d2[f'{user_name}']['chat_id'],
                                                                          'Возвращаю вас в главное меню',
                                                                          reply_markup=None)
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], not_db.message_id)
                                    time.sleep(3)
                                    start(message)

                            local_2 = (cursor.fetchall()[0])
                            comment_info = local_2['сomment']

                            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                            btn3 = types.KeyboardButton('Вернуться в меню авторизации')
                            keyboard.row(btn3)

                            not_db = bot.send_message(message.chat.id,
                                                      f'Ваш аккаунт был удален модерацией\nТак же был оставлен комментарий:\n{comment_info}',
                                                      reply_markup=keyboard)

                            with connection.cursor() as cursor:
                                com = f"DELETE FROM login_and_password WHERE login='{login}' and password='{password}'"
                                cursor.execute(com)
                                connection.commit()

                            while True:
                                try:
                                    bot.delete_message(message.chat.id, what_is_the_password_1.id)
                                    break
                                except:
                                    break
                            while True:
                                try:
                                    bot.delete_message(message.chat.id, message.message_id)
                                    break
                                except:
                                    break

                            bot.register_next_step_handler(message, local_message_check)
                        except Exception as e:
                            print(e)

                else:  # Неверный пароль, но верный логин!!
                    Incorrect_login_or_password = bot.send_message(message.chat.id,
                                                                   'Введен неверный логин или пароль!\nВозвращаю вас в раздел авторизации')
                    bot.delete_message(message.chat.id, what_is_the_password_1.id)
                    bot.delete_message(message.chat.id, message.message_id)
                    message_to_delete_to_main_menu = 'Incorrect_login_or_password'
                    time.sleep(3)
                    password_from_db = ''

                    start(message)

            what_is_the_login(message)

        while True:
            try:
                bot.polling(none_stop=True)
            except Exception as _ex:
                print(f'Error 9 - {_ex}')
                time.sleep(15)

    # Чат для модерации
    def task2():
        token_2 = '6647342828:AAFIVSCmu4EPzA4OTUYKBntxq76huL58lmc'
        bot_2 = telebot.TeleBot(token_2)

        def main_menu(message):
            user_name = message.from_user.username
            if str(user_name) == 'None':
                user_name = message.from_user.first_name
            global main_menu_message_for_moderation, message_to_delete_to_main_menu_for_moderation, total_back_message
            if message_to_delete_to_main_menu_for_moderation == 'Correct_login_or_password_for_moderation':
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], Correct_login_or_password_for_moderation.message_id)
                message_to_delete_to_main_menu_for_moderation = ''
            if total_back_message != '':
                user_name = message.from_user.username
                if str(user_name) == 'None':
                    user_name = message.from_user.first_name
                while True:
                    try:
                        bot_2.delete_message(d2[f'{user_name}']['chat_id'], total_back_message.message_id)
                        break
                    except:
                        break
                total_back_message = ''

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

            btn1 = types.KeyboardButton('Выйти из аккаунта')
            btn2 = types.KeyboardButton('Новые заявки на регистрацию')
            markup.row(btn1, btn2)

            main_menu_message_for_moderation = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                  'Возможности модерации для вас открыты\nВыберите действие',
                                                                  reply_markup=markup)
            while True:
                try:
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], text_for_check.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], application_is_ok.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], local1.message_id)
                    break
                except:
                    break

            bot_2.register_next_step_handler(message, check)

        def check(message):
            user_name = message.from_user.username
            if str(user_name) == 'None':
                user_name = message.from_user.first_name
            global transfer_to_the_authorization_menu, message_to_delete_to_main_menu_for_moderation, log_out_of_your_account, page_number, total_back_message, logged_out
            if message.text == 'Выйти из аккаунта':
                log_out_of_your_account = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                             'Выход из аккаунта')
                message_to_delete_to_main_menu_for_moderation = 'Выход из аккаунта'
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], main_menu_message_for_moderation.message_id)
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                logged_out = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                'Вы вышли из аккаунта\nПереносим вас в главное меню')
                time.sleep(3)
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], logged_out.message_id)
                start_2(message)
            elif message.text == 'Новые заявки на регистрацию':
                transfer_to_the_authorization_menu = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                        'Переносим вас в раздел заявок')
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], main_menu_message_for_moderation.message_id)
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                page_number = 0
                total_back_message = ''
                new_registration_applications(message)

        def new_registration_applications(message):
            user_name = message.from_user.username
            if str(user_name) == 'None':
                user_name = message.from_user.first_name
            global main_menu_message_1, main_menu_photo_1, total_back_message, main_menu_text_1, way_2

            @bot_2.callback_query_handler(func=lambda call: call.data == 'last_order_1')
            def last_order_1(call):
                global kol_for_moder
                if kol_for_moder > 0:
                    kol_for_moder -= 1
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], main_menu_text_1.message_id)
                    new_registration_applications(message)

            @bot_2.callback_query_handler(func=lambda call: call.data == 'next_order_2')
            def next_order_2(call):
                global kol_for_moder
                if kol_for_moder < kol_from_login_and_password - 1:
                    kol_for_moder += 1
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], main_menu_text_1.message_id)
                    new_registration_applications(message)

            @bot_2.callback_query_handler(func=lambda call: call.data == 'check_applications')
            def check_applications(call):
                global unique_id
                print(f'unique_id - {unique_id}')
                with connection.cursor() as cursor_1:
                    wait_3 = f"SELECT * FROM login_and_password WHERE unique_id = '{unique_id}'"
                    cursor_1.execute(wait_3)
                    while True:
                        global university_full, university_abbreviation, university_abbreviation_en
                        try:
                            all_for_moderation = cursor_1.fetchall()
                            print(all_for_moderation)
                            all_for_moderation = all_for_moderation[0]
                            print(all_for_moderation)

                            unique_id = all_for_moderation['unique_id']
                            full_name = all_for_moderation['full_name']
                            date_of_birth = all_for_moderation['date_of_birth']
                            phone_number = all_for_moderation['phone_number']
                            email = all_for_moderation['email']
                            university_full = all_for_moderation['university_full']
                            university_abbreviation = all_for_moderation['university_abbreviation']
                            university_abbreviation_en = all_for_moderation['university_abbreviation_en']
                            break
                        except Exception as ex:
                            all_for_moderation = cursor_1.fetchall()
                            print(all_for_moderation)

                            unique_id = all_for_moderation['unique_id']
                            full_name = all_for_moderation['full_name']
                            date_of_birth = all_for_moderation['date_of_birth']
                            phone_number = all_for_moderation['phone_number']
                            email = all_for_moderation['email']
                            university_full = all_for_moderation['university_full']
                            university_abbreviation = all_for_moderation['university_abbreviation']
                            university_abbreviation_en = all_for_moderation['university_abbreviation_en']
                            break

                            loc = bot_2.send_message(d2[f'{user_name}']['chat_id'], 'Новых заявок нет!')
                            time.sleep(3)
                            bot_2.delete_message(d2[f'{user_name}']['chat_id'], loc.message_id)
                            while True:
                                try:
                                    bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                         transfer_to_the_authorization_menu.message_id)
                                    break
                                except:
                                    break
                            main_menu(message)
                            break

                def check_applications_2(message):
                    while True:
                        try:
                            global way
                            with connection.cursor() as cursor_1:
                                wait_2 = f"SELECT * FROM login_and_password WHERE unique_id = '{unique_id}'"
                                cursor_1.execute(wait_2)
                                while True:
                                    try:
                                        global university_full, university_abbreviation, university_abbreviation_en
                                        all_for_moderation = cursor_1.fetchall()
                                        kol_from_login_and_password = len(all_for_moderation)
                                        print(all_for_moderation)
                                        all_for_moderation = all_for_moderation[0]
                                        print(all_for_moderation)

                                        university_full = all_for_moderation['university_full']
                                        university_abbreviation = all_for_moderation[
                                            'university_abbreviation']
                                        university_abbreviation_en = all_for_moderation[
                                            'university_abbreviation_en']
                                        break
                                    except Exception as ex:
                                        print(f'Error 99 - {ex}')
                                        break
                            while True:
                                try:
                                    user_name = message.from_user.username
                                    if str(user_name) == 'None':
                                        user_name = message.from_user.first_name
                                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], local_for_univercity.message_id)
                                    break
                                except:
                                    break

                            @bot_2.callback_query_handler(func=lambda call: call.data == 'total_back_from_decision')
                            def total_back_from_decision(call):

                                with connection.cursor() as cursor_1:
                                    wait_1 = f"UPDATE login_and_password SET application_status = 'Проверка' WHERE unique_id = '{unique_id}'"
                                    cursor_1.execute(wait_1)
                                    connection.commit()

                                global total_back_message
                                total_back_message = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                        'Возвращаю вас в главное меню',
                                                                        reply_markup=None)
                                time.sleep(3)
                                while True:
                                    try:
                                        bot_2.delete_message(d2[f'{user_name}']['chat_id'], text_for_check.message_id)
                                        break
                                    except:
                                        break
                                main_menu(message)

                            @bot_2.callback_query_handler(func=lambda call: call.data == 'approve_the_application')
                            def approve_the_application(call):
                                global application_is_ok
                                with connection.cursor() as cursor_1:
                                    wait_1 = f"UPDATE login_and_password SET application_status = 'Одобрено' WHERE unique_id = '{unique_id}'"
                                    cursor_1.execute(wait_1)
                                    connection.commit()
                                send_ya_mail(recipients_emails=[f'{email}'],
                                             msg_text=f'Добрый день!\nСтатус вашей регистрации на конференции СНИИ2024 изменился\nВойдите в аккаунт, что бы узнать подробнее\nСсылка: https://t.me/Test_Conf21_bot')
                                application_is_ok = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                       'Заявка одобрена! \nПереносим вас в главное меню')
                                bot_2.delete_message(d2[f'{user_name}']['chat_id'], text_for_check.message_id)
                                time.sleep(3)
                                main_menu(message)

                            @bot_2.callback_query_handler(func=lambda call: call.data == 'reject_application')
                            def reject_application(call):
                                def comment_if_application_is_no(message):
                                    while True:
                                        try:
                                            comment = message.text
                                            global local1
                                            with connection.cursor() as cursor_1:
                                                wait_1 = f"UPDATE login_and_password SET сomment = '{comment}' WHERE unique_id = '{unique_id}'"
                                                cursor_1.execute(wait_1)
                                                connection.commit()
                                            bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                                 application_is_no.message_id)
                                            local1 = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                        'Заявка удалена\nПереносим вас в главное меню')
                                            send_ya_mail(recipients_emails=[f'{email}'],
                                                         msg_text=f'Добрый день!\nСтатус вашей регистрации на конференции СНИИ2024 изменился\nВойдите в аккаунт, что бы узнать подробнее\nСсылка: https://t.me/Test_Conf21_bot')
                                            bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                            time.sleep(3)
                                            main_menu(message)
                                            break
                                        except Exception as ex:
                                            print(f'Error 55 - {ex}')
                                            break

                                global application_is_no
                                with connection.cursor() as cursor_1:
                                    wait_1 = f"UPDATE login_and_password SET application_status = 'Удалено' WHERE unique_id = '{unique_id}'"
                                    cursor_1.execute(wait_1)
                                    connection.commit()
                                application_is_no = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                       'Для удаления заявки необходимо написать причину удаления:')
                                bot_2.delete_message(d2[f'{user_name}']['chat_id'], text_for_check.message_id)
                                bot_2.register_next_step_handler(message, comment_if_application_is_no)

                            @bot_2.callback_query_handler(func=lambda call: call.data == 'edit_the_application')
                            def edit_the_application(call):
                                global text_for_check_2

                                @bot_2.callback_query_handler(func=lambda call: call.data == 'univercity_1')
                                def univercity_1(call):
                                    while True:
                                        try:

                                            def edit_univercity_1(message):
                                                global local_for_univercity
                                                university_full = message.text
                                                with connection.cursor() as cursor_1:
                                                    wait_1 = f"UPDATE login_and_password SET university_full = '{university_full}' WHERE unique_id = '{unique_id}'"
                                                    cursor_1.execute(wait_1)
                                                    connection.commit()
                                                bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                local_for_univercity = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                          'Изменения сохранены\nПереносим вас назад')
                                                bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                                     local_for_univercity_1.message_id)
                                                time.sleep(3)
                                                check_applications_2(message)

                                            local_for_univercity_1 = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                        'Пришлите исправленный вариант "Университет(полное наименование)"')
                                            while True:
                                                try:
                                                    bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                                         text_for_check_2.message_id)
                                                    break
                                                except:
                                                    break
                                            bot_2.register_next_step_handler(message, edit_univercity_1)
                                            break
                                        except Exception as ex:
                                            print(f'Error 43 - {ex}')
                                            break

                                @bot_2.callback_query_handler(func=lambda call: call.data == 'univercity_2')
                                def univercity_2(call):
                                    while True:
                                        try:

                                            def edit_univercity_1(message):
                                                global local_for_univercity
                                                university_abbreviation = message.text
                                                with connection.cursor() as cursor_1:
                                                    wait_1 = f"UPDATE login_and_password SET university_abbreviation = '{university_abbreviation}' WHERE unique_id = '{unique_id}'"
                                                    cursor_1.execute(wait_1)
                                                    connection.commit()
                                                bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                local_for_univercity = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                          'Изменения сохранены\nПереносим вас назад')
                                                bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                                     local_for_univercity_1.message_id)
                                                time.sleep(3)
                                                check_applications_2(message)

                                            local_for_univercity_1 = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                        'Пришлите исправленный вариант "Университет(аббревиатура на русском)"')
                                            while True:
                                                try:
                                                    bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                                         text_for_check_2.message_id)
                                                    break
                                                except:
                                                    break
                                            bot_2.register_next_step_handler(message, edit_univercity_1)
                                            break
                                        except Exception as ex:
                                            print(f'Error 43 - {ex}')
                                            break

                                @bot_2.callback_query_handler(func=lambda call: call.data == 'univercity_3')
                                def univercity_3(call):
                                    while True:
                                        try:

                                            def edit_univercity_1(message):
                                                global local_for_univercity
                                                university_abbreviation_en = message.text
                                                with connection.cursor() as cursor_1:
                                                    wait_1 = f"UPDATE login_and_password SET university_abbreviation_en = '{university_abbreviation_en}' WHERE unique_id = '{unique_id}'"
                                                    cursor_1.execute(wait_1)
                                                    connection.commit()
                                                bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                                                local_for_univercity = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                          'Изменения сохранены\nПереносим вас назад')
                                                bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                                     local_for_univercity_1.message_id)
                                                time.sleep(3)
                                                check_applications_2(message)

                                            local_for_univercity_1 = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                        'Пришлите исправленный вариант "Университет(аббревиатура на английском)"')
                                            while True:
                                                try:
                                                    bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                                         text_for_check_2.message_id)
                                                    break
                                                except:
                                                    break
                                            bot_2.register_next_step_handler(message, edit_univercity_1)
                                            break
                                        except Exception as ex:
                                            print(f'Error 43 - {ex}')
                                            break

                                @bot_2.callback_query_handler(
                                    func=lambda call: call.data == 'total_back_from_univercity')
                                def total_back_from_univercity(call):
                                    bot_2.send_message(d2[f'{user_name}']['chat_id'], 'Возвращаем вас назад')
                                    while True:
                                        try:
                                            bot.delete_message(d2[f'{user_name}']['chat_id'],
                                                               text_for_check_2.message_id)
                                            break
                                        except:
                                            break
                                    while True:
                                        try:
                                            bot.delete_message(d2[f'{user_name}']['chat_id'], text_for_check.message_id)
                                            break
                                        except:
                                            break
                                    check_applications_2(message)

                                for_univercity = telebot.types.InlineKeyboardMarkup()

                                univercity_1 = telebot.types.InlineKeyboardButton(
                                    text="Редактировать Университет(полное наименование)",
                                    callback_data='univercity_1')
                                univercity_2 = telebot.types.InlineKeyboardButton(
                                    text="Редактировать Университет(аббревиатура на русском)",
                                    callback_data='univercity_2')
                                univercity_3 = telebot.types.InlineKeyboardButton(
                                    text="Редактировать Университет(аббревиатура на английском)",
                                    callback_data='univercity_3')
                                total_back_from_univercity = telebot.types.InlineKeyboardButton(
                                    text="Назад в главное меню(Отказаться от рассмотрения заявки)",
                                    callback_data='total_back_from_univercity')

                                for_univercity.add(univercity_1)
                                for_univercity.add(univercity_2)
                                for_univercity.add(univercity_3)
                                for_univercity.add(total_back_from_univercity)

                                text_for_check_2 = bot_2.edit_message_reply_markup(d2[f'{user_name}']['chat_id'],
                                                                                   text_for_check.message_id,
                                                                                   reply_markup=for_univercity)

                            for_decision = telebot.types.InlineKeyboardMarkup()

                            approve_the_application = telebot.types.InlineKeyboardButton(text="Одобрить заявку",
                                                                                         callback_data='approve_the_application')
                            reject_application = telebot.types.InlineKeyboardButton(
                                text="Отклонить заявку + комментарий",
                                callback_data='reject_application')
                            edit_the_application = telebot.types.InlineKeyboardButton(
                                text="Редактировать строку 'Университет'",
                                callback_data='edit_the_application')
                            total_back_from_decision = telebot.types.InlineKeyboardButton(
                                text="Назад в главное меню(Отказаться от рассмотрения заявки)",
                                callback_data='total_back_from_decision')

                            for_decision.add(approve_the_application, reject_application)
                            for_decision.add(edit_the_application)
                            for_decision.add(total_back_from_decision)

                            with connection.cursor() as cursor_1:
                                wait_1 = f"UPDATE login_and_password SET application_status = 'Проверяется' WHERE unique_id = '{unique_id}'"
                                cursor_1.execute(wait_1)
                                connection.commit()

                            while True:
                                try:
                                    with connection.cursor() as cursor_1:
                                        wait_1 = f"""SELECT * FROM login_and_password WHERE unique_id='{unique_id}' """
                                        cursor_1.execute(wait_1)
                                        while True:
                                            try:
                                                user_name = message.from_user.username
                                                if str(user_name) == 'None':
                                                    user_name = message.from_user.first_name

                                                print('test 32')
                                                kol_inf = cursor_1.fetchmany(size=10)
                                                all_inf = kol_inf[0]
                                                work = all_inf['consent']
                                                print('test 33')

                                                def convert_binary_to_file(binary, name):
                                                    with open(name, 'wb') as file:
                                                        file.write(binary)
                                                convert_binary_to_file(work, d2[f'{user_name}']['work_doc'])

                                                print('OKOK')
                                                break
                                            except Exception as ex:
                                                print(f'Error t556 - {ex}')
                                                break

                                    break
                                except:
                                    def convert_binary_to_file(binary, name):
                                        with open(name, 'wb') as file:
                                            file.write(binary)

                                    convert_binary_to_file(work, d2[f'{user_name}']['work_doc'])
                                    break
                            while True:
                                try:
                                    bot.delete_message(d2[f'{user_name}']['chat_id'], text_for_check_2.message_id)
                                    break
                                except:
                                    break

                            global text_for_check
                            print('qwqwqwqw')
                            text_for_check = bot_2.send_document(d2[f'{user_name}']['chat_id'], open(d2[f'{user_name}']['way_2'], 'rb'),
                                                                 caption=f'Заявка на регистрацию {kol_for_moder + 1}/{kol_from_login_and_password}\nУникальный ID пользователя: {unique_id}\nФИО: {full_name}\nДата рождения: {date_of_birth}\nНомер телефона: {phone_number}\nУниверситет(полное наименование): {university_full}\nУниверситет(аббревиатура на русском): {university_abbreviation}\nУниверситет(аббревиатура на английском): {university_abbreviation_en}\nEmail: {email}',
                                                                 reply_markup=for_decision)

                            # dir = 'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/expert_opinions'  # Удаление соглашений
                            # for f in os.listdir(dir):
                            #     os.remove(os.path.join(dir, f))
                            break
                        except Exception as ex:
                            print(f'Error 85 - {ex}')
                            break
                    while True:
                        try:
                            bot_2.delete_message(d2[f'{user_name}']['chat_id'], main_menu_text_1.message_id)
                            break
                        except:
                            break

                check_applications_2(message)

            @bot_2.callback_query_handler(func=lambda call: call.data == 'total_back')
            def total_back(call):

                global total_back_message
                total_back_message = bot_2.send_message(d2[f'{user_name}']['chat_id'], 'Возвращаю вас в главное меню',
                                                        reply_markup=None)
                time.sleep(3)
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], main_menu_text_1.message_id)
                main_menu(message)

            if total_back_message != '':
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], total_back_message.message_id)
                total_back_message = ''

            def binary_to_file(binarydata, filename):
                filename = filename
                with open(filename, 'wb') as file:
                    file.write(binarydata)

            with connection.cursor() as cursor_1:
                wait_1 = "SELECT * FROM login_and_password WHERE application_status = 'Проверка'"
                cursor_1.execute(wait_1)
                while True:
                    try:
                        global unique_id, kol_for_moder
                        all_for_moderation = cursor_1.fetchall()
                        while True:
                            try:
                                kol_from_login_and_password = len(all_for_moderation)
                                break
                            except:
                                break

                        while True:
                            try:
                                all_for_moderation = all_for_moderation[kol_for_moder]
                                break
                            except:
                                while True:
                                    try:
                                        all_for_moderation = all_for_moderation[0]
                                        kol_for_moder = 1
                                        break
                                    except:
                                        break
                                break

                        unique_id = all_for_moderation['unique_id']
                        full_name = all_for_moderation['full_name']
                        date_of_birth = all_for_moderation['date_of_birth']
                        phone_number = all_for_moderation['phone_number']
                        email = all_for_moderation['email']
                        university_full = all_for_moderation['university_full']
                        university_abbreviation = all_for_moderation['university_abbreviation']
                        university_abbreviation_en = all_for_moderation['university_abbreviation_en']

                        local_random = f'Соглашение на обработку персональных данных {random.randint(0, 10000)}'
                        binary = all_for_moderation['consent']
                        way_2 = f'C:/Users/vadim/Desktop/сonference/Tg_bot_for_conference/photos' + f'/{local_random}.png'  # Не уверен на счет .png
                        v = {'way_2': f'{way_2}'}
                        user_name = message.from_user.username
                        if str(user_name) == 'None':
                            user_name = message.from_user.first_name
                        d2[f'{user_name}'].update(v)

                        src = binary_to_file(binary, way_2)
                        way_2 = open(way_2, 'rb')
                        break

                    except Exception as ex:
                        print(f'Error 51 - {ex}')
                        loc = bot_2.send_message(d2[f'{user_name}']['chat_id'], 'Новых заявок нет!')
                        time.sleep(3)
                        bot_2.delete_message(d2[f'{user_name}']['chat_id'], loc.message_id)
                        while True:
                            try:
                                bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                                     transfer_to_the_authorization_menu.message_id)
                                break
                            except:
                                break
                        main_menu(message)
                        break

            keyboard = telebot.types.InlineKeyboardMarkup()
            last_application = telebot.types.InlineKeyboardButton(text="Прошлая заявка",
                                                                  callback_data='last_order_1')
            next_application = telebot.types.InlineKeyboardButton(text="Следующая заявка",
                                                                  callback_data='next_order_2')
            check_applications = telebot.types.InlineKeyboardButton(text="Проверить заявку (получить доп информацию)",
                                                                    callback_data='check_applications')
            total_back = telebot.types.InlineKeyboardButton(text="Назад в главное меню",
                                                            callback_data='total_back')

            keyboard.add(last_application, next_application)
            keyboard.add(check_applications)
            keyboard.add(total_back)

            main_menu_text_1 = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                  f'Заявка на регистрацию {kol_for_moder + 1}/{kol_from_login_and_password}\nУникальный ID пользователя: {unique_id}\nФИО: {full_name}\nУниверситет(полное наименование): {university_full}\nEmail: {email}',
                                                  reply_markup=keyboard)
            while True:
                try:
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], transfer_to_the_authorization_menu.message_id)
                    break
                except:
                    break
            while True:
                try:
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], local_for_univercity.message_id)
                    break
                except:
                    break

        @bot_2.message_handler(commands=['start'])
        def start_2(message):
            global d2
            chat_id = message.chat.id
            user_name = message.from_user.username
            print(user_name)
            if str(user_name) == 'None':
                print('change user_name')
                user_name = message.from_user.first_name
                print(user_name)
            user_id = message.from_user.id
            d = {'chat_id': f'{chat_id}'}
            print(d)
            while True:
                try:
                    print(d2)
                    d4 = {f'{user_name}': d}
                    d4.items()
                    d2.update(d4)
                    print(d2)
                    break
                except:
                    d2 = {f'{user_name}': d}
                    d2.items()
                    user_name = message.from_user.username
                    if str(user_name) == 'None':
                        user_name = message.from_user.first_name
                    print(d2[f'{user_name}']['chat_id'])
                    print(d2)
                    break


            global message_2_chat_id, start_message_for_moderation
            message_2_chat_id = d2[f'{user_name}']['chat_id']

            start_message_for_moderation = bot_2.send_message(d2[f'{user_name}']['chat_id'], f'Войдите в аккаунт')

            if message_to_delete_to_main_menu_for_moderation == 'Correct_login_or_password_for_moderation':
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], Correct_login_or_password_for_moderation.message_id)
            elif message_to_delete_to_main_menu_for_moderation == 'Incorrect_login_or_password_for_moderation':
                bot_2.delete_message(d2[f'{user_name}']['chat_id'],
                                     Incorrect_login_or_password_for_moderation.message_id)
            elif message_to_delete_to_main_menu_for_moderation == '/start':
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
            elif message_to_delete_to_main_menu_for_moderation == 'Prohibited_character_for_moderation':
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], Prohibited_character_for_moderation.message_id)
            elif message_to_delete_to_main_menu_for_moderation == 'Выход из аккаунта':
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], log_out_of_your_account.message_id)

            login_to_account(message)

        def login_to_account(message):
            user_name = message.from_user.username
            if str(user_name) == 'None':
                user_name = message.from_user.first_name
            global login_for_moderation, password_for_moderation

            def log_in(message):
                global login_for_moderation
                login_for_moderation = message.text
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], what_is_the_login_1_for_moderation.id)
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], start_message_for_moderation.message_id)
                what_is_the_password(message)

            def password_1(message):
                password_for_moderation = message

                check(password_for_moderation.text, message)

            def what_is_the_login(message):
                global what_is_the_login_1_for_moderation
                what_is_the_login_1_for_moderation = bot_2.send_message(d2[f'{user_name}']['chat_id'], 'Введите логин:')
                bot_2.register_next_step_handler(message, log_in)

            def what_is_the_password(message):
                global what_is_the_password_1_for_moderation
                what_is_the_password_1_for_moderation = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                           'Введите пароль:')
                bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                bot_2.register_next_step_handler(message, password_1)

            def check(password_for_moderation, message):

                global Incorrect_login_or_password_for_moderation, Correct_login_or_password_for_moderation, password_from_db_for_moderation, message_to_delete_to_main_menu_for_moderation, Prohibited_character_for_moderation
                password_from_db_for_moderation = ''
                for i in login_for_moderation:
                    if i == "'":
                        Prohibited_character_for_moderation = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                 'Введен запрещенный сивол!\nВозвращаю вас в меню авторизации')
                        message_to_delete_to_main_menu_for_moderation = 'Prohibited_character_for_moderation'
                        time.sleep(3)
                        bot_2.delete_message(d2[f'{user_name}']['chat_id'], what_is_the_password_1_for_moderation.id)
                        bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.id)

                        start_2(message)
                for i in password_for_moderation:
                    if i == "'":
                        Prohibited_character_for_moderation = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                 'Введен запрещенный сивол!\nВозвращаю вас в меню авторизации')
                        message_to_delete_to_main_menu_for_moderation = 'Prohibited_character_for_moderation'
                        time.sleep(3)
                        bot_2.delete_message(d2[f'{user_name}']['chat_id'], what_is_the_password_1_for_moderation.id)
                        start_2(message)
                with connection.cursor() as cursor:
                    all = f"SELECT password FROM login_and_password_for_moderation WHERE login='{login_for_moderation}'"
                    cursor.execute(all)
                try:
                    password_from_db_1_for_moderation = (cursor.fetchall()[0])
                    password_from_db_for_moderation = password_from_db_1_for_moderation['password']

                except IndexError:  # Неверный логин или логин и пароль!!
                    print('IndexError1')
                if password_from_db_for_moderation == password_for_moderation:
                    message_to_delete_to_main_menu_for_moderation = 'Correct_login_or_password_for_moderation'
                    Correct_login_or_password_for_moderation = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                  'Вы успешно вошли в аккаунт\nПереносим вас в главное меню')
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], what_is_the_password_1_for_moderation.id)
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                    time.sleep(3)
                    main_menu(message)
                else:  # Неверный пароль, но верный логин!!
                    message_to_delete_to_main_menu_for_moderation = 'Incorrect_login_or_password_for_moderation'
                    Incorrect_login_or_password_for_moderation = bot_2.send_message(d2[f'{user_name}']['chat_id'],
                                                                                    'Введен неверный логин или пароль!\nВозвращаю вас в раздел авторизации')
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], what_is_the_password_1_for_moderation.id)
                    bot_2.delete_message(d2[f'{user_name}']['chat_id'], message.message_id)
                    time.sleep(3)
                    password_from_db_for_moderation = ''

                    start_2(message)

            what_is_the_login(message)

        while True:
            try:
                bot_2.polling(none_stop=True)
            except Exception as _ex:
                print(f'Error 8 - {_ex}')
                time.sleep(15)

    # Потоки программы для запуска и поддержки ботов(Пользователя, Модерации, Проверяющих)

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t2.join()
    t1.join()

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as _ex:
            print(f'Error 7 - {_ex}')
            time.sleep(15)


try:
    connection = pymysql.connect(
        host="host",
        port=port,
        user='user',
        password='password',
        database='database',
        charset="utf8",
        use_unicode=True,
        cursorclass=pymysql.cursors.DictCursor)
    connection.autocommit(True)
except Exception as ex:
    print(ex)


def tables():
    with connection.cursor() as cursor:
        create_table_query = "CREATE TABLE IF NOT EXISTS login_and_password(id int AUTO_INCREMENT," \
                             " unique_id varchar(7)," \
                             " login varchar(50)," \
                             " password varchar(50)," \
                             " full_name varchar(50)," \
                             " date_of_birth varchar(50)," \
                             " phone_number varchar(50)," \
                             " email varchar(50)," \
                             " university_full varchar(500)," \
                             " university_abbreviation varchar(50)," \
                             " university_abbreviation_en varchar(50)," \
                             " user_status varchar(50)," \
                             " consent LONGBLOB," \
                             " application_status varchar(50)," \
                             " сomment varchar(200)," \
                             " PRIMARY KEY (id))DEFAULT CHARSET=utf8;"
        cursor.execute(create_table_query)
    with (connection.cursor() as cursor_1):
        create_table_query_1 = "CREATE TABLE IF NOT EXISTS scientific_work(id int AUTO_INCREMENT," \
                               " unique_id varchar(7)," \
                               " full_name varchar(100)," \
                               " university varchar(400)," \
                               " email varchar(50)," \
                               " name_scientific_work varchar(300)," \
                               " id_scientific_work varchar(50)," \
                               " supervisor varchar(500)," \
                               " co_author varchar(500)," \
                               " date_of_publication varchar(50)," \
                               " work LONGBLOB," \
                               " expert_opinions LONGBLOB," \
                               " section_of_the_work varchar(200)," \
                               " PRIMARY KEY (id))DEFAULT CHARSET=utf8;"
        cursor_1.execute(create_table_query_1)
    with (connection.cursor() as cursor_5):
        create_table_query_2 = "CREATE TABLE IF NOT EXISTS waiting_for_registration(id int AUTO_INCREMENT," \
                               " email_waiting_users varchar(50)," \
                               " id_waiting_users varchar(50)," \
                               " name_scientific_work varchar(300)," \
                               " email_for_registration varchar(50)," \
                               " expected_user_status varchar(50)," \
                               " PRIMARY KEY (id))DEFAULT CHARSET=utf8;"
        cursor_5.execute(create_table_query_2)
    with (connection.cursor() as cursor_6):
        create_table_query_3 = "CREATE TABLE IF NOT EXISTS login_and_password_for_moderation(id int AUTO_INCREMENT," \
                               " login varchar(50)," \
                               " password varchar(50)," \
                               " PRIMARY KEY (id))DEFAULT CHARSET=utf8;"
        cursor_6.execute(create_table_query_3)
    with connection.cursor() as cursor_6:
        insert_querty_0 = f"INSERT INTO login_and_password_for_moderation (login, password) VALUES (%s, %s)"
        values_for_registration_0 = ('admin_56', 'admin_56')
        cursor_6.execute(insert_querty_0, values_for_registration_0)
        connection.commit()


tables()

if __name__ == '__main__':
    message_to_delete_to_main_menu_for_moderation = '/start'
    message_to_delete_to_main_menu = '/start'
    total_back_message = ''
    for_deletion = ''
    supervisor = 'НЕТ'
    co_author = 'НЕТ'
    kol = 0
    kol_for_moder = 0
    change = False
    block = False
    space = ''
    email_from_user_co = ''
    interesting_local = False
    email_check_kol = 0
    kol_wait_7_co = 0
    number_page_invitation = 0
    global name_scientific_work
    freeze_support()
    main_start()
