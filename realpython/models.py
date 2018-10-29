from django.db import models


class TutorialItem(models.Model):
    title = models.TextField()
    url = models.URLField()
    img = models.URLField()

    def __str__(self): return self.title
