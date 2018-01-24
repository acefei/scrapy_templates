import setuptools

setuptools.setup(
    name="scrapy_templates",
    version="0.1.0",
    url="https://github.com/acefei/scrapy_templates",

    author="acefei",
    author_email="acefei@163.com",

    description="Templates for creating new projects with startproject command and new spiders with genspider command.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(exclude=('tests')),
    include_package_data=True,

    entry_points = {
        'console_scripts': [
            'scrapy-startproject=scrapy_templates.command_line:startproj',
            'scrapy-genspider=scrapy_templates.command_line:genspider',
        ],
    },

    install_requires=[
        'scrapy-redis',
        'scrapy-splash',
        'scrapy-random-useragent',
        'scrapy-redis-bloomfilter',
    ],

    classifiers=[
        'Programming Language :: Python',
    ],
)
