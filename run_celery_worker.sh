#!/bin/sh

# wait for PSQL server to start
sleep 10

su -m root -c "celery -A backend worker --loglevel=info"