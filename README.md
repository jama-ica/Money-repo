# tables

bank_payee = {
    name,
    note,
}

bank_paysource = {
    name,
    note,
}

bank = {
    name,
    note,
}

bank_shop = {
    bank_id,
    name,
    bank_shop_number,
    note,
}

bank_book = {
    bank_shop_id,
    bank_book_number,
    note,
}

bank_book_in = {
    bank_book_id,
    bank_payee_id,
    amount,
    date,
    note,
}

bank_book_out = {
    bank_book_id,
    bank_paysource_id,
    amount,
    date,
    note,
}

income_kind = {
    name,
    note,
}

income_source = {
}

income = {
    bank_book_in_id,
    income_kind_id,
    amount,
    date,
    note,
}

expense_kind = {
    name,
    note,
}

pay_method = {
    :
}

expense = {
    :
    pay_method,
    :
}


