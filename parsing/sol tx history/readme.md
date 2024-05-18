# Parsing from solscan

## Overview
This repository contains tools for parsing and merging various file types, particularly focusing on CSV files. It provides a graphical user interface (GUI) for easy file merging and visualizing data loss.

## Repository Structure
- **sol tx history/**: Directory containing historical transaction data.
- **combined_sol_transfers.txt**: Combined text file of SOL transfers.
- **combined_values.csv**: Combined CSV file of values.
- **merge_files.py**: Script to merge various file types into one.
- **visual_of_data_loss.py**: Script to visualize data loss.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries:
    ```sh
    pip install tkinter pandas matplotlib seaborn python-docx
    ```

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ryanshatch/Rugs-and-Scams.db.git
    ```
2. Navigate to the `parsing` directory:
    ```sh
    cd Rugs-and-Scams.db/parsing
    ```

### Usage

#### File Merger
1. Run the `merge_files.py` script to open the GUI:
    ```sh
    python merge_files.py
    ```
2. Use the GUI to:
   - Browse and select multiple files to combine.
   - Enter a name for the new combined file.
   - Click "CREATE" to merge the selected files into one.
   - The combined file will be saved as a `.txt` file, and a CSV file will be created for better readability.

#### Visualize Data Loss
1. Run the `visual_of_data_loss.py` script to visualize data loss:
    ```sh
    python visual_of_data_loss.py
    ```

## License
This project was developed and is under copyright by Ryan Hatch