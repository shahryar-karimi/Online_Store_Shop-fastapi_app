# Generated by Django 4.0 on 2024-03-19 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        ('Salesman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesmen', to='Salesman.salesmanprofile'),
        ),
        migrations.AddField(
            model_name='categorydetail',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_properties', to='Product.category'),
        ),
        migrations.AddField(
            model_name='category',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='Product.category'),
        ),
    ]
