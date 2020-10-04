# -*- coding: utf-8 -*-
from ngwdocker import PackageBase
from ngwdocker.base import AppImage


class Package(PackageBase):
    pass


@AppImage.on_apt.handler
def on_apt(event):
    event.package('python3-mapscript' if event.image.context.python3 else 'python-mapscript')


@AppImage.on_package_files.handler
def on_package_files(event):
    if isinstance(event.package, Package):
        event.add(event.package.path / 'mapscript-to-env')


@AppImage.on_virtualenv.handler
def on_virtualenv(event):
    python_bin = '/usr/bin/python3' if event.image.context.python3 else '/usr/bin/python'
    event.before_install(
        '$NGWROOT/package/nextgisweb_mapserver/mapscript-to-env ' +
        '$NGWROOT/env/bin/python ' + python_bin)