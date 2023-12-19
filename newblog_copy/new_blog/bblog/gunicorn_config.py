bind = '127.0.0.1:8000'

workers = 2

threads = 2

worker_class = 'sync'

accesslog = '/var/log/gunicorn_acess.log'
errorlog = '/var/log/gunicorn_error.log'

loglevel = 'info'

timeout = 30

daemon = 'true'
