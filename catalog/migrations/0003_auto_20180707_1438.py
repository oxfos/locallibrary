# Generated by Django 2.0.6 on 2018-07-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180707_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn" target="_blank">ISBN number</a>', max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('German', 'German'), ('Spanish', 'Spanish'), ('Chinese', 'Chinese'), ('French', 'French'), ('Italian', 'Italian')], default='English', help_text='Language of the book', max_length=100),
        ),
    ]