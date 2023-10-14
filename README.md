# seq_bank

## Description
a simulator to generate LC-MS datasets for given or random RNA sequences.

## System Requirements

### Software requirements
The project has been tested on macOS(Sonoma 14.0).

#### Python dependencies
1. Python version 3.7+ is required. Go to the [Python Website]( https://www.python.org/downloads/) to download python and follow the instruction for installation.
2. The rest dependencies are listed inside requirements.txt, please refer to the [Prepare the Environment](#prepare-the-environment) section on how to install them. They should install within 1 minute, depending on your network speed.

## Download
Clone this repository. Click the green button "Code" and click the "Download ZIP" button. Now a zip file named "seq_bank-main.zip" is downloaded. Unzip this file. In macOS/Linux system, usually the path of the project is ~/Downloads/seq_bank-main. 

## Prepare the Environment 
1. Open the Terminal.
2. Create an virtual environment by entering the following command
```Bash
python3 -m venv <your_virtual_workspace_path>
```
To make it simple, we can setup the virtual environment "vir_env" in "Downloads" folder by entering the command
```Bash
python3 -m venv ~/Downloads/vir_env
```
3. Activate the virtual environment
```Bash
source <your_virtual_workspace_path>/bin/activate
```
In our case, enter the command
```Bash
source ~/Downloads/vir_env/bin/activate
```
4. Go to the root directory of seq_bank project and install all the required libraries. Enter the command
```Bash
cd <root_directory_path>
pip install -r requirements.txt
```
In our case, enter
```Bash
cd ~/Downloads/seq_bank-main
pip install -r requirements.txt
```

## Sequences Simulation
Run the following command to generate LC-MS dataset for given RNA sequences.
```Bash
python seq_bank/process.py -s <seq1,seq2,...>
```
Run the following command to generate LC-MS dataset for random sequences.
```Bash
python seq_bank/process.py -n <number_of_sequences> -l <length_of_sequence>
```

## Help
Run the following command for more instructions.
```Bash
python seq/process.py --help
```

