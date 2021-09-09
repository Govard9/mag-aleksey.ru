import os, sys
sys.path.insert(0, '/home/b/belomakk/mag-aleksey.ru')
sys.path.insert(1, '/home/b/belomakk/.local/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
