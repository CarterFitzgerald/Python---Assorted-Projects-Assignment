name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_rate = float(input("Enter hourly pay rate: "))
ato_tax = float(input("Enter ATO tax withholding rate: "))
medicare_rate = float(input("Enter Medicare Levy rate: "))

last_name = name.split()[-1]
gross_pay = float(hours_worked * hourly_rate)
tax = gross_pay * (float(ato_tax))
tax_percentage = ato_tax * 100
medicare_levy = gross_pay * (float(medicare_rate))
medicare_percentage = medicare_rate * 100
total_deduction = float(medicare_levy + tax)
net_pay = float(gross_pay - total_deduction)

hours_worked_1dp = ("{:.1f}".format(hours_worked))
hourly_rate_2dp = ("{:.2f}".format(hourly_rate))
gross_pay_2dp = ("{:.2f}".format(gross_pay))
tax_percentage_1dp = ("{:.1f}".format(tax_percentage))
tax_2dp = ("{:.2f}".format(tax))
medicare_percentage_1dp = ("{:.1f}".format(medicare_percentage))
medicare_levy_2dp = ("{:.2f}".format(medicare_levy))
total_deduction_2dp = ("{:.2f}".format(total_deduction))
net_pay_2dp = ("{:.2f}".format(net_pay))

result = (
    "\n"
    f"Employee Name: {last_name}\n"
    f"Hours Worked: {hours_worked_1dp}\n"
    f"Pay Rate: ${hourly_rate_2dp}\n"
    f"Gross Pay: ${gross_pay_2dp}\n"
    "Deductions: \n"
    f"   ATO tax ({tax_percentage_1dp}%): ${tax_2dp}\n"
    f"   Medicare Levy ({medicare_percentage_1dp}%): ${medicare_levy_2dp}\n"
    f"   Total Deduction: ${total_deduction_2dp}\n"
    "\n"
    f"Net Pay: ${net_pay_2dp}\n"
    "\n"
)
print(result)
