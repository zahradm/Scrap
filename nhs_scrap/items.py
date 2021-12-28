# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class pharmacyItem(scrapy.Item):
   
   name = scrapy.Field()
   discription = scrapy.Field()
   info = scrapy.Field()
   guides = scrapy.Field()
   
#class webmdItem(scrapy.Item):
#   name = scrapy.Field()
#   uses = scrapy.Field()
#   side_effects = scrapy.Field()
#   precautions = scrapy.Field()
#   interaction = scrapy.Field()
#   overdose = scrapy.Field()
