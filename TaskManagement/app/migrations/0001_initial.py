# Generated by Django 2.1.1 on 2018-10-02 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_1', models.CharField(blank=True, max_length=20, null=True, verbose_name='サンプル項目1 文字列')),
                ('sample_2', models.TextField(blank=True, null=True, verbose_name='サンプル項目2 メモ')),
                ('sample_3', models.IntegerField(blank=True, null=True, verbose_name='サンプル項目3 整数')),
                ('sample_4', models.FloatField(blank=True, null=True, verbose_name='サンプル項目4 浮動小数点')),
                ('sample_5', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='サンプル項目5 固定小数点')),
                ('sample_6', models.BooleanField(verbose_name='サンプル項目6 ブール値')),
                ('sample_7', models.DateField(blank=True, null=True, verbose_name='サンプル項目7 日付')),
                ('sample_8', models.DateTimeField(blank=True, null=True, verbose_name='サンプル項目8 日時')),
                ('sample_9', models.IntegerField(blank=True, choices=[(1, '選択１'), (2, '選択２'), (3, '選択３')], null=True, verbose_name='サンプル項目9_選択肢（固定）')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='作成時間')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='更新時間')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CreatedBy', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('sample_10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sample_10', to=settings.AUTH_USER_MODEL, verbose_name='サンプル項目10_選択肢（マスタ連動）')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='UpdatedBy', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': 'MAMEZOU',
                'verbose_name_plural': 'MAMEZOU',
            },
        ),
    ]
