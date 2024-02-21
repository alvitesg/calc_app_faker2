"""test to be performed on main.py file"""
# pylint: disable=missing-function-docstring
import sys
from io import StringIO
from unittest.mock import patch
import pytest
from main import calculate_and_print, main  # Ensure this import matches your project structure

# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("9", "3", 'add', "The result of 9 add 3 is equal to 12"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("7", "2", 'multiply', "The result of 7 multiply 2 is equal to 14"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("2", "$", 'subtract', "Invalid number input: 2 or $ is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),  # Testing another invalid number input
    ("-5", "3", 'add', "The result of -5 add 3 is equal to -2"),  # Test with negative number
    ("3.5", "2.5", 'subtract', "The result of 3.5 subtract 2.5 is equal to 1.0"),  # Test with floating-point numbers
    ("10000000000000000000000000000000000000000000000000000000000000000", "2", 'divide', "The result of 10000000000000000000000000000000000000000000000000000000000000000 divide 2 is equal to 5.000000000000000000000000000E+63"),  # Test with large numbers
    ("2", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Test division by zero with non-zero dividend
    ("0", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Test division by zero with zero dividend
])
def test_calculate_and_print(a_string, b_string, operation_string,expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

def test_calculate_and_print_add():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        calculate_and_print('5', '3', 'add')
        assert fake_out.getvalue().strip() == "The result of 5 add 3 is equal to 8"

def test_calculate_and_print_subtract():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        calculate_and_print('10', '2', 'subtract')
        assert fake_out.getvalue().strip() == "The result of 10 subtract 2 is equal to 8"

def test_calculate_and_print_invalid_operation():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        calculate_and_print('5', '3', 'invalid')
        assert fake_out.getvalue().strip() == "Unknown operation: invalid"

def test_calculate_and_print_invalid_number_input():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        calculate_and_print('a', '3', 'add')
        assert fake_out.getvalue().strip() == "Invalid number input: a or 3 is not a valid number."

def test_calculate_and_print_divide_by_zero():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        calculate_and_print('10', '0', 'divide')
        assert fake_out.getvalue().strip() == "An error occurred: Cannot divide by zero"

def test_main_valid_arguments():
    with patch.object(sys, 'argv', ['main.py', '5', '3', 'add']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            assert fake_out.getvalue().strip() == "The result of 5 add 3 is equal to 8"

if __name__ == '__main__':
    pytest.main()
    