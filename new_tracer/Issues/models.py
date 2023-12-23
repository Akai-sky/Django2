from django.db import models
from django.contrib.auth import get_user_model
from project.models import Project

User = get_user_model()


class IssuesType(models.Model):
    """ 问题类型 例如：任务、功能、Bug """

    PROJECT_INIT_LIST = ["任务", '功能', 'Bug']

    title = models.CharField(verbose_name='类型名称', max_length=32)
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "问题类型"
        verbose_name_plural = verbose_name


class Module(models.Model):
    """ 模块（里程碑）"""
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='模块名称', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "问题模块"
        verbose_name_plural = verbose_name


class Issues(models.Model):
    """ 问题 """
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    issues_type = models.ForeignKey(IssuesType, verbose_name='问题类型', on_delete=models.CASCADE)
    module = models.ForeignKey(Module, verbose_name='模块', null=True, blank=True, on_delete=models.CASCADE)

    subject = models.CharField(verbose_name='主题', max_length=80)
    desc = models.TextField(verbose_name='问题描述')
    priority_choices = (
        ("danger", "高"),
        ("warning", "中"),
        ("success", "低"),
    )
    priority = models.CharField(verbose_name='优先级', max_length=12, choices=priority_choices, default='danger')

    # 新建、处理中、已解决、已忽略、待反馈、已关闭、重新打开
    status_choices = (
        (1, '新建'),
        (2, '处理中'),
        (3, '已解决'),
        (4, '已忽略'),
        (5, '待反馈'),
        (6, '已关闭'),
        (7, '重新打开'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=1)

    assign = models.ForeignKey(User, verbose_name='指派', related_name='task', null=True, blank=True,
                               on_delete=models.CASCADE)
    attention = models.ManyToManyField(User, verbose_name='关注者', related_name='observe', blank=True)

    start_date = models.DateField(verbose_name='开始时间', null=True, blank=True)
    end_date = models.DateField(verbose_name='结束时间', null=True, blank=True)
    mode_choices = (
        (1, '公开模式'),
        (2, '隐私模式'),
    )
    mode = models.SmallIntegerField(verbose_name='模式', choices=mode_choices, default=1)

    parent = models.ForeignKey("self", verbose_name='父问题', related_name='child', null=True, blank=True,
                               on_delete=models.SET_NULL)

    creator = models.ForeignKey(User, verbose_name='创建者', related_name='create_problems', on_delete=models.CASCADE)

    create_datetime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    latest_update_datetime = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = verbose_name


class IssuesReply(models.Model):
    """ 问题回复"""

    reply_type_choices = (
        (1, '修改记录'),
        (2, '回复')
    )
    reply_type = models.IntegerField(verbose_name='类型', choices=reply_type_choices)

    issues = models.ForeignKey(Issues, verbose_name='问题', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='描述')
    creator = models.ForeignKey(User, verbose_name='创建者', related_name='create_reply', on_delete=models.CASCADE)
    create_datetime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    reply = models.ForeignKey("self", verbose_name='回复', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "问题回复"
        verbose_name_plural = verbose_name
