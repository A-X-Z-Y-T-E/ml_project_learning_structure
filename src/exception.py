import sys
from src.logger import logging

def error_message_detail(error, error_detail):
    """
    Generate a detailed error message including file name and line number.

    Args:
        error: The error message.
        error_detail: The traceback details (usually sys.exc_info()).

    Returns:
        A formatted string with error details.
    """
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script [{file_name}] at line [{line_number}] with error: [{error}]"

class CustomException(Exception):
    """
    Custom exception class for detailed error messages.
    """
    def __init__(self, error_message, error_detail=sys.exc_info()):
        super().__init__(error_message)  # Corrected super().__init__()
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        """
        Return a detailed string representation of the error.
        """
        return self.error_message
    

