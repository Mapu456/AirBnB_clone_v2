#!/usr/bin/env bash
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder function do_pack."""

from fabric.api import local
from datetime import datetime


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
