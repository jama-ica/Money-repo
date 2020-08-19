from django.contrib import admin

# models
from .models import BankPayee
from .models import BankPaysource
from .models import Bank
from .models import BankShop
from .models import BankBook
from .models import BankBookIn
from .models import BankBookOut
from .models import IncomeKind
from .models import Income
from .models import ExpenseKind
from .models import PayMethod
from .models import Expense

admin.site.register(BankPayee)
admin.site.register(BankPaysource)
admin.site.register(Bank)
admin.site.register(BankShop)
admin.site.register(BankBook)
admin.site.register(BankBookIn)
admin.site.register(BankBookOut)
admin.site.register(IncomeKind)
admin.site.register(Income)
admin.site.register(ExpenseKind)
admin.site.register(PayMethod)
admin.site.register(Expense)
