import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request

class ChemistSpider(scrapy.Spider):
    name = 'chemist'
    allowed_domains = ['chemist-4-u.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/home/zd/Documents/chromedriver_linux64/chromedriver')
        self.driver.get('https://www.chemist-4-u.com/pharmacy')
        sel = Selector(text = self.driver.page_source)
        #category = sel.xpath('//*[@class="list-sub__item__inner__header"]//text()').extract()
        
        for url in sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-sub__item__inner", " " ))]/@href').extract():
            yield Request(url,callback=self.pars_cat, meta={'URL' : url})
    
    def pars_cat(self, response):
        
        url = response.meta['URL']
        for cat in sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-sub__item__inner", " " ))]/@href').extract():
            driver.find_element_by_xpath('//span[text()="Load next"]').click()
            
                
        #driver.find_element_by_xpath('//span[text()="Load next"]').click()
        #response.xpath('//*[@class="product attribute description"]//text()').extract() discription
        #response.xpath('//*[@class="col-12 col-md-6 mb-3 px-0 px-md-2"]//text()').extract()


        yield {
            
            'd' : url
        }




    