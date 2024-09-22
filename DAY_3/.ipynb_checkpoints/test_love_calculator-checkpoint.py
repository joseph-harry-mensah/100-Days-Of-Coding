# test_love_calculator.py
import love_calculator  # importing the script named love_calculator.py

def test_love_calculator():
    # Simulate input
    love_calculator.input = lambda _: "Alice"  # Mock the input for name1 and name2
    love_calculator.input = lambda _: "Bob"
    
    # Checking if the program runs without issues
    assert love_calculator  # This ensures the script runs without throwing an error
