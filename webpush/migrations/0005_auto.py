from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpush', '0004_auto_20220831_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptioninfo',
            name='user_agent',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
