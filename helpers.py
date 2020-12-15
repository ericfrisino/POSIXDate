"""Various helpers for the main script and the validator."""

from re import search


# Check to see what the Meridiem is for this time stamp
# -- Called from the validation file.
def check_meridiem(the_time):
    # Search timestamp for the post-meridiem annotation.
    if search(r"^(p|P|pm|PM)$", the_time):
        the_meridiem = ["PM", "", ""]
    # then search timestamp for the anti-meridiem annotation.
    elif search(r"^(a|A|am|AM)$", the_time):
        the_meridiem = ["AM", "", ""]
    # then, if neither exist, fail this test.
    else:
        # Set meridiem to False, and add error information.
        the_meridiem = [False,
                        "Assuming 24 hour notation used due to no recognized meridiem.",
                        "In the future use one of the following : a, A, am, AM, p, P, pm, or PM"]

    # Returns ["AM"|"PM"|False, "", ""]
    return the_meridiem


# Create a 24 hour timestamp from a 12 hour timestamp.
# -- This timestamp only takes into account Hours, Minutes, & Seconds.
def convert_to_24_hour_time(the_timestamp):
    # Break up the timestamp based on the : symbol.
    the_time_split = str(the_timestamp).split(":")

    if int(the_time_split[0]) < 12:

        # add the entered (PM Hours) hour to 12.
        the_new_hour = int(the_time_split[0]) + 12

        # Create a new timestamp.
        return str(the_new_hour) + ":" + str(the_time_split[1]) + ":" + str(the_time_split[2])

    else:
        return str(the_time_split[0]) + ":" + str(the_time_split[1]) + ":" + str(the_time_split[2])
