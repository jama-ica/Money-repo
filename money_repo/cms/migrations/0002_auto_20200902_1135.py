# Generated by Django 3.1 on 2020-09-02 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Bankbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankbook_number', models.PositiveIntegerField()),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BankbookIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BankbookOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BankPayee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('note', models.CharField(blank=True, default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BankPaysource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BankShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('bank_shop_number', models.PositiveSmallIntegerField()),
                ('note', models.CharField(blank=True, max_length=256)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('note', models.CharField(blank=True, max_length=256)),
                ('bankbook_out', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.bankbookout')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('note', models.CharField(blank=True, max_length=256)),
                ('bankbook_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.bankbookin')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PayMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('note', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='income',
            name='income_kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.incomekind'),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.expensekind'),
        ),
        migrations.AddField(
            model_name='expense',
            name='pay_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.paymethod'),
        ),
        migrations.AddField(
            model_name='bankbookout',
            name='bank_paysource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.bankpaysource'),
        ),
        migrations.AddField(
            model_name='bankbookout',
            name='bankbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.bankbook'),
        ),
        migrations.AddField(
            model_name='bankbookin',
            name='bank_payee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.bankpayee'),
        ),
        migrations.AddField(
            model_name='bankbookin',
            name='bankbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.bankbook'),
        ),
        migrations.AddField(
            model_name='bankbook',
            name='bank_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.bankshop'),
        ),
    ]
