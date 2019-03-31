#!/usr/bin/env python

# distutils setup script for fcrypt.
#
# Copyright (C) 2000, 2001, 2004  Carey Evans  <careye@spamcop.net>

import sys
from distutils.core import setup

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup( name = 'fcrypt',
       version = '1.3.1',
       description = 'Unix password crypt function.',
       author = 'Carey Evans',
       author_email = 'careye@spamcop.net',
       url = 'http://home.clear.net.nz/pages/c.evans/sw/#python-fcrypt',
       download_url = 'http://home.clear.net.nz/pages/c.evans/sw/fcrypt-1.3.tar.gz',
       license = 'BSD',
       long_description = """\
A pure Python implementation of the Unix DES password crypt function,
based on Eric Young's fcrypt.c.  It works with any version of Python
from version 1.5 or higher, and because it's pure Python it doesn't
need a C compiler to install it.""",
       classifiers = [
         'Development Status :: 5 - Production/Stable',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: BSD License',
         'Natural Language :: English',
         'Programming Language :: Python',
         'Topic :: Security' ],

       py_modules = ['fcrypt'] )
