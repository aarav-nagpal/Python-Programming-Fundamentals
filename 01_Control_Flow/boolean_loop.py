"""
Basic Control Flow Demonstration
Purpose: Understanding how boolean flags control while-loops.
"""

current_state = True
stop_signal = False

# The loop runs as long as current_state is True
while(current_state):
    print("Hello World")
    
    # Update the state to False to ensure the loop terminates after one run
    current_state = stop_signal
