# Copyright 2012, Sean B. Palmer
# Code at http://inamidst.com/duxlot/
# Apache License 2.0

# python3 setup.py sdist --formats=bztar

import os.path
import sys
import distutils.core

import api

if sys.version_info < (3, 2):
    print("Error: Requires python 3.2 or later", file=sys.stderr)
    sys.exit(1)

with open(os.path.join("data", "version"), encoding="ascii") as f:
    version = f.read()
    version = version.rstrip()

README = r"""
Duxlot_ is a new IRC bot created in 2012 by `Sean B. Palmer`_, the maker of the
popular Phenny_. Features include a fast multiprocess based architecture,
modularity, and ease of use. Duxlot has no dependencies except Python3, and will
even work without having to be installed as as package.

.. _Duxlot: http://inamidst.com/duxlot/
.. _Sean B. Palmer: http://inamidst.com/sbp/
.. _Phenny: http://inamidst.com/phenny/

Source on Github, `@sbp/duxlot`_.

.. _@sbp/duxlot: https://github.com/sbp/duxlot

    **WARNING:** This is an early, pre-release alpha version of Duxlot. The API
    and features may change wildly, and the bot may not be stable.

Install
---------

You may use **either** of these methods:

*	Download the latest source.

	Unpack it and enter ``duxlot-%s/``

	**Optionally** install using::

		python3 setup.py install

*	Install using pip_::

		pip install duxlot

.. _pip: http://pypi.python.org/pypi/pip

**Optionally** use virtualenv_ for either of these methods.

.. _virtualenv: http://www.virtualenv.org/en/latest/index.html#installation

You can now use the ``duxlot`` script—either the one in the package that you downloaded, or the one that should be on your ``$PATH`` from installation.

""" % version

# http://stackoverflow.com/questions/4384796
# http://packages.python.org/distribute/

distutils.core.setup(
    name="duxlot",
    version=version,
    author="Sean B. Palmer",
    url="http://inamidst.com/duxlot/",
    description="IRC bot and data suite, by the maker of phenny",
    long_description=README,
    packages=["duxlot"],
    package_dir={"duxlot": ""},
    package_data={"duxlot": ["README.rst", "data/*.*", "standard/*.*"]},
    scripts=["duxlot"],
    platforms=[
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX"
    ],
    license="License :: OSI Approved :: Apache Software License"
)
