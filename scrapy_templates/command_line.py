import scrapy_templates
import os,re
from scrapy import cmdline
from glob import glob
import subprocess

class ScrapyRun(object):
    def __init__(self):
        self._proj_list = list()
        self._tmpl_path = scrapy_templates.__path__[0]

    def show_proj_tmpls(self):
        self._proj_list = glob('{0}/scrapy*'.format(self._tmpl_path))
        print "\nscrapy startproject templates"
        for i, proj in enumerate(self._proj_list):
            print i+1, os.path.basename(proj)

    def startproject(self):
        choice = int(raw_input("choice the template: "))
        assert 0 < choice <= len(self._proj_list), 'Selection is out of range.'
        tmpl_path = self._proj_list[choice-1]

        proj_name = raw_input("specify the project name: ")
        assert re.match(r'^[a-zA-Z]\w{,15}', proj_name), 'Invalid project name.'

        cmd_str = "scrapy startproject {proj_name} -s TEMPLATES_DIR={tmpl_path}"
        cmd = cmd_str.format(**locals())
        # print cmd
        try:
            cmdline.execute(cmd.split())
        except SystemExit:
            print "\nYou can also use scrapy-genspider to generate new spider with custom template."

    def show_spider_tmpls(self):
        print "\nscrapy genspider templates"
        # original spider templates
        output = subprocess.check_output("scrapy genspider -l".split())
        spider_tmpls = [l.strip() for l in output.split("\n") if l.startswith(' ')]

        # extentional spider templates
        tmpl_path = scrapy_templates.__path__[0]
        cmd_str = "scrapy genspider -l -s TEMPLATES_DIR={tmpl_path}"
        cmd = cmd_str.format(**locals())
        output = subprocess.check_output(cmd.split())
        spider_tmpls_new = [l.strip() for l in output.split("\n") if l.startswith(' ')]
        spider_tmpls.extend(spider_tmpls_new)

        self._spider_tmpls = spider_tmpls
        for i, t in enumerate(spider_tmpls):
            print i+1, t

    def genspider(self):
        choice = int(raw_input("choice the template: "))
        assert 0 < choice <= len(self._spider_tmpls), 'Selection is out of range.'
        tmpl = self._spider_tmpls[choice-1]

        spider_name = raw_input("specify spider name: ")
        assert re.match(r'^[a-zA-Z]\w{,15}', spider_name), 'Invalid project name.'

        tmpl_path = scrapy_templates.__path__[0]
        cmd_str = "scrapy genspider {spider_name} {spider_name} -t {tmpl} -s TEMPLATES_DIR={tmpl_path}"
        cmd = cmd_str.format(**locals())
        #print cmd
        cmdline.execute(cmd.split())

def startproj():
    sr = ScrapyRun()
    sr.show_proj_tmpls()
    sr.startproject()

def genspider():
    sr = ScrapyRun()
    sr.show_spider_tmpls()
    sr.genspider()
