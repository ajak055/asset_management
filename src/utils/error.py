

class CustomError(Exception):

    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


    # def businessValidationError(self, message):
    #     return message
    

if __name__ == "__main__":
    if(10<12):
        raise CustomError("this is an error")