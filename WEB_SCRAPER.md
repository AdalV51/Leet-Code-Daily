
# Web Scraper Usage Instructions

This document provides a step-by-step guide on how to set up and use the web scraper for LeetCode problems.

## Prerequisites

- Python 3.10
- Git (optional, for cloning the repository)

## Setup and Installation

1. **Clone the Repository** (Optional)
   
   If the code is hosted in a Git repository, clone it to your local machine:

   ```bash
   git clone https://github.com/AdalV51/LeetCode-Daily.git
   cd LeetCode-Daily
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to avoid conflicts with other projects or system-wide Python packages. 

   ```bash
   python3 -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Requirements**

   Install the required packages using the provided `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Scraper

1. **Execute the Script**

   Run `main.py` using Python:

   ```bash
   python main.py
   ```

2. **Enter the LeetCode Problem URL**

   When prompted, enter the URL of the LeetCode problem you wish to scrape. The script will process the URL and scrape the necessary data.

3. **Generated Files**

   After successful execution, the script will generate the following files in a new directory:

   - `README.md`: Contains the formatted problem description.
   - `solution.py`: A placeholder Python file for your solution.

## Notes

- Ensure that your Python version is 3.10 as the script is tested and confirmed to work with this version.
- Always activate the virtual environment (`venv`) before running the script to ensure all dependencies are correctly used.
