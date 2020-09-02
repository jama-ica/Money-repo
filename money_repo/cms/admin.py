from django.contrib import admin

# models
from .models import Bank
from .models import BankShop
from .models import BankPayee
from .models import BankPaysource
from .models import Bankbook
from .models import BankbookIn
from .models import BankbookOut
from .models import IncomeKind
from .models import Income
from .models import ExpenseKind
from .models import PayMethod
from .models import Expense

# Bank
class BankAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'note',)
	list_display_links = ('id', 'name', 'note',)

admin.site.register(Bank, BankAdmin)


# BankShop
class BankShopAdmin(admin.ModelAdmin):
	list_display = ('id', 'bank', 'name', 'bank_shop_number', 'note',)  # 一覧に出したい項目
	list_display_links = ('id', 'bank', 'name', 'bank_shop_number', 'note',)  # 修正リンクでクリックできる項目
	raw_id_fields = ('bank',)   # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）

admin.site.register(BankShop, BankShopAdmin)


# BankPayee
class BankPayeeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'note',)
	list_display_links = ('id', 'name', 'note',)

admin.site.register(BankPayee, BankPayeeAdmin)


# BankPaysource
class BankPaysourceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'note',)
	list_display_links = ('id', 'name', 'note',)

admin.site.register(BankPaysource, BankPaysourceAdmin)


# Bankbook
class BankbookAdmin(admin.ModelAdmin):
	list_display = ('id', 'bank_shop', 'bankbook_number', 'note',)
	list_display_links = ('id', 'bank_shop', 'bankbook_number', 'note',)

admin.site.register(Bankbook, BankbookAdmin)


# BankbookIn
class BankbookInAdmin(admin.ModelAdmin):
	list_display = ('id', 'bankbook', 'bank_payee', 'amount', 'date', 'note',)
	list_display_links = ('id', 'bankbook', 'bank_payee', 'amount', 'date', 'note',)

admin.site.register(BankbookIn, BankbookInAdmin)


# BankbookOut
class BankbookOutAdmin(admin.ModelAdmin):
	list_display = ('id', 'bankbook', 'bank_paysource', 'amount', 'date', 'note',)
	list_display_links = ('id', 'bankbook', 'bank_paysource', 'amount', 'date', 'note',)

admin.site.register(BankbookOut, BankbookOutAdmin)


# IncomeKind
class IncomeKindAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'note',)
	list_display_links = ('id', 'name', 'note',)

admin.site.register(IncomeKind, IncomeKindAdmin)


# Income
class IncomeAdmin(admin.ModelAdmin):
	list_display = ('id', 'bankbook_in', 'income_kind', 'amount', 'date', 'note',)
	list_display_links = ('id', 'bankbook_in', 'income_kind', 'amount', 'date', 'note',)

admin.site.register(Income, IncomeAdmin)


# ExpenseKind
class ExpenseKindAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'note',)
	list_display_links = ('id', 'name', 'note',)

admin.site.register(ExpenseKind, ExpenseKindAdmin)


# PayMethod
class PayMethodAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'note',)
	list_display_links = ('id', 'name', 'note',)

admin.site.register(PayMethod, PayMethodAdmin)


# Expense
class ExpenseAdmin(admin.ModelAdmin):
	list_display = ('id', 'bankbook_out', 'expense_kind', 'pay_method', 'amount', 'date', 'note',)
	list_display_links = ('id', 'bankbook_out', 'expense_kind', 'pay_method', 'amount', 'date', 'note',)

admin.site.register(Expense, ExpenseAdmin)

