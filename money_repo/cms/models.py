from django.db import models

# Bank
class Bank(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return self.name


# Bank Shop
class BankShop(models.Model):
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
	name = models.CharField(blank=False, max_length=64)
	bank_shop_number = models.PositiveSmallIntegerField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return str(self.bank) + ' ' + self.name


# Bank Pay Target
class BankPayee(models.Model):
	name = models.CharField(blank=False, max_length=64, default='')
	note = models.CharField(blank=True, max_length=256, default='', editable=True)

	def __str__(self):
		return self.name


# Bank Paysource
class BankPaysource(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return self.name


# Bankbook
class Bankbook(models.Model):
	bank_shop = models.ForeignKey(BankShop, on_delete=models.CASCADE)
	bankbook_number = models.PositiveIntegerField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return str(self.bank_shop) + ' ' + str(self.bankbook_number)


# Bankbook In
class BankbookIn(models.Model):
	bankbook = models.ForeignKey(Bankbook, on_delete=models.CASCADE)
	bank_payee = models.ForeignKey(BankPayee, on_delete=models.SET_NULL, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=False)
	date = models.DateField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return str(self.date) + ' ' + str(self.amount)


# Bankbook Out
class BankbookOut(models.Model):
	bankbook = models.ForeignKey(Bankbook, on_delete=models.CASCADE)
	bank_paysource = models.ForeignKey(BankPaysource, on_delete=models.SET_NULL, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=False)
	date = models.DateField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return str(self.date) + ' ' + str(self.amount)


# Income Kind
class IncomeKind(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return self.name


# Income
class Income(models.Model):
	bankbook_in = models.ForeignKey(BankbookIn, on_delete=models.CASCADE)
	income_kind = models.ForeignKey(IncomeKind, on_delete=models.SET_NULL, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=False)
	date = models.DateField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return str(self.amount)


# Expense Kind
class ExpenseKind(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return self.name


# Pay Method
class PayMethod(models.Model):
	name = models.CharField(blank=False, max_length=64)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return self.name


# Expense
class Expense(models.Model):
	bankbook_out = models.ForeignKey(BankbookOut, on_delete=models.CASCADE)
	expense_kind = models.ForeignKey(ExpenseKind, on_delete=models.SET_NULL, blank=True, null=True)
	pay_method = models.ForeignKey(PayMethod, on_delete=models.SET_NULL, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=False)
	date = models.DateField(blank=False)
	note = models.CharField(blank=True, max_length=256, editable=True)

	def __str__(self):
		return str(self.amount)

