from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ircengg/__init__.py
from ircengg import __version__ as version

setup(
	name="ircengg",
	version=version,
	description="Customization for attendance and other.",
	author="ircengg",
	author_email="ircengg@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
