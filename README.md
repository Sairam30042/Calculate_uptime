# Charger Uptime Calculation Tool

This tool calculates the uptime percentage for charging stations based on the availability reports of individual chargers. It processes input files containing station and charger data, computes the uptime, and outputs the results.

## System Requirements

- Python 3.6 or higher

## File Structure

- `calculate_uptime.py`: The main Python script that reads input data, calculates uptime, and prints results.
- `test_calculate_uptime.py`: The unit test script for testing the functionality of the uptime calculation.

## Installation

No installation is required, other than having Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/) if it's not already installed.

## How to Run the Tool

1. **Prepare Your Input File**: Ensure your input file is in the correct format. The file should consist of two sections:
   - **Stations Section**: Lists station IDs followed by the charger IDs at that station.
   - **Charger Availability Reports Section**: Lists charger IDs with their respective up and down times.

Example format:
[Stations] 0 1001 1002 1 1003 2 1004

[Charger Availability Reports] 1001 0 50000 true 1001 50000 100000 true 1002 50000 100000 true 1003 25000 75000 false 1004 0 50000 true 1004 100000 200000 true


2. **Run the Script**: Navigate to the directory containing `calculate_uptime.py` and run the following command in the terminal:
   ```bash
   python calculate_uptime.py path/to/your/input_file.txt

3. **How to Run Tests**
Ensure you have the test input files in the test_data/ directory. Run the test script from the terminal:

bash
Copy code
python test_calculate_uptime.py
This will execute all defined test cases based on the input files specified in the test_calculate_uptime.py script.
Make sure the path for the inputs are correctly handled in test_calculate_uptime.py

Understanding the Output
The script outputs the station ID followed by the uptime percentage, rounded down to the nearest integer. The output is printed directly to the console.

Example output:

Copy code
0 100
1 0
2 75
This indicates that Station 0 had 100% uptime, Station 1 had 0% uptime, and Station 2 had 75% uptime.