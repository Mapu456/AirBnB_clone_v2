#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder function do_pack."""

from fabric.api import *
from datetime import datetime

env.hosts = ['35.243.245.64', '18.234.66.163']
env.user = "ubuntu"


def do_pack():
    """Fabric script that generates a .tgz archive from the contents of
    the web_static folder function do_pack"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_file = "versions/web_static_{}.tgz".format(date)
    execute_tar = local("tar -cvzf {} web_static".format(tgz_file))

    if execute_tar.succeeded:
        return tgz_file
    else:
        return None


def do_deploy(archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp/')

        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """Fabric script that creates and distributes an archive
    to your web servers, using the function deploy"""

    tgz_file = do_pack()
    if tgz_file is None:
        return False
    do_deploy_value = do_deploy(tgz_file)
    return do_deploy_value
