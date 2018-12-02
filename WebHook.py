import constants
import cherrypy
import telebot

bot = telebot.TeleBot(constants.token)


class WebHookServer(object):
    """Куча непонятних речей які гугл не зміг обяснити, крім того що цей клас ставить вебхук,
    чи просто видає URL на яке приходять оповіщення..."""
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)

            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


cherrypy.config.update({
    'server.socket_host': constants.WEBHOOK_LISTEN,
    'server.socket_port': constants.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': constants.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': constants.WEBHOOK_SSL_PRIV})
