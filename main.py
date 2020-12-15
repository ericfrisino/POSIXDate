#!/usr/bin/env python
"""Convert dates from YYYY-MM-DD HH:MM:SS format to ISO format."""

from validation import *

__author__ = "Eric Frisino"
__copyright__ = "Copyright 2020, Eric Frisino"
__credits__ = ""
__license__ = "GPL-3.0-or-later"
__version__ = "0.0.1"
__maintainer__ = "Eric Frisino"
__email__ = "code@ericfrisino.com"
__status__ = "Prototype"  # "Prototype", "Development", or "Production"


# Get Initial Date Time from user.
def get_date_time():
    # Request timestamp from the user.
    users_date_timestamp = input("Please Enter Date & Time (YYYY-MM-DD HH:MM:SS) : ")
    # Let the user know what they entered.
    # print("You entered     : " + users_date_timestamp)
    # Return the timestamp
    return users_date_timestamp


# Get Initial Date Time from user.
def get_date():
    # Request timestamp from the user.
    users_datestamp = input("║ Please Enter Date (YYYY-MM-DD) : ")
    # Let the user know what they entered.
    # print("You entered     : " + users_datestamp)
    # Return the timestamp
    return users_datestamp


# Get Initial Date Time from user.
def get_time():
    # Request timestamp from the user.
    users_timestamp = input("║ Please Enter Time (HH:MM:SS) : ")
    # Let the user know what they entered.
    # print("You entered     : " + users_timestamp)
    # Return the timestamp
    return users_timestamp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Get date-time stamp from user.
    a_timestamp = get_date_time()

    # Split date-time stamp into two parts.
    # `split_timestamp[0]` should be YYYY-MM-DD
    # `split_timestamp[1]` should be HH:MM;SS (meridiem)
    split_timestamp = a_timestamp.split(' ', 1)

    # Let the developer know how the string split.
    print(str(split_timestamp))

    # Send date portion to be validated.
    valid_date_input = check_date(split_timestamp[0])

    # if it comes back invalid, keep asking for & validating it until the user gets it right.
    while not valid_date_input[0]:
        valid_date_input = check_date(get_date())

    valid_time_input = check_time(split_timestamp[1])

    while not valid_time_input[0]:
        valid_time_input = check_time(get_time())

    # Clean up returned Stamps
    the_correct_date_parts = str(valid_date_input[1])
    the_correct_date = the_correct_date_parts.split(" ")

    the_correct_time_parts = str(valid_time_input[1])
    the_correct_time = the_correct_time_parts.split()

    # Once we have a valid date and time, concatenate them.
    the_corrected_stamp = str(the_correct_date[0]) + " " + str(the_correct_time[1])

    # Set validated time message.
    validated_time = "Validated Time : " + the_corrected_stamp
    # Pad validated time message.
    validated_time_message = validated_time.ljust(77, ' ')
    # Print validated time message.
    print("║ \033[01m\u001b[32m\u2713\u001b[0m " + validated_time_message + "║")

    # Process the entered data into an actual timestamp.
    a_timestamp_obj = datetime.datetime.strptime(the_corrected_stamp, '%Y-%m-%d %H:%M:%S')
    # Set actual timestamp message.
    timestamp_obj = "ISO Time       : " + str(a_timestamp_obj)
    # Pad actual timestamp message.
    timestamp_obj_message = timestamp_obj.ljust(77, ' ')
    # Show the user the timestamp.
    print("║ \033[01m\u001b[32m\u2713\u001b[0m " + timestamp_obj_message + "║")

    # Convert the timestamp into an ISO timestamp.
    a_POSIX_timestamp = a_timestamp_obj.timestamp()
    # Set POSIX timestamp message.
    POSIX_timestamp = "POSIX Time     : " + str(int(a_POSIX_timestamp))
    # Pad POSIX timestamp message.
    POSIX_timestamp_message = POSIX_timestamp.ljust(77, ' ')
    # Show the user the ISO timestamp.
    print("║ \033[01m\u001b[32m\u2713\u001b[0m " + POSIX_timestamp_message + "║")

    # Print last line of UI
    print("╚════════════════════════════════════════════════════════════════════════════════╝")
