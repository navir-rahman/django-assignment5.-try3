# Generated by Django 5.0.1 on 2024-01-25 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserAccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('balance_after_transaction', models.DecimalField(decimal_places=2, max_digits=12)),
                ('transaction_type', models.IntegerField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdrawal'), ('BORROW', 'Borrow Book'), ('RETURN', 'Return Book')], null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('loan_approve', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='UserAccount.useraccount')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
