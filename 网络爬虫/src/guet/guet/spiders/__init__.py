# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from guet.spiders.jy import JySpider

def __init__(self, date,  *args, **kwargs):
    super(JySpider, self).__init__(*args, **kwargs)
    self.date = date