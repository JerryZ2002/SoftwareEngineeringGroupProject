from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('your_app_name', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_info',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('specification', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
