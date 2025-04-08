class BudgetAppExceptions (Exception):

    def __init__(self, message="Internal Error") -> None:
        self.message = message
        super().__init__(self.message)


class ZeroNegativeError(BudgetAppExceptions):
    def __init__(self, message="[ERROR]: Function error, value is either negative or zero"):
        super().__init__(message)
        with open('log_file.txt', 'w+') as file:
            file.write(message)
