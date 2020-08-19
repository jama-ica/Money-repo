from django.db import models

# Bank Pay Target
class Bank(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return self.name

class BankShop(models.Model):
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
	name = models.CharField(blank=False, max_length=64)
	bank_shop_number = models.PositiveSmallIntegerField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

class BankPayee(models.Model):
	name = models.CharField(blank=False, max_length=64, default='')
	note = models.CharField(blank=True, max_length=256, default='', editable=True)

class BankPaysource(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

class BankBook(models.Model):
	bank_shop = models.ForeignKey(BankShop, on_delete=models.CASCADE)
	bank_book_number = models.PositiveIntegerField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

class BankBookIn(models.Model):
	bank_book = models.ForeignKey(BankBook, on_delete=models.CASCADE)
	bank_payee = models.ForeignKey(BankPayee, on_delete=models.SET_NULL, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=False)
	date = models.DateTimeField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

class BankBookOut(models.Model):
	bank_book = models.ForeignKey(BankBook, on_delete=models.CASCADE)
	bank_paysource = models.ForeignKey(BankPaysource, on_delete=models.SET_NULL, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=False)
	date = models.DateTimeField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

class IncomeKind(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

class Income(models.Model):
	bank_book_in = models.ForeignKey(BankBookIn, on_delete=models.CASCADE)
	income_kind = models.ForeignKey(IncomeKind, on_delete=models.SET_NULL, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=False)
	date = models.DateTimeField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

class ExpenseKind(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

class PayMethod(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

class Expense(models.Model):
	bank_book_in = models.ForeignKey(BankBookIn, on_delete=models.CASCADE)
	expense_kind = models.ForeignKey(ExpenseKind, on_delete=models.SET_NULL, blank=True, null=True)
	pay_method = models.ForeignKey(PayMethod, on_delete=models.SET_NULL, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=False)
	date = models.DateTimeField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)
