from fabric.contrib.files import append,exists,sed
from fabric.api import env,local,run

import random

REPO_URL='https://github.com/JiJiQ/Python-TDD.git'
def deploy():
    site_folder=f'/home/work/{env.host}'
    source_folder=site_folder+'/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder,env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)
    _nginx_and_systemd(source_folder)
def _create_directory_structure_if_necessary(site_folder):
    for subfolder in('database','static','virtualenv','source'):
        run(f'mkdir -p {site_folder}/{subfolder}')
def _get_latest_source(source_folder):
    if exists(source_folder+'/.git'):
        #可以热改动
        run(f'cd {source_folder} && git fetch')
    else:
        run(f'git clone {REPO_URL} {source_folder}')
    #获取本地最近一次提交
    current_commit=local('git log -n 1 --format=%H',capture=True)
    run(f'cd {source_folder} '
        f'&& git checkout master '
        f'&& git reset --hard {current_commit}')
def _update_settings(source_folder,site_name):
    settings_path=source_folder+'/TDD/settings.py'
    sed(settings_path,'DEBUG = True','DEBUG = False')
    sed(settings_path,'ALLOWED_HOSTS=.+$',f'ALLOWED_HOSTS=["{site_name}"]')
    secret_ksy_file=source_folder+'/TDD/secret_key.py'
    if not exists(secret_ksy_file):
        chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key=''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_ksy_file,f'SECRET_KEY="{key}"')
    append(settings_path,'\n'+'from .secret_key import SECRET_KEY')
def _update_virtualenv(source_folder):
    virtualenv_folder=source_folder+'/../virtualenv'
    if not exists(virtualenv_folder+'/bin/pip'):
        run(f'python -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements.txt')
def _update_static_files(source_folder):
    run(f'cd {source_folder}'
        ' && ../virtualenv/bin/python manage.py collectstatic --noinput')
def _update_database(source_folder):
    run(
        f'cd {source_folder}'
        ' && ../virtualenv/bin/python manage.py migrate --noinput'
    )
def _nginx_and_systemd(source_folder):
    nginx_available_path='/etc/nginx/sites-available'
    nginx_enable_path='/etc/nginx/sites-enabled'
    systemd_path='/etc/systemd/system/'
    if exists(f'{source_folder}/deploy_tools'):
        #文件拷贝
        run(
            f'cd {source_folder}/deploy_tools '
            f'&& cp nginx.template.conf {nginx_available_path}/{env.host} '
            f'&& cp gunicorn-systemd.template.service {systemd_path}/gunicorn-{env.host}.service'
        )

        #站点内容更新
        run(f'cd {nginx_available_path}')
        sed(f'{nginx_available_path}/{env.host}','SITENAME',f'{env.host}')

        run(f'cd {systemd_path}')
        sed(f'{systemd_path}/gunicorn-{env.host}.service','SITENAME',f'{env.host}')

        #nginx虚拟站点激活
        ln_path=f'{nginx_enable_path}/{env.host}'
        #软链存在时再次创建软链会执行失败中断部署
        if not exists(ln_path):
            run(f'ln -s {nginx_available_path}/{env.host} {ln_path} ')

        #启动nginx和gunicorn
        run('systemctl daemon-reload')
        run('systemctl reload nginx')
        run(f'systemctl enable gunicorn-{env.host}')
        run(f'systemctl start gunicorn-{env.host}')
