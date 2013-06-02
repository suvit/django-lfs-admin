# -*- coding: utf-8 -
#
# This file is part of django-lfs-admin released under the MIT license.
# See the LICENSE for more information.

from setuptools import setup, find_packages

setup(
    name='django-lfs-admin',
    version=__import__('lfs_admin').VERSION,
    description='Intergation of django-lfs and django.contrib.admin',
    author='Victor Safronovich',
    author_email='',
    license='MIT',
    url='http://github.com/suvit/django-lfs-admin',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=['django-privatesite',
                      'django-tinymce',
                     ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Web Environment',
        'Topic :: Software Development',
    ]
)
