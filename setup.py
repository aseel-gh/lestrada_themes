from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lestrada_themes/__init__.py
from lestrada_themes import __version__ as version

setup(
	name="lestrada_themes",
	version=version,
	description="Erpnext 14",
	author="Aseel",
	author_email="aseel.gharbia@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
