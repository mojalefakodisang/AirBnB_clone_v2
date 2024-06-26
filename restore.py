"""Restores the servers"""
import os
from fabric.api import *

env.hosts = [
        '34.239.250.176',
        '52.201.211.251'
        ]

def put_file(file):
    put(file, ".")

def execute_file(file):
    sudo(f"chmod +x {file}")
    sudo(f"./{file}")

def restore_local():
    local("rm -rf versions")

def restore_server():
    run("rm -rf /data/web_static/releases")

def restore():
    restore_local()
    restore_server()
