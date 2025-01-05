# Generated by Django 5.1.4 on 2025-01-05 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicename', models.CharField(max_length=200, unique=True)),
                ('isclient', models.BooleanField(null=True)),
                ('hostname', models.CharField(max_length=200)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('wanip', models.CharField(max_length=200)),
                ('rpcport', models.IntegerField(blank=True, default=7777, null=True)),
                ('rpcurl', models.URLField(blank=True, null=True)),
                ('sshport', models.IntegerField(blank=True, default=22, null=True)),
                ('deviceplatform', models.CharField(max_length=20)),
                ('laniface', models.CharField(blank=True, max_length=20, null=True)),
                ('waniface', models.CharField(blank=True, max_length=20, null=True)),
                ('wlaniface', models.CharField(blank=True, max_length=20, null=True)),
                ('extaprops', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DUTHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dutname', models.CharField(max_length=200, unique=True)),
                ('hostname', models.CharField(max_length=200)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('serial', models.CharField(blank=True, max_length=50, null=True)),
                ('baudrate', models.IntegerField(blank=True, null=True)),
                ('wanip', models.CharField(max_length=200)),
                ('waniface', models.CharField(blank=True, max_length=20, null=True)),
                ('sshport', models.IntegerField(blank=True, default=22, null=True)),
                ('dutplatform', models.CharField(max_length=20)),
                ('extaprops', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestcaseHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testcasename', models.CharField(max_length=200, unique=True)),
                ('testplatform', models.CharField(max_length=30)),
                ('testarea', models.CharField(max_length=200)),
                ('isstandalone', models.BooleanField(default=False)),
                ('description', models.TextField(default='No Description')),
                ('priority', models.CharField(default='P0', max_length=20)),
                ('testcasedetails', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='TestSuiteHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testsuitename', models.CharField(max_length=200, unique=True)),
                ('testsuiteplatform', models.CharField(max_length=30)),
                ('testcaselist', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceMapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientslist', models.ManyToManyField(related_name='mapped_clients', to='core.devicehandler')),
                ('profilename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.duthandler')),
            ],
        ),
    ]
