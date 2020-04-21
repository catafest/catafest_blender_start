# -*- coding:utf-8 -*-
#
# catafest_addon_start.py
#
# This is a Blender script that uses procedural generation to create
# a catafest 3D mesh from a random seed. Tested with Blender 2.77a.
#
# catalinfest@gmail.com
# https://github.com/catafest/catafest_blender_start
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

#import all python modules 
import sys
import os
import os.path
import bpy
import bmesh
import datetime
from math import sqrt, radians, pi, cos, sin
from mathutils import Vector, Matrix
from random import random, seed, uniform, randint, randrange
from enum import IntEnum
from colorsys import hls_to_rgb

DIR = os.path.dirname(os.path.abspath(__file__))

# get resource path
def resource_path(*path_components):
    return os.path.join(DIR, *path_components)

# Deletes all existing catafest_addon_start and unused materials from the scene
def reset_scene():
    for item in bpy.data.objects:
        item.select = item.name.startswith('catafest_addon_start')
    bpy.ops.object.delete()
    for material in bpy.data.materials:
        if not material.users:
            bpy.data.materials.remove(material)
    for texture in bpy.data.textures:
        if not texture.users:
            bpy.data.textures.remove(texture)


if __name__ == "__main__":
    
    reset_scene()
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            ctx = bpy.context.copy()
            ctx['area'] = area
            ctx['region'] = area.regions[-1]
            bpy.ops.view3d.view_selected(ctx)
    
    scene = bpy.data.scenes["Scene"]
    scene.render.resolution_x = res_x
    scene.render.resolution_y = res_y
    scene.camera.rotation_mode = 'XYZ'
    scene.camera.data.angle = radians(fov)
    frame = 0
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
