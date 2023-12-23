from django.db import models
from django.contrib.auth import get_user_model
from project.models import Project

User = get_user_model()


class FileRepository(models.Model):
    """ 文件库 """
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    file_type_choices = (
        (1, '文件'),
        (2, '文件夹')
    )
    file_type = models.SmallIntegerField(verbose_name='类型', choices=file_type_choices)
    name = models.CharField(verbose_name='文件夹名称', max_length=32, help_text="文件/文件夹名")
    key = models.CharField(verbose_name='文件储存在COS中的KEY', max_length=128, null=True, blank=True)

    # int类型最大表示的数据
    file_size = models.BigIntegerField(verbose_name='文件大小', null=True, blank=True, help_text='字节')
    # https://桶.cos.ap-chengdu/....
    file_path = models.FileField(upload_to='data/uploads', verbose_name='文件路径', max_length=255, null=True)

    parent = models.ForeignKey('self', verbose_name='父级目录', related_name='child', null=True, blank=True,
                               on_delete=models.CASCADE)

    update_user = models.ForeignKey(User, verbose_name='最近更新者', on_delete=models.CASCADE)
    update_datetime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "文件库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


