from realpython.models import TutorialItem


class ScrapperPipeline(object):
    def process_item(self, item, spider):
        TutorialItem.objects.create(
            title=item['title'],
            url=item['url'],
            img=item['img'],
        )
        return item
