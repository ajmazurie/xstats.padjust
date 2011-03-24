#!/usr/bin/env python

# see http://www.sourceweaver.com/posts/python-namespace-packages
try:
	from setuptools import setup, Extension, find_packages
except ImportError:
	from ez_setup import use_setuptools
	use_setuptools()
	from setuptools import setup, Extension, find_packages

setup(
	name = "MultipleTesting",
	version = "1.0",
	description = "P-values correction for multiple testing",
	long_description = open("README.rst").read(),
	url = "http://github.com/ajmazurie/xstats.mtesting",
	license = open("LICENSE.txt").read(),

	author = "Aurelien Mazurie",
	author_email = "ajmazurie@oenone.net",

	namespace_packages = ["xstats"],
	packages = find_packages("lib"),
	package_dir = {'': "lib"},
)