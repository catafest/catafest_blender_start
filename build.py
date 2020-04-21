#!/usr/bin/env python

from os.path import abspath, dirname, join as pjoin
import zipfile

SRC_DIR = dirname(abspath(__file__))

with zipfile.ZipFile('catafest_addon_start.zip', 'w', zipfile.ZIP_DEFLATED) as arch:
    for filename in [
            '__init__.py',
            'catafest_addon_start.py',
            'textures/texture_001.png']:
        arch.write(pjoin(SRC_DIR, filename), 'add_mesh_catafest_blender_start/'+filename)

print('created file: catafest_addon_start.zip')
