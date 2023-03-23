from django.db import models
from django.contrib.auth.models import User


# the Block and Memo class contains the essential fields and behaviors of the data we use

class Block(models.Model):
    # the Block model will be used to contain Memo instance (like a folder)
    block_title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('creation date', auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.block_title


class Memo(models.Model):
    # the Memo model will be used to contain information about its block parent it also contains a boolean field to
    # track its progress
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    memo_title = models.CharField(max_length=255)
    memo_text = models.TextField()
    pub_date = models.DateTimeField('creation date', auto_now_add=True)
    accomplish = models.BooleanField(default=False)

    class Meta:
        ordering = ('memo_title',)

    def __str__(self):
        return self.memo_title
