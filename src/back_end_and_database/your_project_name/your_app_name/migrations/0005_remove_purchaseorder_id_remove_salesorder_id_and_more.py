from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('your_app_name', '0004_alter_product_info_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='id',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='id',
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_number',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='order_number',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
