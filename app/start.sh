GUNICORN_CMD_ARGS="--bind=0.0.0.0:7000 --workers=1 --log-file=-" gunicorn app.app:app -e PYTHONUNBUFFERED="TRUE"
