# Generated by Django 4.1.5 on 2023-01-22 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment_created_at_comment_page_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]