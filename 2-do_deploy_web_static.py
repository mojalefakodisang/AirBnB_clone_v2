#!/usr/bin/python3
"""
Module that archives files
"""
import os
from fabric.api import *
from datetime import datetime
env.hosts = ["34.239.250.176", "52.201.211.251"]


def do_deploy(archive_path):
    """Deploys the web static"""
    if not os.path.exists(archive_path):
        return False

    basename = os.path.basename(archive_path)
    tmp_archive_path = f"/tmp/{basename}"

    try:
        put(archive_path, tmp_archive_path)
        x_archive = "/data/web_static/releases/{}".format(
                os.path.splitext(basename)[0]
        )
        run(f"mkdir -p {x_archive}")
        run("tar -xzf {} -C {} --strip-components=1".format(
            tmp_archive_path, x_archive
        ))
        run("rm -f {}".format(tmp_archive_path))
        symlink = "/data/web_static/current"
        run(f"rm -rf {symlink}")
        run(f"ln -s {x_archive}/ {symlink}")
    except Exception:
        return False
    return True
