from django.db import models

# Create your models here.
class Sql(models.Model):
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)
    #文章的标题
    title = models.TextField()
    #文章的摘要
    brief_title = models.TextField()
    #文章的发布时间
    publish_date = models.DateTimeField(auto_now=True)
    #文章的内容
    content = models.TextField()