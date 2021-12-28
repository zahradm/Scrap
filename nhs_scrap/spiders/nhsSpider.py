import scrapy


class NhsspiderSpider(scrapy.Spider):
    name = 'nhsSpider'
    allowed_domains = ['www.nhs.uk']
    start_urls = ['https://www.nhs.uk/medicines/']

    def parse(self, response):
        drugs = response.xpath('//li[@class="nhsuk-list-panel__item"]')
        for drug in drugs:
            url = 'https://www.nhs.uk' + drug.xpath('.//a[@class="nhsuk-list-panel__link"]/@href').extract_first()
            title = drug.xpath('.//a[@class="nhsuk-list-panel__link"]/text()').extract_first().replace(' ','')
            yield scrapy.Request(url, callback=self.parse_discription, meta={'Title' : title, 'URL' : url })
                 
            
    def parse_discription(self, response):
        title = response.meta['Title']
        url = response.meta['URL']
        contents = response.xpath('.//*[@class="nhsuk-body-s"]/li/text()').extract()
        text = response.xpath('.//*[@class="block-richtext"]//text()').extract()
        question = response.xpath('//*[@class="block-question"]//text()').extract()


        yield {
            'Title' : title,
            'URL' : url,
            'Content' : text,
            'Common_ question' : question
        }
