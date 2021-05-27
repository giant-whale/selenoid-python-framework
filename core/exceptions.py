class CustomBrokenException(Exception):
    """
    Test will be marked as "Broken"
    """
    pass


class CustomFailedException(Exception):
    """
    Test will be marked as "Failed"
    """
    pass


class DriverSetupException(Exception):
    pass
