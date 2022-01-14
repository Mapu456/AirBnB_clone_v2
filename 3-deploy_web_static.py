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
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers,
    using the function do_deploy"""
    if os.path.isfile(archive_path) is False:
        return False
    else:
        file_name = archive_path[9:]
        name_dir = "/data/web_static/releases/" + file_name[:-4]
        path_to_store = "/tmp/" + file_name

        put(archive_path, "/tmp/")

        run("sudo mkdir -p {}".format(name_dir))
        run("sudo tar -xzf {} -C {}".format(path_to_store, name_dir))
        run("sudo rm {}".format(path_to_store))
        run("sudo mv {}/web_static/* {}".format(name_dir,
                                                name_dir))
        run("sudo rm -rf {}/web_static".format(name_dir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current"
            .format(name_dir))
        print("New version deployed!")

        return True


def deploy():
    """Fabric script that creates and distributes an archive
    to your web servers, using the function deploy"""

    tgz_file = do_pack()
    if tgz_file is None:
        return False
    do_deploy_value = do_deploy(tgz_file)
    return do_deploy_value