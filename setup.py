import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name = 'django-cards',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    license = 'MIT License',
    description = "A simple app to view trello's development board",
    long_description = README,
    url = 'https://github.com/mliudev/trello-card-viewer',
    author = 'Mike Liu',
    author_email = 'mike.liu@mliu.io',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
