from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length=250)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s'% self.title


def get_absolute_url(self):
    return reverse('myblog.views.post', args=[self.slug])
