# Python Number File Processor

## Overview
Python Number File Processor is a Python-based application designed to read and manipulate a list of numbers stored in a text file through a graphical user interface (GUI). The application can create a new file if the specified data file does not exist. It provides various functionalities, including sorting numbers, calculating their total and average, searching for occurrences, appending random numbers, and encrypting or decrypting the file content.

## Motivation
This project was developed during my Python learning phase to enhance my skills in scripting with Python. It focuses on basic file operations, GUI design using Tkinter, and encryption techniques.

## Features
- **Select / Create Data File**: Choose an existing text file or create a new one for storing numerical data.
- **Display All Numbers**: View all numbers in the selected file, along with their total and average.
- **Sort Numbers**: Display all numbers sorted from smallest to largest.
- **Search Number**: Search for a specific number within the file and display its frequency of occurrence.
- **Display Largest Number**: Show the largest number in the data file.
- **Append Random Numbers**: Add one or more randomly generated numbers to the data file.
- **Encrypt File**: Secure the contents of the file using the Caesar cipher encryption method.
- **Decrypt File**: Revert the encrypted file content back to its original form using the same encryption method.
- **Exit**: Close the application.

## Technologies Used
- **Python 3**: Developed using Python 3, utilizing its standard libraries.
- **Tkinter**: Used for creating the GUI, providing an interactive interface with buttons, labels, and dialogs.
- **Random**: A standard Python library for generating random numbers to append to the file.
- **Caesar Cipher**: A basic encryption technique used to secure file contents.

## Setup Instructions

### Prerequisites
- **Python 3**: Ensure Python 3 is installed on your machine. [Download Python](https://www.python.org/).
- **Tkinter**: Confirm Tkinter is available with your Python installation. It is usually bundled with most Python setups. If missing, install it using:
  ```bash
  sudo apt-get install python3-tk  # For Ubuntu/Linux
## Installation Steps
1. Clone the Repository: Download the project files from GitHub

   git clone https://github.com/jay-gajjar7/Python-Number-File-Processor
   
3. Open the Project: Load the project into PyCharm or any Python IDE of your choice.
   
4. Run the Application: Execute the main script from your IDE to launch the application.

## Usage Guide
1. Launch the Application: Run the main script to open the GUI window with several buttons corresponding to different functionalities.
2. Select / Create File: Use this option to choose an existing text file or create a new file for storing numbers.
3. Display All: Click to view all numbers in the file along with their total sum and average.
4. Sort Numbers: Click to sort the numbers in ascending order.
5. Search Number: Enter a specific number to search for within the file and see how many times it appears.
6. Largest Number: Displays the largest number found in the file.
7. Append Random Number: Adds one or more randomly generated numbers between 1 and 1000 to the file.
8. Encrypt File: Encrypts the content of the file using a Caesar cipher with a shift key of 5.
9. Decrypt File: Decrypts the previously encrypted file content back to its original state.
10. Exit: Closes the application.  

## Future Enhancements
- **Improved Encryption**: Explore more advanced encryption methods to enhance file security.
- **User Customization**: Allow users to set custom encryption keys and random number ranges.
- **Extended File Format** Support: Expand support to other file formats like CSV or JSON.
- **Enhanced Error Handling**: Improve error messages and handling for a more robust user experience.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Python.org for providing comprehensive documentation and resources.
