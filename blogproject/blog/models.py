from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

from django.urls import reverse

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):   #分类
    name = models.CharField(max_length=100) # CharField 指定了 name 的数据类型， max_length 指定其最大长度

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):    #标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70) ## 文章标题

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200,blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)

    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    #将urls里传递的pk接入数据库的id，以返回文章
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def get_absolute_ursl(self):
        return reverse('blog:post_delete',kwargs={'pk':self.pk})

    #increase_views 方法首先将自身对应的 views 字段的值 +1（此时数据库中的值还没变），
    # 然后调用 save 方法将更改后的值保存到数据库。
    # 注意这里使用了 update_fields 参数来告诉 Django 只更新数据库中 views 字段的值，以提高效率
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
