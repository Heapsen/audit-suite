import load_items

items = load_items.table_to_items()
for item in items:
    item.check_unit_count()
    item.check_total_unit_value()
    item.print_issues()