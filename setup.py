from setuptools import setup, find_packages

setup(
    name='django-debug-toolbar-request-history',
    version='0.1.2',
    description='Request History Panel for Django Debug Toolbar',
    author='David Sutherland',
    author_email='djsutho@gmail.com',
    license='BSD',
    packages=find_packages(exclude=('tests', 'example')),
    include_package_data=True,
    install_requires=['django-debug-toolbar>=2.0'],
    url='https://github.com/djsutho/django-debug-toolbar-request-history',
    download_url='https://github.com/djsutho/django-debug-toolbar-request-history/tarball/0.1.2',
    keywords=['django', 'debug', 'ajax'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)