#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder function do_pack."""

from fabric.api import *
from datetime import datetime
import os


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


env.hosts = ['35.243.245.64', '18.234.66.163']


def do_deploy(archive_path):
    name_dir = archive_path[9:-4]
    if os.path.exists(archive_path):
        put(archive_path, '/tmp')
        run("sudo mkdir -p /data/web_static/releases/{}".format(name_dir))
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
            format(name_dir, name_dir))
        run("sudo rm /tmp/{}.tgz".format(name_dir))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{} /".format(name_dir, name_dir))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(name_dir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name_dir))
        print("New version deployed!")
        return True
    else:
        return False
