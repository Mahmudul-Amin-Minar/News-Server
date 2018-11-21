from django.db import models


class News(models.Model):
    source_name = models.CharField(max_length=255, blank=True)
    source_slug = models.SlugField(max_length=255, blank=True)
    category_name = models.CharField(max_length=255, blank=True)
    category_slug = models.SlugField(max_length=255, blank=True)
    title = models.CharField(max_length=555)
    link = models.TextField()
    img_link = models.TextField(blank=True, null=True)
    news_date = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added',)

    def __str__(self):
        return str(self.source_name) + '-' + str(self.title)
