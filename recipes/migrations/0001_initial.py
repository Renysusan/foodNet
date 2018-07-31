# Generated by Django 2.0.2 on 2018-07-31 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuisines', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('dish_title', models.CharField(max_length=255)),
                ('dish_image', models.FileField(upload_to='images/')),
                ('cooking_time', models.CharField(max_length=50)),
                ('method', models.TextField()),
                ('method_html', models.TextField(editable=False)),
                ('votes_total', models.IntegerField(default=1)),
                ('cuisine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='cuisines.Cuisine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='recipe',
            unique_together={('user', 'method')},
        ),
    ]
