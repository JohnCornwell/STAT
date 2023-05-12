# This file is used by the presentation layer as a bridge to the persistent layer.
# This file includes user data access and access to basic test-specific info

from Storage import testAccess, directoryAccess

# -- Functions for User Info -- #


def login(username):
    error = directoryAccess.login_user(username)
    return error


def logout():
    error = directoryAccess.logout_user()
    return error


def create_user(username):
    error = directoryAccess.create_user(username)
    return error


# Right now, we don't implement the delete user function in GUI. Can be added later to
# the GUI as there is full implementation in persistent layer
def delete_user(username):
    error = directoryAccess.delete_user(username)
    return error

# -- Functions for Test Info -- #


def list_tests():
    result = testAccess.list_tests()
    return result


def load_test(name):
    error, result = testAccess.load_test(name)
    if error != "":
        return error, result
    elif result.get("Num_tasks") is None:
        return "The test params file is missing a Num_tasks value.", result
    else:
        try:
            int(result.get("Num_tasks"))
        except ValueError:
            return "The test params file is missing a valid Num_tasks value.", result
        return error, result


def delete_test(name):
    error = testAccess.delete_test(name)
    return error
