import os, sys
sys.path.append('/usr/lib/python2.6/site-packages/django')
sys.path.append('/home/uw/dumponus')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

