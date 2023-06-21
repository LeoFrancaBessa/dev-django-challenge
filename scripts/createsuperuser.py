import logging
from django.contrib.auth.models import User


if not User.objects.filter(username='useradmin').exists():
    User.objects.create_superuser('useradmin', 'useradmin@example.com', 'Mundo098@')
    logging.warn('Super usuário criado')
    logging.warn('username : admin / senha : Mundo098@')
else:
    logging.warn('Usuário já existe')