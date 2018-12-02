import ssl
import OpenSSL

token = '757135112:AAFORt0ZC9Lr3B80-_OGamm0fnOcCb0eKNA'

exams = ['Мат.аналіз - 17 грудня, 9 год 410 аудиторя', '\nІсторія - 26 грудня, 9 год, 418 аудиторія']
schedule = ['Понеділок \n'
            ' 1 - Архітектура комп.(403 - аудиторія)\n'
            ' 2 - Архітектура комп.(403 - аудиторія) \n'
            ' 3 - Програмне забеспечення(427 - аудиторія)\n'
            ' 4 - Програмне забеспечення(427 - аудиторія)\n',
            'Вівторок\n'
            ' 1 - Валеологія(607 - аудиторія)\n'
            ' 2 - Історія(420 - аудиторія мейбі)\n'
            ' 3 - Вища математика(430 - аудиторія)\n'
            ' 4 - Вища математика(430 - аудиторія)\n',
            'Середа\n'
            ' 1 - Операційні системи(414 - аудиторія)\n'
            ' 2 - Операційні системи(414 - аудиторія)\n'
            ' 3 - Елементарна математика(419 - аудиторія)\n'
            ' 4 - Запитати у старости \n'
            ' 5 - Фізкультура',
            'Четвер\n'
            ' 1 - Мат.аналіз(410 - аудиторія)\n'
            ' 2 - Мат.аналіз(410 - аудиторія)\n'
            ' 3 - Програмування(427 - аудиторія)\n'
            ' 4 - Програмування(427 - аудиторія)\n']
#group = {'Stas': 527015957, 'Vetal_Z': 491288853, 'Den': 396904570, 'Galas': 482586910}
WEBHOOK_HOST = '188.163.32.99'
WEBHOOK_PORT = 443 #80, 88 або 8443 (відкритий)
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу
WEBHOOK_SSL_CERT = '/webhook_cert.pem'  # Путь к сертификату


WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{0}/".format(token)
print(ssl.get_server_certificate((WEBHOOK_HOST, 443)))
cert = ssl.get_server_certificate((WEBHOOK_HOST, 443))

# OpenSSL
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
x509.get_subject().get_components()
#[('C', 'US'),
# ('ST', 'California'),
# ('L', 'Mountain View'),
# ('O', 'Google Inc'),
# ('CN', 'www.google.com')]