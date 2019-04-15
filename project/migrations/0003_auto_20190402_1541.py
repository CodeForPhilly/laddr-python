# Generated by Django 2.1.7 on 2019-04-02 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190402_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='update_content',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='community_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='developer_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='homepage_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, to='project.Profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='project.Tag'),
        ),
        migrations.AlterField(
            model_name='role',
            name='filled_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Profile'),
        ),
    ]
