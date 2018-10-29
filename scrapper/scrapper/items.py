import scrapy


class TutorialItem(scrapy.Item):
    url = scrapy.Field()
    img = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    tags = scrapy.Field()


class TagItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
