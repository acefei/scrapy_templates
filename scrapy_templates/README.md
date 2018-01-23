The directories where to look for templates when creating new projects with startproject command and new spiders with genspider command.

#### Precondition
```
pip install -r requirements.txt
```

Check Splash [install docs](http://splash.readthedocs.io/en/latest/install.html) for more info.


#### Introduction

scrapy_redis_splash: templates for new scrapy project integreted with [scrapy-redis](https://github.com/rmax/scrapy-redis) and [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash/).

scrapy_redis_bloomfilter_splash: templates for new scrapy project integreted with [scrapy-redis-bloomfilter](https://github.com/Python3WebSpider/ScrapyRedisBloomFilter) and [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash/).

spiders: templates for new spiders

#### Usage
```
cd && git clone https://github.com/acefei/scrapy_templates

scrapy startproject myproject -s TEMPLATES_DIR=~/scrapy_templates/scrapy_redis_splash

scrapy startproject myproject -s TEMPLATES_DIR=~/scrapy_templates/scrapy_redis_bloomfilter_splash

scrapy genspider -t <redis_crawl|redis_spider> -s TEMPLATES_DIR=~/scrapy_templates mydomain mydomain.com
```

#### Inspiration

[scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash)

[ScrapyRedisBloomFilter](https://github.com/Python3WebSpider/ScrapyRedisBloomFilter)

[scrapy-proxies](https://github.com/aivarsk/scrapy-proxies)

[scrapy-scrapy-fake-useragent](https://github.com/alecxe/scrapy-fake-useragent)



