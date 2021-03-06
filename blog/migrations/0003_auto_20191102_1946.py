# Generated by Django 2.2.6 on 2019-11-02 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_publicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to='featured_image', verbose_name='キャッチアイ画像'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.Category', verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicity',
            field=models.BooleanField(default=True, verbose_name='公開する'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag', verbose_name='タグ'),
        ),
    ]
