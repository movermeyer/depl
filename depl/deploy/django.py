from StringIO import StringIO
import textwrap
from os.path import exists
import re

from depl.deploy import python
from fabric.api import cd, prefix, put, sudo


def load(settings, package):
    if not exists('manage.py'):
        raise LookupError('Django projects need a manage.py')

    # settings
    settings_module = settings['settings']
    if settings_module is None:
        with open('manage.py') as f:
            m = re.search('''["']DJANGO_SETTINGS_MODULE['"], ["']([\d\w_.]+)["']''',
                         f.read())
            if not m:
                raise LookupError("manage.py doesn't have a settings module defined")
            settings_module = m.groups()[0]

    remote_path = '/var/www/depl-' + settings['id']

    # static files
    depl_settings = textwrap.dedent("""
    from %s import *

    STATIC_ROOT = 'depl-staticfiles'
    """ % settings_module)
    settings['static'] = {'/static': 'depl-staticfiles'}

    # wsgi - use the right settings
    wsgi_file = python.search_wsgi(settings)
    depl_wsgi = textwrap.dedent("""
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "depl_settings")
    from %s import *
    """) % wsgi_file
    settings['wsgi'] = 'depl_wsgi'

    def django_stuff():
        with cd(remote_path):
            put(StringIO(depl_settings), 'depl_settings.py', use_sudo=True)
            put(StringIO(depl_wsgi), 'depl_wsgi.py', use_sudo=True)
            sudo('chown www-data:www-data depl_settings.py')
            with prefix('source venv/bin/activate'):
                # collectstatic
                sudo('django-admin.py collectstatic --noinput --pythonpath . '
                     '--settings=depl_settings ', user='www-data')
                # syncdb
                sudo('django-admin.py syncdb --noinput --pythonpath . '
                     '--settings=depl_settings ', user='www-data')

    dependencies, commands = python.load(settings, package)
    return dependencies, commands + [django_stuff]
