# Binomial Compensation Calculator

## Overview
This project calculates the binomial probability and expected values to determine the maximum compensation to offer to passengers for oversold flights. The calculation is based on the number of seats, the probability of passengers showing up, and potential losses due to empty seats.

## Features
- **Binomial Probability**: Calculates the probability of `y` passengers showing up.
- **Expected Value**: Calculates the expected number of passengers showing up based on the binomial distribution.
- **Compensation Calculation**: Determines the maximum and average compensation to offer based on probability and loss per seat.

## Files
- `binomial_compensation.py`: Contains functions for binomial probability, expected value, and compensation calculation.
- `main.py`: Runs the program, calculates the results, and displays the binomial probability plot.
- `README.md`: Project instructions and overview.

## Requirements
- Python 3.x
- `matplotlib` for plotting
- `math` for binomial probability calculations

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/binomial-compensation-calculator.git

Install the required packages:
pip install matplotlib
Run the program:

python main.py
## Usage

The program will plot the binomial probability distribution for N=100 and p=0.5.
It will also calculate the maximum compensation to offer based on a set number of oversold seats and probability.
Finally, the program will calculate the average compensation for a range of oversold seats and probabilities.
