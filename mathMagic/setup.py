import sys
from cx_Freeze import setup, Executable

setup(
    name="MathMagique",
    version="1.0",
    description="Description de votre application",
    executables=[Executable("MathMagique.py", base=None)],
)