import scrapy

from ..items import TutorialItem, TagItem


class TutorialSpider(scrapy.Spider):
    name = "tutorial"
    base_url = "https://realpython.com/"

    def start_requests(self):
        start_urls = [
            "https://realpython.com/",
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tutorials = scrapy.Selector(response).xpath(
            '//div[contains(@class,"main-content")]/div[@class="row"]/div[contains(@class,"mb-5")]'
        )

        item = TutorialItem()
        for tut in tutorials:
            item['url'] = self.base_url + tut.xpath('div/a/@href').re_first('\w.*')
            item['img'] = tut.xpath('.//img/@src').re_first('\w.*')
            item['title'] = tut.xpath('.//h2/text()').re_first('\w.*')
            item['date'] = tut.xpath('.//small[contains(@class,"text-muted")]/text()').re_first('\w.*')

            tags = []
            for tag in tut.xpath('.//a[contains(@class,"badge")]'):
                tag_item = TagItem()
                tag_item['name'] = tag.xpath('text()').re_first('\w.*')
                tag_item['url'] = self.base_url + tag.xpath('@href').re_first('\w.*')
                tags.append(dict(tag_item))

            item['tags'] = tags

            yield item
