from django.contrib import admin

# models
from .models import Bank
from .models import BankShop
from .models import BankPayee
from .models import BankPaysource
from .models import BankBook
from .models import BankBookIn
from .models import BankBookOut
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


admin.site.register(BankPayee)



admin.site.register(BankPaysource)

admin.site.register(BankBook)
admin.site.register(BankBookIn)
admin.site.register(BankBookOut)
admin.site.register(IncomeKind)
admin.site.register(Income)
admin.site.register(ExpenseKind)
admin.site.register(PayMethod)
admin.site.register(Expense)
