[uwsgi]
chdir           = /home/webadmin/catfacts/catfact
wsgi-file       = /home/webadmin/catfacts/catfact/catfact/wsgi.py
module          = catfact.uwsgi:application
master          = true
socket          = :8001
uid             = catfact
gid             = catfact
chmod-socket	= 664
vacuum          = true
processes       = 10
workers         = 5
