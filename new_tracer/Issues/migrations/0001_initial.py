# Generated by Django 4.2.7 on 2023-12-23 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_alter_project_options_alter_projectuser_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=80, verbose_name='主题')),
                ('desc', models.TextField(verbose_name='问题描述')),
                ('priority', models.CharField(choices=[('danger', '高'), ('warning', '中'), ('success', '低')], default='danger', max_length=12, verbose_name='优先级')),
                ('status', models.SmallIntegerField(choices=[(1, '新建'), (2, '处理中'), (3, '已解决'), (4, '已忽略'), (5, '待反馈'), (6, '已关闭'), (7, '重新打开')], default=1, verbose_name='状态')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='开始时间')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结束时间')),
                ('mode', models.SmallIntegerField(choices=[(1, '公开模式'), (2, '隐私模式')], default=1, verbose_name='模式')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('latest_update_datetime', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('assign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to=settings.AUTH_USER_MODEL, verbose_name='指派')),
                ('attention', models.ManyToManyField(blank=True, related_name='observe', to=settings.AUTH_USER_MODEL, verbose_name='关注者')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_problems', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='模块名称')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '问题模块',
                'verbose_name_plural': '问题模块',
            },
        ),
        migrations.CreateModel(
            name='IssuesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='类型名称')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '问题类型',
                'verbose_name_plural': '问题类型',
            },
        ),
        migrations.CreateModel(
            name='IssuesReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_type', models.IntegerField(choices=[(1, '修改记录'), (2, '回复')], verbose_name='类型')),
                ('content', models.TextField(verbose_name='描述')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_reply', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('issues', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Issues.issues', verbose_name='问题')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Issues.issuesreply', verbose_name='回复')),
            ],
            options={
                'verbose_name': '问题回复',
                'verbose_name_plural': '问题回复',
            },
        ),
        migrations.AddField(
            model_name='issues',
            name='issues_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Issues.issuestype', verbose_name='问题类型'),
        ),
        migrations.AddField(
            model_name='issues',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Issues.module', verbose_name='模块'),
        ),
        migrations.AddField(
            model_name='issues',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='Issues.issues', verbose_name='父问题'),
        ),
        migrations.AddField(
            model_name='issues',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project', verbose_name='项目'),
        ),
    ]
