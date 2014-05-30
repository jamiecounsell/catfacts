# Change Mood
import sys, atexit, time, os
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from datetime import datetime
from django.conf import settings
from grumpy.helpers import current_mood, change_mood


def exit_remove_pid():
    p = '/home/webadmin/catfacts/mood.pid'
    os.remove(p)

def pid_is_running(pid):
    try:
        os.kill(pid, 0)

    except OSError:
        return

    else:
        return pid

def write_pidfile_or_die(path_to_pidfile):

    if os.path.exists(path_to_pidfile):
        pid = int(open(path_to_pidfile).read())

        if pid_is_running(pid):
            print("Sorry, Grumpy is already running with PID: {0}".format(pid))
            raise SystemExit

        else:
            os.remove(path_to_pidfile)

    open(path_to_pidfile, 'w').write(str(os.getpid()))
    return path_to_pidfile

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        				make_option('--long', '-l', dest='long',
            			help='Help for the long options'),
    				)
    help = 'Meow, there is no help for you.'

    def handle(self, **options):
         try:
            s = time.time()
            write_pidfile_or_die('/home/webadmin/catfacts/mood.pid')
            print "Changing mood."

            m = change_mood()

            print("Done. Mood is {0}!".format(m))
            t = time.time() - s

            print('Grumpy process {0} finished work! {1}s'.format(os.getpid(), round(t, 2)))
            
         except Exception as e:
            print e

atexit.register(exit_remove_pid)