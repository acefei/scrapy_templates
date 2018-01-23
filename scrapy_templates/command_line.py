import scrapy_templates
import os,re
from scrapy import cmdline
from glob import glob

class ScrapyRun(object):
    def __init__(self):
        self._proj_list = list()
        self._tmpl_path = scrapy_templates.__path__[0]

    def show_tmpls(self):
        self._proj_list = glob('{0}/scrapy*'.format(self._tmpl_path))
        print "\nscrapy startproject templates\n"
        for i, proj in enumerate(self._proj_list):
            print i+1, os.path.basename(proj)

    def startproject(self):
        choice = int(raw_input("choice the template num: "))
        assert 0 < choice < len(self._proj_list), 'Selection is out of range.'

        proj_name = raw_input("specify the project name: ")
        assert re.match(r'^[a-zA-Z]\w{,15}', proj_name), 'Invalid project name.'

        tmpl_path = self._proj_list[choice-1]
        cmd_str = "scrapy startproject {proj_name} -s TEMPLATES_DIR={tmpl_path}"
        cmd = cmd_str.format(**locals())
        # print cmd
        cmdline.execute(cmd.split())


def main():
    sr = ScrapyRun()
    sr.show_tmpls()
    sr.startproject()
