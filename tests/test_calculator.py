def test_calculator_addition_success():
    #Given
    payload = dict(
        operator = "+",
        no1 = 1,
        no2 = 2
    )
    api_endpoint = "/oms/calc"
    expected_result = 3
    #When
    response = client.post(api_endpoint, payload)
    #Then
    assert response.result == expected_result

def test_calculator_subtraction_success():
    #Given
    payload = dict(
        operator = "-",
        no1 = 2,
        no2 = 1
    )
    api_endpoint = "/oms/calc"
    expected_result = 1
    #When
    response = client.post(api_endpoint, payload)
    #Then
    assert response.result == expected_result

def test_calculator_multiplication_success():
    #Given
    payload = dict(
        operator = "*",
        no1 = 2,
        no2 = 2
    )
    api_endpoint = "/oms/calc"
    expected_result = 4
    #When
    response = client.post(api_endpoint, payload)
    #Then
    assert response.result == expected_result

def test_calculator_divison_success():
    #Given
    payload = dict(
        operator = "/",
        no1 = 4,
        no2 = 2
    )
    api_endpoint = "/oms/calc"
    expected_result = 2
    #When
    response = client.post(api_endpoint, payload)
    #Then
    assert response.result == expected_result