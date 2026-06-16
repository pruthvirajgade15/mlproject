import sys


def error_message_details(error, error_detail: sys):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in {file_name} at line {line_number}: {str(error)}"


def CustomException(error, error_detail: sys):
    message = error_message_details(error, error_detail=error_detail)
    return message

def __str__(self):
    return self.message