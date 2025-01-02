import pandas as pd

table_before_file = 'table_before_anonce.xlsx'
table_after_file = 'table_after_anonce.xlsx'

before = pd.read_excel(table_before_file)
after = pd.read_excel(table_after_file)

address_column = 'Wallet Address'

common_addresses = pd.merge(before, after, on=address_column)

added_addresses = after[~after[address_column].isin(before[address_column])]

before['status'] = 'normal'
after['status'] = 'normal'

common_addresses['status'] = 'purple'

added_addresses['status'] = 'blue'

styled_addresses = pd.concat([before, common_addresses, added_addresses]).drop_duplicates()

styled_addresses.to_excel('styled_addresses.xlsx', index=False)
