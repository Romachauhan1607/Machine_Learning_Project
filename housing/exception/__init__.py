import os
import sys

class HousingException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message='error_message',error_detail='error_detail')

@staticmethod
def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
    _,_,exec_tb = error_detail.exec_info()

    line_number=exec_tb.tb_frame.f_lineno
    filename =exec_tb.tb_frame.f_code.co_filename
    error_message=f"Error occured in scipt: [{filename}] at line_number:[{line_number}] error_message:[{error_message}]"
    return error_message