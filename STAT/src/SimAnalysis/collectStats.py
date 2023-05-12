from Storage import testAccess


# This method is responsible for retrieving data related to stats on
# a test, and returning this data in a form that will be displayed by
# the calling GUI.
def collect_stats(test_name):
    # collect data from file
    error, data = testAccess.read_stats(test_name)
    # change int or float data into a string
    for key in data:
        data[key] = str(data[key])
    return error, data


# This method will return the size of the test directory
def get_size():
    pass
