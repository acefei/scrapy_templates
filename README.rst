scrapy_templates
================

Templates for creating new projects with startproject command and new spiders with genspider command.

Usage
-----
::  

  $ scrapy-startproject

    scrapy startproject templates

    1 scrapy
    2 scrapy_redis_bloomfilter_splash
    3 scrapy_redis_splash
    choice the template num: 1
    specify the project name: trail
    New Scrapy project 'trail', using template directory '/usr/lib/python2.7/site-packages/scrapy_templates-0.1.0-py2.7.egg/scrapy_templates/scrapy/project', created in:
        /tmp/trail

    You can start your first spider with:
        cd trail
        scrapy genspider example example.com


Installation
------------
::

  pip install git+https://github.com/acefei/scrapy_templates.git
  # or
  pip install https://github.com/acefei/scrapy_templates/archive/master.zip

Licence
-------

Authors
-------

`scrapy_templates` was written by `acefei <acefei@163.com>`_.
