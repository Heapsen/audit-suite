class Item:
    def __init__(self, id, name, units_held, value_per_unit, total_value_held_sl, verified_count, total_vv, row):
        self.name = name
        self.id = id
        self.units_held = units_held
        self.value_per_unit = value_per_unit
        self.verified_count = verified_count
        self.total_value_held_sl = total_value_held_sl
        self.total_vv = total_vv
        self.issues = []
        self.row = row

    def check_unit_count(self):
        if self.units_held != self.verified_count:
            self.issues.append("Units Held does not match Verified Stock Count ")
    
    def print_issues(self):
        for issue in self.issues:
            print("(Row " +str(self.row) + ") " + self.name + ": " + issue)

    def check_total_unit_value(self):
        if self.units_held*self.value_per_unit != self.total_value_held_sl:
            self.issues.append("Total Verified Stock Value does not match Total Value Held as per Stock Listing")