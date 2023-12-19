# This module contains functions that support the main functionality
# but are not directly involved in data processing or visualization. 
# They perform auxiliary tasks like reading CSV files.

# --- imports --- #
import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog


# --- utility classes --- #
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


# --- utility helpers --- #

# [ check_libraries() ]: check if user has the necessary libraries #
def check_libraries():
	libraries = ["pandas", "matplotlib", "seaborn", "numpy", "tkinter", "wordcloud"]
	missing_libraries = []

	for lib in libraries:
		try:
			__import__(lib)
		except ImportError:
			missing_libraries.append(lib)
	
	return missing_libraries

# [ install_libraries() ]: install missing libraries #
def install_libraries(libraries):
	for lib in libraries:
		subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# [open_dir]: opens folder where output was saved #
#             taking OS into account              #
def open_dir(save_path):
    if sys.platform == 'win32':  # Windows
        os.startfile(save_path)
    elif sys.platform == 'darwin':  # macOS
        subprocess.run(['open', save_path])
    else:  # Linux and Unix-like systems
        subprocess.run(['xdg-open', save_path])



# [ dataview_logo() ]: print DataView ASCII logo #
def dataview_logo():
    logo = """
  ___           _           __   __  _                
 |   \   __ _  | |_   __ _  \ \ / / (_)  ___  __ __ __
 | |) | / _` | |  _| / _` |  \ V /  | | / -_) \ V  V /
 |___/  \__,_|  \__| \__,_|   \_/   |_| \___|  \_/\_/ 
 						   1.0
    """
    print(logo)

# [ read_csv() ]: opening a .csv file custom error handling #
def read_csv(file_path):
	try:
		return pd.read_csv(file_path)
	except Exception as e:
		print(f"{Colors.RED}[ERROR] An error occured importing the .csv: {e}{Colors.RESET}")
		return None

# [ select_columns() ]: show available columns in .csv and ask #
# 					  user which columns they will work with #
def select_columns(df):
	print(f"{Colors.GREEN}Available columns: ", df.columns.tolist(), f"{Colors.RESET}")
	ui_columns = input(f"{Colors.GREEN}Enter the column(s) you want to work with (use , to seperate; no quatation marks): {Colors.RESET}")

	# handle no columns selected
	if not ui_columns:
		print(f"{Colors.RED}[NOTICE] No columns selected. Exiting.{Colors.RESET}")
		sys.exit(1)
	else:
		selected_columns = [col.strip() for col in ui_columns.split(',')]
		return selected_columns

# [ is_num() ]: identifies numerical columns #
def is_num(series):
	if pd.api.types.is_numeric_dtype(series):
		# account for years
		if 'year' in series.name.lower():
			return False
		else:
			return True


# [ is_cat() ]: identifies categorical columns #
def is_cat(series, pd):
	return isinstance(series.dtype, pd.CategoricalDtype) or series.dtype == object