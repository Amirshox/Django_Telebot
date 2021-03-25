from django.db import models


class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='slider_img/')
    cms_title = models.CharField(max_length=100, verbose_name='Title')
    cms_text = models.TextField(verbose_name='Text')
    cms_css = models.CharField(max_length=100, null=True, default='-', verbose_name='CSS class')

    def __str__(self):
        return self.cms_text

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'
