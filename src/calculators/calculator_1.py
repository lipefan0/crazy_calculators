from typing import Dict
from flask import Request as FlaskRequest  # Import the Request class for type hinting

class Calculator1:
    def calculate(self, request: FlaskRequest):  # Use FlaskRequest for type hinting
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_calculation(splited_number)
        second_process_result = self.__second_calculation(splited_number)
        calc_result = first_process_result + second_process_result + splited_number
        response = self.__format_response(calc_result)

        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("Number is required")
        input_date = body["number"]
        return input_date
    
    def __first_calculation(self, first_number: float) -> float:
        first_part =  (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part
    
    def __second_calculation(self, second_number: float) -> float:
        first_part = (second_number ** 2.121)
        second_part = (first_part / 5) + 1
        return second_part
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "calculator": 1,
                "result": round(calc_result, 2)
            }
        }