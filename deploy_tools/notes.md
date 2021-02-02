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
full_clean:模型全字段校验
escape:字符串转义成html协议下的字符串

## TDD思想
* 事不过三，三则重构

## python应用
* class中实现__str__方法，定制str(class)
* @property属性修饰的方法将方法名转化为类成员变量，可直接通过对象名.name访问
## Django高级应用
* 命名视图，在模板文件里使用{% url %}标签指定视图的路由
* 在模型中定义get_absolute_url方法，get_absolute_url方法中指定视图名并传参，redirect(model对象)就可以重定向到model数据对应的路由
* 视图和模板中应用表单，当输入不符合时，form的errors不为空，显示错误提示
* form.save()方法会存储到嵌套类Meta中声明的model中

## model嵌套类Meta的几个应用
* unique_together(),限定模型两个字段不能同时相同
* ordering(),按照指定字段排序
* model A的外键B，可调用B.A_set方法返回指定B字段的所有A
* 反向查询reverse('url_name',args=[a])，可以传参args得到指定url_name的路由

## 使用过的django断言
* assertRedirects(response,'/')

## jenkins使用过程中遇到的问题-解决
* 密钥下载失败-多重试几次并且不要对系统文件做任何的修改
* 默认8080端口被占用-/etc/default/jenkins中更改默认端口
* 提示目录设置错误（status=7）启动失败-jdk找不到，安装jdk后在update-alternatives中注册：update-alternatives --config java
* jenkins构建运行selenium自动化测试时报错Xfvb找不到-在“全局工具配置”中配置Xfvb的name与path