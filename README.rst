scrapy_templates
================

Templates for creating new projects with startproject command and new spiders with genspider command.

Installation
------------
::

  pip install git+https://github.com/acefei/scrapy_templates.git
  # or
  pip install https://github.com/acefei/scrapy_templates/archive/master.zip
  # update
  pip install --upgrade git+https://github.com/acefei/scrapy_templates.git


Usage
-----
::  

    $ scrapy-startproject

    scrapy startproject templates
    1 scrapy
    2 scrapy_redis_bloomfilter_splash
    3 scrapy_redis_splash
    choice the template: 1
    specify the project name: trail
    New Scrapy project 'trail', using template directory '/usr/lib/python2.7/site-packages/scrapy_templates/scrapy/project', created in:
        /home/acefei/trail

    You can start your first spider with:
        cd trail
        scrapy genspider example example.com

    You can also use 'scrapy-genspider' to generate new spider with custom template.

    $ cd trail
    $ scrapy-genspider

    scrapy genspider templates
    1 basic
    2 crawl
    3 csvfeed
    4 xmlfeed
    5 redis_crawl
    6 redis_spider
    choice the template: 5
    specify spider name: trail_spider
    Created spider 'trail_spider' using template 'redis_crawl' in module:
      trial.spiders.trail_spider

Authors
-------

`scrapy_templates` was written by `acefei <acefei@163.com>`_.
