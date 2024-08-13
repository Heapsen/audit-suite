import openpyxl
import Item

# Load Excel Spreadsheet
path = "Book1.xlsx"
wb = openpyxl.load_workbook(path)
ws = wb.active

def table_to_items():
    # Gets the range 
    # e.g. A1:G4
    table = ws.tables["Table1"].ref
    # Gets all the cells from the range
    table_cells = ws[table]
    # Turns the cells into a list
    # We do this so we can loop over the cells using `for`
    rows = list(table_cells)

    # Loop through rows and turn each row into an object `Item`
    # Adds each created Item into a list and returns it
    item_list = []
    for i in range(len(rows)):
        row = rows[i]
        # Ignores the heading (first row)
        if (i != 0):
            row_values = [cell.value for cell in row]
            item_list.append(Item.Item(row_values[0], row_values[1], row_values[2], row_values[3], row_values[4], row_values[5], row_values[6], i+1))
    return item_list