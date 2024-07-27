#Christopher
#CIS261
#Week 3 - Course Project Phase 1: Create and Call Functions With Parameters
def get_emp_name():
    emp_name = input("Enter employee name: ")
    return emp_name

def get_hours_worked():
    while True:
        try:
            hours = float(input("Enter Hours: "))
            return hours
        except ValueError:
            print("Please enter a valid number for hours.")

def get_hourly_rate():
    while True:
        try:
            hourly_rate = float(input("Enter Hourly Rate: "))
            return hourly_rate
        except ValueError:
            print("Please enter a valid number for hourly rate.")

def get_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter Tax Rate: "))
            return tax_rate / 100
        except ValueError:
            print("Please enter a valid number for tax rate.")

def calc_tax_and_net_pay(hours, hourly_rate, tax_rate):
    g_pay = hours * hourly_rate
    income_tax = g_pay * tax_rate
    net_pay = g_pay - income_tax
    return g_pay, income_tax, net_pay

def print_info(emp_name, hours, hourly_rate, g_pay, tax_rate, income_tax, net_pay):
    print(f"{emp_name} {hours:,.2f} {hourly_rate:,.2f} {g_pay:,.2f} {tax_rate:.1%} {income_tax:,.2f} {net_pay:,.2f}")

def print_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    print(f"\nTotal Number Of Employees: {total_employees}")
    print(f"Total Hours: {total_hours:,.2f}")
    print(f"Total Gross Pay: {total_gross_pay:,.2f}")
    print(f"Total Tax: {total_tax:,.2f}")
    print(f"Total Net Pay: {total_net_pay:,.2f}")

if __name__ == "__main__":
    total_employees = 0
    total_hours = 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_net_pay = 0.00

    while True:
        emp_name = get_emp_name()
        if emp_name.upper() == "END":
            break
        hours = get_hours_worked()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        g_pay, income_tax, net_pay = calc_tax_and_net_pay(hours, hourly_rate, tax_rate)
        print_info(emp_name, hours, hourly_rate, g_pay, tax_rate, income_tax, net_pay)
        total_employees += 1
        total_hours += hours
        total_gross_pay += g_pay
        total_tax += income_tax
        total_net_pay += net_pay

    print_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay)
