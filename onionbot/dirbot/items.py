from scrapy.item import Field, Item


class CrawledWebsiteItem(Item):

    domain = Field()
    url = Field()
    tor2web_url = Field()
    title = Field()
    text = Field()
    date_inserted = Field()
    id = Field()
    django_ct = Field()
    django_id = Field()