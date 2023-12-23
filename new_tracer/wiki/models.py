from django.db import models
from project.models import Project


class Wiki(models.Model):
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='内容')

    depth = models.IntegerField(verbose_name='深度', default=1)

    # 子关联
    parent = models.ForeignKey("self", verbose_name='父文章', null=True, blank=True, related_name='children',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
