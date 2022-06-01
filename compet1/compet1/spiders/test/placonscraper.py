import scrapy
from scrapy_selenium import SeleniumRequest



class PlaconSpider(scrapy.Spider):
    name = "Pla_spider"

    with open("placon-product-sitemap-051222.txt", "rt") as f:
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

            PART_SELECTOR = '/html/body/div[2]/main/article/div/div/main/div[2]/div[2]/*'

           
            yield {
                'Part': response.xpath(PART_SELECTOR).extract(),
                 minPrice = 
                 ["min_price", "orderby", "perpage", "slider__cavity_length","slider__cavity_width","slider__cavity_depth","slider__recycled_bottles_per_case","slider__recycled_bottles_per_unit","product_visibility","product_cat","product_tag","pa_case-count","pa_color","pa_compartments","pa_count","pa_features","pa_lids","pa_material","pa_product-type","pa_size","pa_tray-dimensions","pa_vent","pa_volume"];

              
            }

       # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
       # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
       # if next_page:
       #     yield scrapy.Request(
       #         response.urljoin(next_page),
       #         callback=self.parse
       #     )