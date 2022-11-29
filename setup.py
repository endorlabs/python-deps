from setuptools import setup

version = '1.2.dev0'
shortdesc = "Building data structures as node trees"

setup(
    name='endorpysetup',
    version=version,
    description=shortdesc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='endor tree fullmapping dict demo',
    author='Endor labs Contributors',
    author_email='all@endor.ai',
    url='http://github.com/endorlabs/python-deps',
    license='Simplified BSD',
    install_requires=[
        'odict>=1.9.0',
        'plumber>=1.5',
        'setuptools',
        'zope.component==5.0.1',
        'zope.deferredimport',
    ],
    test_suite='endor.tests.test_suite'
)