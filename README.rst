xstats.padjust
==============

``padjust`` is a Python_ library, part of the ``xstats`` toolkit, which can be used to correct p-values for multiple testing.

- **Contact** Aurelien Mazurie <ajmazurie@oenone.net>
- **Keywords** Python, Statistics, Multiple testing

Getting started
---------------

- Download the latest version of the library from http://github.com/ajmazurie/xstats.padjust/downloads
- Unzip the downloaded file, and ``cd`` into the resulting directory
- Run ``python setup.py install``. Alternatively, you can package the library by typing ``python setup.py bdist``, which will result in the creation of a file dist/xstats.padjust-xxx.tar.gz, with 'xxx' being the version number and the name of your platform. Installing the library is then as simple as ``easy_install dist/xstats.padjust-xxx.tar.gz`` (see the setuptools `documentation <http://pypi.python.org/pypi/setuptools>`_)

From then you only have to import ``padjust`` to use the library::

	import xstats.padjust

.. _Python: http://www.python.org/
