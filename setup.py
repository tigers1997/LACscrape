# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = compet1.settings']},
    package_data={
        'project': ['compet1/spiders/*.txt']
    },
)
