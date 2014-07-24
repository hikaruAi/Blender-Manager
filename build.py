import sys

from cx_Freeze import setup, Executable
includes = ["re"]
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "Blender Console Manager",
        version = "3.0",
        description = "Blender console manager and Batch renderer",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable("BatchRender.pyw", base = base,icon="icono.ico")])

