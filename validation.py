"""Validates `YYYY-MM-DD` & `HH:MM:SS` portions of date input."""


import datetime
from helpers import *

__author__ = "Eric Frisino"
__copyright__ = "Copyright 2020, Eric Frisino"
__license__ = "GPL-3.0-or-later"
__maintainer__ = "Eric Frisino"
__email__ = "code@ericfrisino.com"


def check_date(the_date, test=False):
    """Validate each component and the entire date stamp

    This function breaks up the date into the year month and date, then provides appropriate feedback based
    on validation criteria and lets the user know what need to be fixed to move forward."""

    # Output beginning of error checking test.
    print("╔════════════════════════════════════════════════════════════════════════════════╗")

    # Before we move on, lets check to make sure were formatted correctly.
    # TODO : Be forgiving, and add forward slash as option for writing out date.
    correctly_formatted_date = search(r'^\d{1,4}-\d{1,2}-\d{1,2}$', the_date)

    if correctly_formatted_date:
        # Split date on -
        date_parts = the_date.split('-')
        # Print the split date data
        # print("date_parts      : " + str(date_parts))

        # Validate Year by making sure its exactly 4 digits long.
        if search(r'^\d{4}$', date_parts[0]):
            if 1969 < int(date_parts[0]) < 10000:
                # Set the message.
                valid_year = "Year is valid."
                # Pad the message.
                valid_year_message = valid_year.ljust(76, ' ')
                # Print the message.
                print("║ \033[01m\u001b[32m\u2713\u001b[0m " + valid_year_message + " ║")
                # Set Year out of bounds flag to true.
                year_out_of_bounds_flag = False

            else:
                # Set the message.
                year_out_of_bounds = "Year falls out of bounds. Please Enter a year between 1970 and 9999."
                # Pad the message.
                yob_message = year_out_of_bounds.ljust(77, ' ')
                # Print the Message.
                print("║ \033[01m\033[33m!\u001b[0m " + yob_message + "║")
                # Set Year out of bounds flag to true.
                year_out_of_bounds_flag = True

        else:
            # Set the message.
            invalid_year = "Year not valid. Please Enter an integer between 1970 and 9999."
            # Pad the message.
            invalid_year_message = invalid_year.ljust(77, ' ')
            # Print the message.
            print("║ \033[01m\033[31m\u00bb\u001b[0m " + invalid_year_message + "║")
            # Set Year out of bounds flag to true.
            year_out_of_bounds_flag = False

        # Validate Month
        if search(r'^\d{1,2}$', date_parts[1]):
            if 0 < int(date_parts[1]) < 13:
                # Set the message.
                valid_month = "Month is valid."
                # Pad the message.
                valid_month_message = valid_month.ljust(77, ' ')
                # Print the message.
                print("║ \033[01m\u001b[32m\u2713\u001b[0m " + valid_month_message + "║")

            else:
                # Set the message.
                month_out_of_bounds = "Month out of bounds. Please Enter a month between 01 and 12."
                # Pad the message.
                month_out_of_bounds_message = month_out_of_bounds.ljust(77, ' ')
                # Print the message.
                print("║ \033[01m\033[31m\u00bb\u001b[0m " + month_out_of_bounds_message + "║")

        else:
            # Set the message.
            invalid_month = "Month not valid. Please Enter an integer between 01 and 12."
            # Pad the message.
            invalid_month_message = invalid_month.ljust(77, ' ')
            # Print the message.
            print("║ \033[01m\033[31m\u00bb\u001b[0m " + invalid_month_message + "║")

        # Validate Day
        if search(r'^\d{1,2}$', date_parts[2]):
            # Check to see if the day number falls into possible day numbers.
            if 0 < int(date_parts[2]) < 32:
                # Check to see if the day number is over 28.
                if 28 < int(date_parts[2]):
                    # Set the message.
                    day_possibly_out_of_bounds = "Day may be out of bounds depending on the month."
                    # Pad the message.
                    day_possibly_out_of_bounds_message = day_possibly_out_of_bounds.ljust(77, ' ')
                    # Print the message.
                    print("║ \033[01m\033[33m!\u001b[0m " + day_possibly_out_of_bounds_message + "║")
                else:
                    # Set the message.
                    valid_day = "Day is valid."
                    # Pad the message.
                    valid_day_message = valid_day.ljust(77, ' ')
                    # Print the message.
                    print("║ \033[01m\u001b[32m\u2713\u001b[0m " + valid_day_message + "║")
            else:
                # Set the message.
                day_out_of_bounds = "Day out of bounds. Please Enter a month between 01 and 32."
                # Pad the message.
                day_out_of_bounds_message = day_out_of_bounds.ljust(77, ' ')
                # Print the message.
                print("║ \033[01m\033[31m\u00bb\u001b[0m " + day_out_of_bounds_message + "║")
        else:
            # Set the message.
            invalid_day = "Day not valid. Please Enter an integer between 01 and 32.."
            # Pad the message.
            invalid_day_message = invalid_day.ljust(77, ' ')
            # Print the message.
            print("║ \033[01m\033[31m\u00bb\u001b[0m " + invalid_day_message + "║")

        if not year_out_of_bounds_flag:
            try:
                # See if we can convert the input to a proper date stamp.
                properly_formatted_date_stamp = datetime.datetime.strptime(the_date, '%Y-%m-%d')
                # then cast it to a string...
                properly_formatted_date = str(properly_formatted_date_stamp)
                # Set the message.
                valid_date = "Full Date is valid."
                # Pad the message.
                valid_date_message = valid_date.ljust(77, ' ')
                # and let the user know were all good here.
                print("║ \033[01m\u001b[32m\u2713\u001b[0m " + valid_date_message + "║")
                # Then set the validity flag to true.
                valid_date_input = True
            except ValueError as e:
                # otherwise, let the user know it is invalid...
                # Set the message.
                invalid_date = "Full Date is Invalid."
                # Pad the message.
                invalid_date_message = invalid_date.ljust(77, ' ')
                # Print the message.
                print("║ \033[01m\u001b[32m\u2713\u001b[0m " + invalid_date_message + "║")
                # Convert the error to a string.
                error_string = str(e).capitalize()
                # Pad the error message...
                the_error = error_string.ljust(75, ' ')
                # and print the message.
                print("║ \033[01m\033[31m  \u00bb\u001b[0m " + the_error + "║")
                # Then set the validity flag and the formatted date to false.
                properly_formatted_date = False
                valid_date_input = False
        else:
            # Convert the error to a string.
            error_string = "The year is valid, however " + date_parts[0] + " does not fall between 1970 and 9999"
            # Pad the error message...
            the_error = error_string.ljust(75, ' ')
            # and print the message.
            print("║ \033[01m\033[31m  \u00bb\u001b[0m " + the_error + "║")
            # Then set the validity flag and the formatted date to false.
            properly_formatted_date = False
            valid_date_input = False
    else:
        # Convert the error to a string.
        error_string = "\"" + the_date + "\" does not match format \'%y-%m-%d\'"
        # Pad the error message...
        the_error = error_string.ljust(77, ' ')
        # and print the message.
        print("║ \033[01m\033[31m\u00bb\u001b[0m " + the_error + "║")
        # Then set the validity flag and the formatted date to false.
        properly_formatted_date = False
        valid_date_input = False

    # Make a quick list to return.
    valid_date_information = [valid_date_input, properly_formatted_date]

    # Output the end of error checking.
    if not test:
        print("╟────────────────────────────────────────────────────────────────────────────────╢")
    else:
        print("╚════════════════════════════════════════════════════════════════════════════════╝")

    # Return the info for the calling function to handle.
    return valid_date_information


def check_time(the_time):
    """Validate the time portion of the stamp.

    This function will check to see if a meridiem was included, if it was it will check to see if were in
    the am or pm and then adjust the time accordingly. After that it will split the time apart at the `:`
    and validate each piece, then reassemble the timestamp and validate it with datetime. if all is well
    the stamp will be returned to the calling function and we will proceed, if not, we will continue to ask
    the user for a new time stamp and run this validation until it validates."""

    correctly_formatted_time = search(r'^\d{1,2}:\d{1,2}:\d{1,2}\s?.*$', the_time)

    if correctly_formatted_time:
        # Split time on :
        date_parts = the_time.split(':')

        # Try to split the time stamp.
        the_stamp = the_time.split(' ', 1)

        # Check to see if the correct meridiem was used.
        try:
            # Does anything exist at this address?
            am_pm = the_stamp[1]
            # if so, lets check for the meridiem.
            the_meridiem = check_meridiem(am_pm)

            # If the meridiem comes back False...
            if not the_meridiem[0]:
                # Pad the messages.
                invalid_meridiem_message_l1 = the_meridiem[1].ljust(77, ' ')
                invalid_meridiem_message_l2 = the_meridiem[2].ljust(77, ' ')
                # Print the messages.
                print("║ \033[01m\033[33m!\u001b[0m " + invalid_meridiem_message_l1 + "║")
                print("║ \033[01m\033[33m!\u001b[0m " + invalid_meridiem_message_l2 + "║")
                # Assuming it is already in 24 hour notation set the time.
                time_in_24_hours = the_stamp[0]
            # otherwise if it comes back as PM...
            elif the_meridiem[0] == "PM":
                # convert the time to 24 hour notation...
                time_in_24_hours = convert_to_24_hour_time(the_stamp[0])
            # or in the case that it comes back as AM...
            else:
                # otherwise it already is in 24 hour notation.
                time_in_24_hours = the_stamp[0]
        except IndexError as e:
            # If we dont have a meridiem notation let the user know were using a 24 hour format...
            print('║ \033[01m\u001b[32m\u2713\u001b[0m No meridiem found, assuming 24 Hour time used.')
            # and print the error if its not the one we know.
            if str(e) != "list index out of range":
                print(e)
            # Then set the hours timestamp to the `time_in_24_hours` variable.
            time_in_24_hours = the_stamp[0]

        # Split time on :
        time_parts = time_in_24_hours.split(':')

        # Validate Hour
        if search(r"^\d{1,2}$", time_parts[0]):
            if 0 <= int(time_parts[0]) < 24:
                print("║ \033[01m\u001b[32m\u2713\u001b[0m Hour is valid.")
            else:
                print("║ \033[01m\033[31m\u00bb\u001b[0m Hour out of bounds. Please Enter a hour between 0 and 23.")
                valid_time_input = False
        else:
            print("║ \033[01m\033[31m\u00bb\u001b[0m Hour not valid. Please Enter an integer between 0 and 23.")
            valid_time_input = False

        # Validate Minute
        if search(r"^\d{1,2}$", time_parts[1]):
            if 0 <= int(time_parts[1]) < 60:
                print("║ \033[01m\u001b[32m\u2713\u001b[0m Minute is valid.")
            else:
                print("║ \033[01m\033[31m\u00bb\u001b[0m Minute out of bounds. Please Enter a minute between 0 and 59.")
                valid_time_input = False
        else:
            print("║ \033[01m\033[31m\u00bb\u001b[0m Minute not valid. Please Enter an integer between 0 and 59.")
            valid_time_input = False

        # Validate Second
        if search(r"^\d{1,2}$", time_parts[2]):
            if 0 <= int(time_parts[2]) < 60:
                print("║ \033[01m\u001b[32m\u2713\u001b[0m Second is valid.")
            else:
                print("║ \033[01m\033[31m\u00bb\u001b[0m Second out of bounds. Please Enter a second between 0 and 59.")
                valid_time_input = False
        else:
            print("║ \033[01m\033[31m\u00bb\u001b[0m Second not valid. Please Enter an integer between 0 and 59.")
            valid_time_input = False

        try:
            properly_formatted_time = str(datetime.datetime.strptime(time_in_24_hours, '%H:%M:%S'))
            print("║ \033[01m\u001b[32m\u2713\u001b[0m Full Time is valid.")
            valid_time_input = True
        except ValueError as e:
            print("║ \033[01m\033[31m\u00bb\u001b[0m Full Time is Invalid.")
            print("║ \033[01m\033[31m  \u00bb\u001b[0m " + str(e))
            properly_formatted_time = False
            valid_time_input = False

    else:
        # Convert the error to a string.
        error_string = "\"" + the_time + "\" does not match format \'%H:%M:%S\'"
        # Pad the error message...
        the_error = error_string.ljust(77, ' ')
        # and print the message.
        print("║ \033[01m\033[31m\u00bb\u001b[0m " + the_error + "║")
        # Then set the validity flag and the formatted date to false.
        properly_formatted_time = False
        valid_time_input = False

    # Output the end of error checking.
    if correctly_formatted_time:
        # If theres no error, continue the table output.
        print("╟────────────────────────────────────────────────────────────────────────────────╢")
    else:
        print("╟────────────────────────────────────────────────────────────────────────────────╜")

    valid_time_information = [valid_time_input, properly_formatted_time]

    return valid_time_information
