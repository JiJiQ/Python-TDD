建站部署
===========
## 需要的包：

* nginx
* Python 3.6
* virtualenv+pip
* git

以ubuntu为例:

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python36 python3.6-venv

##nginx虚拟主机
* 参考nginx.template.conf
* 把SITENAME替换成域名 例如staging.my-domain.com

##Systemd服务
* 参考gunicorn-systemd.template.service