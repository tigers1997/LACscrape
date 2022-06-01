import scrapy
from scrapy_selenium import SeleniumRequest



class InlineSpider(scrapy.Spider):
    name = "Inline_spider"

    with open("wp-sitemap-posts-product-1.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    #def start_requests(self):
    for url in start_urls:
        SeleniumRequest(
            url=url,
            wait_time = 3,
            screenshot = True,
           # callback = self.parse, 
            dont_filter = True    
            )
    #with open("wp-sitemap-posts-product-1.txt", "rt") as f:
    #    start_urls = [url.strip() for url in f.readlines()]
        #start_urls = ['https://www.inlineplastics.com/catalog/?product_number=&view=10000']

    def parse(self, response):
       # PRODUCT_SELECTOR = '//*[@id="catalog_wrapper"]/div[2]/div[2]/div[1]/div'
       # for response in response.xpath(PRODUCT_SELECTOR):

            PART_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[3]/h1/text()'
            PARTDESC_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[3]/div/text()'
            FAMILY_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[1]/div[1]/div[2]/a/@href'
            COMPART_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[5]/div[2]/div[2]/text()'
            COMPARTSIZE_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[5]/div[3]/div[2]/text()'
            VOLUME_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[5]/div[3]/div[2]/span[1]/text()'
            VOLUMEIDM_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[5]/div[4]/div[2]/span/text()'
            PROD_IDM_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[5]/div[5]/div[2]/span[2]/text()'
            PROD_ODM_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[5]/div[6]/div[2]/span[2]/text()'
            BASELID_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[5]/div[7]/div[2]/text()'
            CASEPACK_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[6]/div[2]/div[2]/text()'
            CASEWEIGHT_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[6]/div[3]/div[2]/span[1]/text()'
            APPLICATION_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[7]/div[1]/div[2]/a/text()'
            MARKETS_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[7]/div[2]/div[2]/a/text()'
            FEATURES_SELECTOR = '/html/body/div[4]/div[3]/div/div/div[3]/div[2]/div[7]/div[3]/div[2]/a/text()'
           
            yield {
                'Part': response.xpath(PART_SELECTOR).extract_first(),
                'PartDesc': response.xpath(PARTDESC_SELECTOR).extract_first(),
                'Family': response.xpath(FAMILY_SELECTOR).extract_first(),
                'Compart': response.xpath(COMPART_SELECTOR).extract_first(),
                'CompartSize': response.xpath(COMPARTSIZE_SELECTOR).extract_first(),
                'Volume': response.xpath(VOLUME_SELECTOR).extract_first(),
                'Volume2': response.xpath(VOLUMEIDM_SELECTOR).extract(),
                'ProdIDM': response.xpath(PROD_IDM_SELECTOR).extract(),
                'ProdODM': response.xpath(PROD_ODM_SELECTOR).extract(),
                'BASELID': response.xpath(BASELID_SELECTOR).extract_first(),
                'CasePack': response.xpath(CASEPACK_SELECTOR).extract_first(),
                'CaseWeight': response.xpath(CASEWEIGHT_SELECTOR).extract_first(),
                'Application': response.xpath(APPLICATION_SELECTOR).extract(),
                'Markets': response.xpath(MARKETS_SELECTOR).extract(),
                'Features': response.xpath(FEATURES_SELECTOR).extract(),                
            }

       # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
       # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
       # if next_page:
       #     yield scrapy.Request(
       #         response.urljoin(next_page),
       #         callback=self.parse
       #     )