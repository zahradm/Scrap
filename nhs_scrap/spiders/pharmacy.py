import scrapy
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from time import sleep
from nhs_scrap.items import pharmacyItem



class PharmacySpider(scrapy.Spider):
    name = 'pharmacy'
    
    def start_requests(self):
        settings = get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get('https://www.chemist-4-u.com/pharmacy/')
            
       
        
        
        
        while True:
            next = driver.find_element_by_xpath('//span[text()="Load next"]')

            try:
                driver.execute_script("arguments[0].click();", next)
                sleep(5)

                
            except:
                break
            

    

                
        link_elements = driver.find_elements_by_xpath(
            '//*[@class="product-item-link itc-font--cyan-dark"]')

        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)

        driver.quit()

    def parse(self, response, **kwargs):
        item = pharmacyItem(
            name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]//text()').extract(),
            discription= [dis.strip().replace('\xa0',' ') for dis in response.css('ul:nth-child(25) li::text , #description li~ li+ li::text , ul:nth-child(6) li::text , #description h3::text , h2::text , p::text').getall()],
            info = [inf.strip().replace(' ','') for inf in response.xpath('//*[@class="col-12 col-md-6 mb-3 px-0 px-md-2"]//text()').extract()],
            guides = [guid.strip().replace('\n','') for guid in response.xpath('//*[@class="itl-tabs__content__inner itl-tabs__content__inner--standard"]//text()').extract()],
            


        )

        yield item
