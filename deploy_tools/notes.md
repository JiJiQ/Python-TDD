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

##自动部署
* 构建fabric脚本完成站点目录创建->获取最新代码->更新django的设置文件、站点数据库，创建站点虚拟环境，收集站点静态文件，创建nginx虚拟站点配置和systemd服务
* 幂等性：nginx站点配置模板和gunicorn-systemd配置模板文件中的站点名称应为SITENAME，使用fabric脚本中替换为具体站点名称
##问题记录
fatal: Could not parse object:commitid(本地代码未提交导致)
