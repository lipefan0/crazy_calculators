from typing import Dict
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"number": 1})

    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)

    # Formato da resposta
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 14.25
    assert response["data"]["calculator"] == 1
    print()
    print(response)