def average(lst):
    return sum(lst) / len(lst)


def main():
    month_lst = ['January', 'February', 'March', 'April', 'May',
                 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']
    avg_lst = []
    jan_lst = []
    feb_lst = []
    mar_lst = []
    apr_lst = []
    may_lst = []
    jun_lst = []
    jul_lst = []
    aug_lst = []
    sep_lst = []
    oct_lst = []
    nov_lst = []
    dec_lst = []

    try:
        input_file = open('steps.txt', 'r')

        daily_steps = input_file.readlines()

# This is the loop to read and create a list for all steps in January
        for i in range(0, 31):
            jan_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        jan_avg = ("{:,.1f}".format(average(jan_lst)))
# This appends the average steps taken in Jan to a yearly list
        avg_lst.append(jan_avg)
        # This is the loop to read and create a list for all steps in February
        for i in range(31, 59):
            feb_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        feb_avg = ("{:,.1f}".format(average(feb_lst)))
# This appends the average steps taken in Feb to a yearly list
        avg_lst.append(feb_avg)
# This is the loop to read and create a list for all steps in March
        for i in range(59, 90):
            mar_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        mar_avg = ("{:,.1f}".format(average(mar_lst)))
# This appends the average steps taken in Mar to a yearly list
        avg_lst.append(mar_avg)
# This is the loop to read and create a list for all steps in April
        for i in range(90, 120):
            apr_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        apr_avg = ("{:,.1f}".format(average(apr_lst)))
# This appends the average steps taken in Apr to a yearly list
        avg_lst.append(apr_avg)
# This is the loop to read and create a list for all steps in May
        for i in range(120, 151):
            may_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        may_avg = ("{:,.1f}".format(average(may_lst)))
# This appends the average steps taken in May to a yearly list
        avg_lst.append(may_avg)
# This is the loop to read and create a list for all steps in June
        for i in range(151, 181):
            jun_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        jun_avg = ("{:,.1f}".format(average(jun_lst)))
# This appends the average steps taken in Feb to a yearly list
        avg_lst.append(jun_avg)
# This is the loop to read and create a list for all steps in July
        for i in range(181, 212):
            jul_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        jul_avg = ("{:,.1f}".format(average(jul_lst)))
# This appends the average steps taken in Jul to a yearly list
        avg_lst.append(jul_avg)
# This is the loop to read and create a list for all steps in August
        for i in range(212, 243):
            aug_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        aug_avg = ("{:,.1f}".format(average(aug_lst)))
# This appends the average steps taken in Aug to a yearly list
        avg_lst.append(aug_avg)
# This is the loop to read and create a list for all steps in September
        for i in range(243, 273):
            sep_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        sep_avg = ("{:,.1f}".format(average(sep_lst)))
# This appends the average steps taken in May to a yearly list
        avg_lst.append(sep_avg)
# This is the loop to read and create a list for all steps in October
        for i in range(273, 304):
            oct_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        oct_avg = ("{:,.1f}".format(average(oct_lst)))
# This appends the average steps taken in Feb to a yearly list
        avg_lst.append(oct_avg)
# This is the loop to read and create a list for all steps in November
        for i in range(304, 334):
            nov_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        nov_avg = ("{:,.1f}".format(average(nov_lst)))
# This appends the average steps taken in Jul to a yearly list
        avg_lst.append(nov_avg)
# This is the loop to read and create a list for all steps in December
        for i in range(334, 365):
            dec_lst.append(float(daily_steps[i]))
# This is the variable that calls the average function and formats the value to return the correct average steps.
        dec_avg = ("{:,.1f}".format(average(dec_lst)))
# This appends the average steps taken in Aug to a yearly list
        avg_lst.append(dec_avg)

        print("===Fitness Tracker Program===")
        n = 0
        while n <= 11:
            print(f"The average steps taken in {month_lst[n]} was {avg_lst[n]}")
            n += 1

    except IOError:
        print('The file could not be found.')
    except IndexError:
        print('There was an indexing error.')
    except:
        print('An error occurred.')


main()
