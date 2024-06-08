from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('your_app_name', '0003_inventory_salesorder_purchaseorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='product_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
