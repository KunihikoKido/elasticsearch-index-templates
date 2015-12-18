# coding=utf-8
import os
from fabric.api import local, run, put
from fabric.api import env
from fabric.colors import blue, cyan, green, magenta, red, white, yellow
from fabric.contrib import console


TEMPLATE_FILES = local("ls templates/*.json", capture=True).split()


def deploy(host="localhost:9200"):
    """Deploy index templates to elasticsearch"""
    for filename in TEMPLATE_FILES:
        template_name, ext = os.path.splitext(os.path.basename(filename))
        result =local("curl -XPUT {host}/_template/{template_name} --data-binary @{filename}".format(
            host=host, template_name=template_name, filename=filename
        ), capture=True)

        if "error" in result:
            print(red(result))

def delete(host="localhost:9200"):
    """Delete index templates from elasticsearch"""
    for filename in TEMPLATE_FILES:
        template_name, ext = os.path.splitext(os.path.basename(filename))
        result = local("curl -XDELETE {host}/_template/{template_name}".format(
            host=host, template_name=template_name
        ), capture=True)

        if "error" in result:
            print(red(result))
