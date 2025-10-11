import multiprocessing
import os


workers = min(multiprocessing.cpu_count() * 2 + 1, 8)

worker_class = 'sync'



timeout = 60

# Timeout gracioso para restart de workers
graceful_timeout = 30

# Keep-alive entre requests
keepalive = 2


bind = '0.0.0.0:8000'

backlog = 2048


accesslog = '-'
errorlog = '-'
loglevel = 'warning' 

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

proc_name = 'django_app'


max_requests = 1000
max_requests_jitter = 100 

timeout_worker_boot = 30

limit_request_line = 4094

limit_request_fields = 100
limit_request_field_size = 8190


preload_app = True
reuse_port = True
reload = False
