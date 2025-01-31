# import sys
# import logging

# def error_message_details(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exe_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename
#     error_message = 'Error occured in python script name[{0}] line number [{1} error messsage [{2}]'.format(
#         file_name,exc_tb.tb_lineno,str(error))

#     return error_message



# class CustomerException(Exception):
#     def __init__(self, error_message, error_details:sys):
#         super().__init__(error_message)
#         self.error_message = error_message
#         self.error_message = error_message_details(error_message,error_detail=error_details)

#     def __str__(self):
#         return self.error_message


# if __name__ == '__main__':

#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("divide by zero error")
#         raise CustomerException(e,sys)

import sys
import logging
from src.logger import logging


def error_message_details(error, error_detail: sys):
    """Generate detailed error message."""
    _, _, exc_tb = error_detail.exc_info()  # Fixed typo: `exe_info` -> `exc_info`
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occurred in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):  # Changed `CustomerException` to `CustomException` for a general-purpose name
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message


