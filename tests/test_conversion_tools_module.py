from MyPythonLibrary.conversion_tools import MyConversionTools

tool = MyConversionTools()

def test_celsius_to_fahrenheit():
    assert tool.celsius_to_fahrenheit(0) == 32

def test_kilometers_to_miles():
    assert round(tool.kilometers_to_miles(1), 2) == 0.62
