import scrapy
#from scrapy.utils.project import get_project_settings
#from selenium import webdriver
#from time import sleep
#from nhs_scrap.items import webmdItem

class WebmdSpider(scrapy.Spider):
    name = 'webmd'
    allowed_domains = ['https://www.webmd.com/drugs/']
    start_urls = ['https://www.webmd.com/drugs/']
    
    def parse(self, response):
        alphas = response.css('.alpha-container a::attr(href)').getall()
        urls = []
        for alpha in alphas:
           urls.append('https://www.webmd.com' +alpha)
        for url in urls:
          
           yield scrapy.Request(url, callback=self.parse_discription)
           
    def parse_discription(self, response):
        x = response.css('.browse-letters squares sub-alpha a::attr(href)').getall()
        print(x)
         #   url = 'https://www.webmd.com' + str(alpha.css('.squares a::attr(href)').extract_first())
            #print(url)
            #title = drug.xpath('.//a[@class="nhsuk-list-panel__link"]/text()').extract_first().replace(' ','')
            #yield scrapy.Request(url, callback=self.parse_discription, meta={'Title' : title, 'URL' : url })
   
        
#response.css('.squares a::attr(href)').getall()    /drugs/2/alpha/a
#response.css('.sub-alpha-square a::attr(href)').getall   /drugs/2/alpha/a/au
#response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "alpha-drug-name", " " ))]/@href').getall()    /drugs/2/drug-22150/baza-protect-cream/details   B+Ba>>>>one  link


#response.css('.monograph-content p::text, .monograph-content a::text').getall()



