#!/bin/bash

NAME="riodevday" #Name app
DJANGODIR=/home/webapps/riodevday/current/
SOCKFILE=/home/webapps/riodevday/run/gunicorn.sock  # we will communicte using
NUM_WORKERS=3                                     # how many worker processes
DJANGO_SETTINGS_MODULE=riodevday.settings_production             # which settings file should
DJANGO_WSGI_MODULE=riodevday.wsgi                     # WSGI module name

# Activate the virtual environment
cd $DJANGODIR
source /home/webapps/riodevday/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do
# not use --daemon)

exec /home/webapps/riodevday/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--bind=unix:$SOCKFILE \
	--log-level=debug \
	--log-file=-
