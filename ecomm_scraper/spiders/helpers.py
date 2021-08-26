import os
import json

class SpiderHelper:
    def get_start_url(self, spider_name):
        start_urls = None
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, "urls/%s.txt" % spider_name)
        with open(abs_file_path) as f:
            start_urls  = [line.strip() for line in f.readlines()]
        
        return start_urls

    def get_item_to_scrap(self, config_file):
        
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, f'urls/{config_file}.json')
        file = open(abs_file_path,)
        data = json.load(file)
        
        return data