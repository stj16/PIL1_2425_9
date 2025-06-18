# Generated manually to add date_time field

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_carrequest_start_hours_usual'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrequest',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ] 