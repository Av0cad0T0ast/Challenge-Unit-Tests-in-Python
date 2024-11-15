import unittest
from unittest.mock import patch
from datetime import datetime


def getStockSymbol():
    while True:
        symbol = input("Please enter the stock symbol (1-7 capital letters): ").upper()
        if symbol.isalpha() and 1 <= len(symbol) <= 7:
            return symbol
        print("Invalid stock symbol. Please enter 1-7 capital letters.")


def getChartType():
    while True:
        print("Chart Types\n---------------------")
        print("1. Bar")
        print("2. Line")
        user_input = input("Enter the chart type you want (1, 2): ")
        if user_input.isdigit() and int(user_input) in [1, 2]:
            return int(user_input)
        print("Invalid input. Please enter 1 or 2.")


def getTimeSeriesFunction():
    while True:
        print("Select the Time Series of the chart you want to generate")
        print("--------------------------------------------------------")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        user_input = input("Enter time series function (1, 2, 3, 4): ")
        if user_input.isdigit() and int(user_input) in range(1, 5):
            return int(user_input)
        print("Invalid input. Please enter 1, 2, 3, or 4.")


def validateDate(prompt):
    while True:
        user_input = input(prompt)
        try:
            return datetime.strptime(user_input, '%Y-%m-%d')
        except ValueError:
            print('Invalid date format. Please enter in YYYY-MM-DD format.')


class TestInputValidation(unittest.TestCase):

    @patch('builtins.input', side_effect=['AAPL', 'GOOG', 'INVALID', 'AMZN'])
    def test_getStockSymbol(self, mock_input):
        self.assertEqual(getStockSymbol(), 'AAPL')  
        self.assertEqual(getStockSymbol(), 'GOOG')  

    @patch('builtins.input', side_effect=['1', '2', '3', 'abc'])
    def test_getChartType(self, mock_input):
        self.assertEqual(getChartType(), 1)  
        self.assertEqual(getChartType(), 2)  

    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_getTimeSeriesFunction(self, mock_input):
        self.assertEqual(getTimeSeriesFunction(), 1)  
        self.assertEqual(getTimeSeriesFunction(), 2)  
        self.assertEqual(getTimeSeriesFunction(), 3)  
        self.assertEqual(getTimeSeriesFunction(), 4)  

    @patch('builtins.input', side_effect=['2024-11-15', '2024-01-01'])
    def test_validateDate(self, mock_input):
        self.assertEqual(validateDate("Enter date:"), datetime(2024, 11, 15))
        self.assertEqual(validateDate("Enter date:"), datetime(2024, 1, 1))


if __name__ == '__main__':
    unittest.main()

# run script in terminal with command: python -m unittest mod13_rteq4n.py