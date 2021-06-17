import pathlib
from setuptools import setup,find_packages

setup(
	name='python-mp3',
	version='0.0.1',
	author='CCC Jugendgruppe Göttingen',
	url='https://github.com/CCC-Jugendgruppe/python_mp3',
	#py_modules=[],
	packages=find_packages(include=['python_mp3','python_mp3.*']),
	install_requires=[
		'pyqt6',
		'mp3_tagger'
	],
	entry_points={
		'console_scripts': ['python-mp3=python_mp3.main:main']
	}
)
