import telebot
import constants
import os
import logging
import random
import WebHook
import cherrypy

bot = telebot.TeleBot(constants.token)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


def log(message, answer):
    print('\n -------')
    from datetime import datetime
    print(datetime.now())
    print('Повідомлення від {0} {1}. id = {2}\n Текст - {3}'.format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('/schedule', '/exams')
    user_markup.row('/alcohol_party', 'рофл', 'Audio')
    bot.send_message(message.from_user.id, 'Ранок добрий! ', reply_markup=user_markup)


@bot.message_handler(commands=['exams'])
def handle_exams(message):

        if message.text == '/exams' and ((message.from_user.id == 527015957) or
                                         (message.from_user.id == 396904570) or
                                         (message.from_user.id == 482586910) or
                                         (message.from_user.id == 491288853) or
                                         (message.from_user.id == 337254056) or
                                         (message.from_user.id == 486661473) or
                                         (message.from_user.id == 456295869) or
                                         (message.from_user.id == 429766188) or
                                         (message.from_user.id == 600382419) or
                                         (message.from_user.id == 653014541) or
                                         (message.from_user.id == 653608792) or
                                         (message.from_user.id == 307395118)):
            bot.send_message(message.from_user.id, constants.exams[0] + constants.exams[1])
            log(message, answer='okay')


@bot.message_handler(commands=['alcohol_party'])
def handle_alcohol_party(message):
        if message.text == '/alcohol_party' and ((message.from_user.id == 527015957) or
                                                 (message.from_user.id == 396904570) or
                                                 (message.from_user.id == 482586910) or
                                                 (message.from_user.id == 491288853) or
                                                 (message.from_user.id == 337254056) or
                                                 (message.from_user.id == 486661473) or
                                                 (message.from_user.id == 456295869) or
                                                 (message.from_user.id == 429766188) or
                                                 (message.from_user.id == 600382419) or
                                                 (message.from_user.id == 653014541) or
                                                 (message.from_user.id == 653608792) or
                                                 (message.from_user.id == 307395118)):
            bot.send_chat_action(message.from_user.id, 'find_location')
            bot.send_location(message.from_user.id, 49.54354869, 25.56928664)
            log(message, answer='okay')


@bot.message_handler(commands=['schedule'])
def handle_schedule(message):
    if message.text == '/schedule':
        for word in constants.schedule:
            bot.send_message(message.from_user.id, word)
        log(message, answer='okay')


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Нервує блок з командами, без проблем - закриваю, тільки не бий ',
                    reply_markup=hide_markup)


@bot.message_handler(content_types=['text'])
def handle_messages(message):

        if (message.text == 'Тоня' or message.text == 'тоня') and \
                ((message.from_user.id == 527015957) or
                 (message.from_user.id == 396904570) or
                 (message.from_user.id == 482586910) or
                 (message.from_user.id == 491288853) or
                 (message.from_user.id == 337254056) or
                 (message.from_user.id == 486661473) or
                 (message.from_user.id == 456295869) or
                 (message.from_user.id == 429766188) or
                 (message.from_user.id == 600382419) or
                 (message.from_user.id == 653014541) or
                 (message.from_user.id == 653608792) or
                 (message.from_user.id == 307395118)):
            answer = '*Біжу по гуртожитку і кричу* *Тоня ТИ ДЕ??????'
            bot.send_message(message.chat.id, answer)
            log(message, answer)
        elif (message.text == 'рофл' or
              message.text == 'Рофл' or
              message.text == 'rofl' or
              message.text == 'Rofl') and ((message.from_user.id == 527015957) or
                                           (message.from_user.id == 396904570) or
                                           (message.from_user.id == 482586910) or
                                           (message.from_user.id == 491288853) or
                                           (message.from_user.id == 337254056) or
                                           (message.from_user.id == 486661473) or
                                           (message.from_user.id == 456295869) or
                                           (message.from_user.id == 429766188) or
                                           (message.from_user.id == 600382419) or
                                           (message.from_user.id == 653014541) or
                                           (message.from_user.id == 653608792) or
                                           (message.from_user.id == 307395118)):
            directory_photo = 'D:\Бот_ім_13\Рофли'
            img = (open(directory_photo + '/' + random.choice(os.listdir(directory_photo)), 'rb'))
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()
            log(message, answer='okay')
        elif (message.text == 'аудішки' or
              message.text == 'audio' or
              message.text == 'Аудішки' or
              message.text == 'Audio') and ((message.from_user.id == 527015957) or
                                            (message.from_user.id == 396904570) or
                                            (message.from_user.id == 482586910) or
                                            (message.from_user.id == 491288853) or
                                            (message.from_user.id == 337254056) or
                                            (message.from_user.id == 486661473) or
                                            (message.from_user.id == 456295869) or
                                            (message.from_user.id == 429766188) or
                                            (message.from_user.id == 600382419) or
                                            (message.from_user.id == 653014541) or
                                            (message.from_user.id == 653608792) or
                                            (message.from_user.id == 307395118)):
            directory_audio = 'D:\Бот_ім_13\Рофли_аудіо'
            ###
            audio = (open(directory_audio + '/' + random.choice(os.listdir(directory_audio)), 'rb'))
            bot.send_chat_action(message.from_user.id, 'upload_audio')
            bot.send_audio(message.from_user.id, audio)
            audio.close()
            log(message, answer='okay')
        elif (message.text == 'Для настрою') and ((message.from_user.id == 527015957) or
                                                  (message.from_user.id == 396904570) or
                                                  (message.from_user.id == 482586910) or
                                                  (message.from_user.id == 491288853) or
                                                  (message.from_user.id == 337254056) or
                                                  (message.from_user.id == 486661473) or
                                                  (message.from_user.id == 456295869) or
                                                  (message.from_user.id == 429766188) or
                                                  (message.from_user.id == 600382419) or
                                                  (message.from_user.id == 653014541) or
                                                  (message.from_user.id == 653608792) or
                                                  (message.from_user.id == 307395118)):
            random_number = random.randint(1, 10)
            bot.send_message(message.from_user.id, random_number)
        elif (message.text == 'Тарас' or
              message.text == 'тарас') and ((message.from_user.id == 527015957) or
                                            (message.from_user.id == 396904570) or
                                            (message.from_user.id == 482586910) or
                                            (message.from_user.id == 491288853) or
                                            (message.from_user.id == 337254056) or
                                            (message.from_user.id == 486661473) or
                                            (message.from_user.id == 456295869) or
                                            (message.from_user.id == 429766188) or
                                            (message.from_user.id == 600382419) or
                                            (message.from_user.id == 653014541) or
                                            (message.from_user.id == 653608792) or
                                            (message.from_user.id == 307395118)):
            directory_gifts = 'D:\Бот_ім_13\Рофли_гіфки'
             ####
            gifts = (open(directory_gifts + '/' + random.choice(os.listdir(directory_gifts)), 'rb'))
            bot.send_chat_action(message.from_user.id, 'upload_video')
            bot.send_video(message.from_user.id, gifts)
            gifts.close()
            log(message, answer='okay')
        elif (message.text == 'Око' or
              message.text == 'око') and ((message.from_user.id == 527015957) or
                                        (message.from_user.id == 396904570) or
                                        (message.from_user.id == 482586910) or
                                        (message.from_user.id == 491288853) or
                                        (message.from_user.id == 337254056) or
                                        (message.from_user.id == 486661473) or
                                        (message.from_user.id == 456295869) or
                                        (message.from_user.id == 429766188) or
                                        (message.from_user.id == 600382419) or
                                        (message.from_user.id == 653014541) or
                                        (message.from_user.id == 653608792) or
                                        (message.from_user.id == 307395118)):

            oko_voice = (open('D:\Бот_ім_13' + '/' + 't_voice5301237537421918696.ogg', 'rb'))
            bot.send_chat_action(message.from_user.id, 'upload_audio')
            bot.send_voice(message.from_user.id, oko_voice)
            oko_voice.close()
            log(message, answer='okay')
        elif (message.text == 'Вова' or
              message.text == 'вова') and ((message.from_user.id == 527015957) or
                                           (message.from_user.id == 396904570) or
                                           (message.from_user.id == 482586910) or
                                           (message.from_user.id == 491288853) or
                                           (message.from_user.id == 337254056) or
                                           (message.from_user.id == 486661473) or
                                           (message.from_user.id == 456295869) or
                                           (message.from_user.id == 429766188) or
                                           (message.from_user.id == 600382419) or
                                           (message.from_user.id == 653014541) or
                                           (message.from_user.id == 653608792) or
                                           (message.from_user.id == 307395118)):
            bot.send_message(message.from_user.id, '*Вихожу...*, сорок?')
            log(message, answer='okay')
        elif (message.text == 'Валєра' or
              message.text == 'валєра') and ((message.from_user.id == 527015957) or
                                             (message.from_user.id == 396904570) or
                                             (message.from_user.id == 482586910) or
                                             (message.from_user.id == 491288853) or
                                             (message.from_user.id == 337254056) or
                                             (message.from_user.id == 486661473) or
                                             (message.from_user.id == 456295869) or
                                             (message.from_user.id == 429766188) or
                                             (message.from_user.id == 600382419) or
                                             (message.from_user.id == 653014541) or
                                             (message.from_user.id == 653608792) or
                                             (message.from_user.id == 307395118)):
            valera_photo = (open('D:\Бот_ім_13' + '/' + 'photo5472064471892601413.jpeg', 'rb'))
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, valera_photo)
            valera_photo.close()
            log(message, answer='okay')


bot.remove_webhook()

bot.set_webhook(url=constants.WEBHOOK_URL_BASE + constants.WEBHOOK_URL_PATH,
                certificate=open(constants.WEBHOOK_SSL_CERT, 'r'))


cherrypy.quickstart(WebHook.WebHookServer(), constants.WEBHOOK_URL_PATH, {'/': {}})
