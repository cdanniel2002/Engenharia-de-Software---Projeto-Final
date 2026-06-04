from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-*_n9rhh6)*li)qt3#2&43w5k1&fo_vk#o!p^ifb+6k=ho7q@l0'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]

# Em desenvolvimento não há servidor SMTP configurado: imprime e-mails no
# console e desativa os e-mails de ativação/confirmação do Djoser para que
# o cadastro funcione sem depender de envio de e-mail.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DJOSER = {
    **DJOSER,
    'SEND_ACTIVATION_EMAIL': False,
    'SEND_CONFIRMATION_EMAIL': False,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': False,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': False,
}
