
I. Building a package.

1. Create directory 'project'.

2. In that directory, create directory 'aps2' and copy modules there, like follows:

$ ls aps2

aps.py  apsapi.py  runtime.py  uLogging.py

3. Create __init__.py module in aps directory, containing __all__ array, listing the modules:

$ cat aps2/__init__.py 
__all__ = ["aps2"]

4. In directory 'project', create setup.py, with the following context:

$ cat setup.py 
#!/usr/bin/env python

from distutils.core import setup
setup(
    name = "aps-python-runtime",
    packages = ["aps2"],
    version = "2.0-5",
    description = "Runtime package for aps 2.x applicaitons in Python"
)

5. Now, we can install package using the following command:

python setup.py install

6. Alternatively, create a tar archive and install it using pip:

tar czvf aps.tgz setup.py  aps2
pip install aps.tgz

Installing pip utility:

1. wget https://bootstrap.pypa.io/get-pip.py
2. python get-pip.py

II. Setup application

1. Install mod_wsgi:

yum install mod_wsgi

2. Create application directory, for example:

