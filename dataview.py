# --- legend --- #
# ui = user input

# --- colors for output --- #
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

# [check_libraries]: check if user has the necessary libraries #
import sys
def check_libraries():
	libraries = ["pandas", "matplotlib", "seaborn", "numpy", "tkinter"]
	missing_libraries = []

	for lib in libraries:
		try:
			__import__(lib)
		except ImportError:
			missing_libraries.append(lib)
	
	return missing_libraries

# --- main function --- #
def dataview():
	# initial dialogue - library check #
	print(f"{Colors.RED} Performing library check ...")
	missing_libraries = check_libraries()
	if missing_libraries:
		print("The following required libraries are missing:")
		print(", ".join(missing_libraries))
		print("Please install them before running this script.")
		sys.exit(1)

	# welcome dialogue #
	print(f"{Colors.BLUE} Welcome to DataView! (version 1.0)")
	print(f"Notes: ")
	print(f"(1) DataView 1.0 only works with clean data.")
	print(f"(2) DataView 1.0 distinguishes between numerical and categorical data and generates the appropriate visuals and descriptive statistics.")
	print(f"(3) DataView 1.0 generates: histograms, boxplots and countplots as .PNG\'s.")
	print(f"(4) The descriptive statistics are saved into .TXT\'s.")
	print(f"* All files are saved in the current directory. *{Colors.RESET}")

	# set up a root window for tk but don't display it #
	root = tk.Tk()
	root.withdraw()

	# open a file dialog to select the CSV file #
	file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])

	# main functionality #
	if file_path:
		df = read_csv(file_path)
		
		if df is not None:
			selected_columns = select_columns(df)

		with open(f"descriptivestatistics-{file_path.split('/')[-1]}.txt", 'w') as stats_file:
			for column in selected_columns:
				if is_num(df[column]):
					visualyze_num(df, column)
					descrybe_num(df, column, stats_file)
				elif is_cat(df[column]):
					visualyze_cat(df, column)
					descrybe_cat(df, column, stats_file)
				else:
					print(f"{Colors.RED}[NOTICE] Column {column} is neither strictly numerical nor categorical. No visualizations or descriptives were generated.{Colors.RESET}")
	else:
		print(f"{Colors.RED}[ERROR] No CSV file selected.{Colors.RESET}")

# make sure script runs properly
if __name__ == "__main__":
	dataview()

# --- required libraries --- #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import tkinter as tk
from tkinter import filedialog

# --- accessory functions --- #
 
# [read_csv()]: opening a .csv file custom error handling #
def read_csv(file_path):
	try:
		return pd.read_csv(file_path)
	except Exception as e:
		print(f"{Colors.RED}[ERROR] An error occured importing the .csv: {e}{Colors.RESET}")
		return None

# [select_columns()]: show available columns in .csv and ask #
# 					  user which columns they will work with #
def select_columns(df):
	print(f"{Colors.BLUE}Available columns: ", df.columns.tolist())
	ui_columns = input(f"{Colors.GREEN}Enter the column(s) you want to work with (use , to seperate): {Colors.RESET}")
	selected_columns = [col.strip() for col in ui_columns(',')]
	return selected_columns

# [is_num()]: identifies numerical columns #
def is_num(series):
	return pd.api.types.is_numeric_dtype(series)

# [is_cat()]: identifies categorical columns #
def is_cat(series):
	return pd.api.types.is_categorical_dtype(series) or series.dtype == object

# [visualyze_num()]:  generates appropriate visuals  	#
# 				 	  for numerical data 				#
def visualyze_num (df, column):
	# histogram #
	plt.figure(figsize=(10,6))
	sns.histplot(df[column], kde=True)
	plt.title(f"Histogram of {column}")
	hist_fname = f"{column}-histogram.png"
	plt.savefig(hist_fname)
	plt.close()
	print(f"{Colors.BLUE} Saved histogram of \'{column}\' column as \'{hist_fname}\' in the current directory.{Colors.RESET}")

	# boxplot #
	plt.figure(figsize=(10,6))
	sns.boxplot(y=df[column])
	plt.title(f"Boxplot of {column}")
	box_fname = f"{column}-boxplot.png"
	plt.savefig(box_fname)
	plt.close()
	print(f"{Colors.BLUE} Saved boxplot of \'{column}\' column as \'{box_fname}\' in the current directory.{Colors.RESET}")


# [visualyze_cat()]:  generates appropriate visuals 	#
# 				 	  for felines 						#
def visualyze_cat(df, column):
	# bar countplot #
	plt.figure(figsize=(10,6))
	sns.countplot(y=df[column])
	plt.title(f"Count Plot of {column}")
	count_fname = f"{column}-countplot.png"
	plt.savefig(count_fname)
	plt.close()
	print(f"{Colors.BLUE} Saved countplot of \'{column}\' column as \'{count_fname}\' in the current directory.{Colors.RESET}")

# [descrybe_num()]: calculate descriptive statistics for #
# 					numerical data 						 #
def descrybe_num(df, column, file):
	file.write(f"Statistics for {column}:\n")
	file.write(df[column].describe().to_string())
	file.write("\n\n")

# [descrybe_cat()]: calculate descriptive statistics for #
# 					categorical data 					 #
def descrybe_cat(df, column, file):
	file.write(f"Frequency Counts for {column}:\n")
	file.write(df[column].value_counts().to_string())
	file.write("\n\n")