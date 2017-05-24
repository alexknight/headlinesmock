### 1.pip依赖安装
``` bash
$ sudo apt-get install python-pip
$ sudo apt-get install build-essential python
$ sudo pip install uwsgi
$ sudo apt-get install python-mysqldb
$ sudo pip install -r requirements.txt
``` 
### 2.mysql安装
``` bash
$ sudo apt-get install mysql-server  (root/ucwebit)
$ sudo vim /etc/mysql/my.cnf 
#bind-address = 127.0.0.1 
$ sudo /etc/init.d/mysql restart
```

### 3.redis-server安装
``` bash
$ cd /home/ucweb/mockServer/
$ wget http://download.redis.io/releases/redis-3.0.6.tar.gz
$ tar xzf redis-3.0.6.tar.gz
$ cd redis-3.0.6

$ make
$ sudo mv redis-3.0.6 redis
$ sudo vim redis/redis.conf
#bind 127.0.0.1 192.168.1.102
$ sudo make install
$ sudo ln -sf /usr/local/bin/redis-server /etc/init.d/redis-server
$ /etc/init.d/redis-server &
$ sudo apt-get install sysv-rc-conf #加入开机自启动
$ sysv-rc-conf redis-server on
```

### 4.更改配置
``` bash
$ sudo vim prestart.py
pool = redis.ConnectionPool(host='127.0.0.1',db=0,socket_timeout=3)
$ sudo vim settings.py
======================================
class DevelopmentConfig(Config):
    DEBUG = False
    # session
    CSRF_ENABLED = True
    SECRET_KEY = "4234189"
    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://root:ucwebit@127.0.0.1/mockapi"
    SQLALCHEMY_ECHO = True
    REDIS_SERVER = "127.0.0.1"
    REDIS_DB = 0
======================================
$ sudo vim manage.py
manager.add_command("runserver",Server(host="xx.xx.xx.xx",port=5000,use_reloader=True))
```
 
### 5.nginx安装配置
``` bash
$ sudo add-apt-repository ppa:nginx/stable
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install nginx
$ vim /etc/nginx/nginx.conf
        server {
        listen      8050;
        server_name 100.84.35.192;
        charset     utf-8;
        client_max_body_size 75M;
        root /var/www/mockapp/mockServer;
        location / {
                include      uwsgi_params;
                uwsgi_pass   localhost:5000;  # 指向uwsgi 所应用的内部地址,所有请求将转发给uwsgi 处理
                uwsgi_param UWSGI_PYHOME /var/www/mockapp/mockServer; # 指向虚拟环境目录
                uwsgi_param UWSGI_CHDIR  /var/www/mockapp; # 指向网站根目录
                uwsgi_param UWSGI_SCRIPT main:app; # 指定启动程序
                }
        }
``` 
 
### 6.uwsgi安装配置
``` bash
$ pip install uwsgi
$ sudo vim /var/www/mockapp/mockapp_uwsgi.ini
[uwsgi]
# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:5000
# 指向网站目录
chdir = /var/www/mockapp/mockServer
py-autoreload = 1
# python 启动程序文件
wsgi-file = manage.py
# python 程序内用以启动的 application 变量名
callable = app
# 处理器数
processes = 1
# 线程数
threads = 1
#状态检测地址
stats = 127.0.0.1:9191
```

### 7.用supervisor来管理uwsgi
``` bash
$ pip install supervisor
$ sudo vim /etc/supervisor/conf.d/mockapp_supervisor.conf
[program:mockapp]
# 启动命令入口
command=/usr/local/bin/uwsgi /var/www/mockapp/mockapp_uwsgi.ini
# 命令程序所在目录
directory=/var/www/mockapp/
#运行命令的用户名
user=root
autostart=true
autorestart=true
#日志地址
stdout_logfile=/var/log/uwsgi/uwsgi_supervisor.log
```

### 8.启动uwsgi/nginx
``` bash
$ sudo service supervisor start
$ sudo /etc/init.d/nginx start
```