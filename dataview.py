# DataView 1.0 by George Dreemer (ETA444) #
# Quick way to get basic visualizations and descriptive statistics from a .csv file

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

# --- initial imports --- #
import os
import sys
import subprocess

# --- helper functions --- #
# [ check_libraries() ]: check if user has the necessary libraries #
def check_libraries():
	libraries = ["pandas", "matplotlib", "seaborn", "numpy", "tkinter"]
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


# [ read_csv() ]: opening a .csv file custom error handling #
# args: file_path (file path to the csv); pd (as the pandas module is not globally imported it needs to be provided)
def read_csv(file_path, pd):
	try:
		return pd.read_csv(file_path)
	except Exception as e:
		print(f"{Colors.RED}[ERROR] An error occured importing the .csv: {e}{Colors.RESET}")
		return None

# [ select_columns() ]: show available columns in .csv and ask #
# 					  user which columns they will work with #
def select_columns(df):
	print(f"{Colors.GREEN}Available columns: ", df.columns.tolist(), f"{Colors.RESET}")
	ui_columns = input(f"{Colors.GREEN}Enter the column(s) you want to work with (use , to seperate): {Colors.RESET}")

	# handle no columns selected
	if not ui_columns:
		print(f"{Color.RED}[NOTICE] No columns selected. Exiting.")
		sys.exit(1)
	else:
		selected_columns = [col.strip() for col in ui_columns.split(',')]
		return selected_columns

# [ is_num() ]: identifies numerical columns #
def is_num(series, pd):
	if pd.api.types.is_numeric_dtype(series):
		# account for years
		if 'year' in series.name.lower():
			return False
		else:
			return True


# [ is_cat() ]: identifies categorical columns #
def is_cat(series, pd):
	return isinstance(series.dtype, pd.CategoricalDtype) or series.dtype == object

# [ visualyze_num() ]:  generates appropriate visuals  	#
# 				 	  for numerical data 				#
def visualyze_num (df, column, save_path, plt, sns, style, color):
	# - histogram - #
	# generate histogram
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.histplot(df[column], kde=True, color=color) # dynamic color
	plt.title(f"Histogram of {column}")

	# save histogram
	hist_fname = f"{column}-histogram.png"
	output_histogram = os.path.join(save_path, hist_fname) # dynamic save path
	plt.savefig(output_histogram)
	plt.close()

	# inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved histogram of \'{column}\' column as \'{hist_fname}\' in: {save_path}{Colors.RESET}")

	# - boxplot - #
	# generate boxplot
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.boxplot(y=df[column], color=color) # dynamic color
	plt.title(f"Boxplot of {column}")

	# save boxplot
	box_fname = f"{column}-boxplot.png"
	output_boxplot = os.path.join(save_path, box_fname) # dynamic save path
	plt.savefig(output_boxplot)
	plt.close()

	# inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved boxplot of \'{column}\' column as \'{box_fname}\' in: {save_path}{Colors.RESET}")


# [ visualyze_cat() ]:  generates appropriate visuals 	#
# 				 	  for felines 						#
def visualyze_cat(df, column, save_path, plt, sns, style, color):
	# - bar countplot - #
	# generate countplot
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.countplot(y=df[column], color=color) # dynamic color
	plt.title(f"Count Plot of {column}")

	# save countplot
	count_fname = f"{column}-countplot.png"
	output_countplot = os.path.join(save_path, count_fname) # dynamic save path
	plt.savefig(output_countplot)
	plt.close()

	# inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved countplot of \'{column}\' column as \'{count_fname}\' in: {save_path}{Colors.RESET}")

# [ descrybe_num() ]: calculate descriptive statistics for #
# 					numerical data 						 #
def descrybe_num(df, column, file):
	file.write(f"Statistics for {column}:\n")
	file.write(df[column].describe().to_string())
	file.write("\n\n")

# [ descrybe_cat() ]: calculate descriptive statistics for #
# 					categorical data 					 #
def descrybe_cat(df, column, file):
	file.write(f"Frequency Counts for {column}:\n")
	file.write(df[column].value_counts().to_string())
	file.write("\n\n")	


# --- main function --- #
def dataview():

	# initial dialogue - library check #
	print(f"{Colors.YELLOW}[SETUP] Performing library check ...{Colors.RESET}")
	missing_libraries = check_libraries()

	# setup - handle missing libraries with consent#
	if missing_libraries:
		print(f"{Colors.RED}[SETUP] The following libraries are missing:", ", ".join(missing_libraries), f"{Colors.RESET}")
		
		consent = input(f"{Colors.GREEN}[SETUP] Would you like to install them? (y/n): {Colors.RESET}")
		
		if consent.lower() == 'y':
			install_libraries(missing_libraries)
			print(f"{Colors.BLUE}[SETUP-COMPLETE] Libraries installed successfully, DataView is ready to initialize.{Colors.RESET}")
		else:
			print(f"{Colors.RED}[SETUP-ENDED] DataView relies on these libraries to run.")
			print(f"[SETUP-ENDED] Exiting DataView.{Colors.RESET}")
			sys.exit(1)

	# --- final imports --- #
	import pandas as pd
	import matplotlib.pyplot as plt
	import seaborn as sns
	import numpy as np
	import tkinter as tk
	from tkinter import filedialog

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
	print(f"{Colors.GREEN}[CSV FILE] You will now be prompted to choose your CSV file.{Colors.RESET}")
	file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])

	# main functionality #
	if file_path:
		
		# open a dialog to select the save path of the output #
		print(f"{Colors.CYAN}[SAVE PATH] You will now be prompted to choose your save path for the visualizations and descriptive statistics.{Colors.RESET}")
		save_path = filedialog.askdirectory(title="Select a directory to save visualizations and descriptive statistics")
    	
		if not save_path:
			print(f"{Colors.RED}[NOTICE] No save directory selected. Exiting.{Colors.RESET}")
			sys.exit(1)
		else:
			print(f"{Colors.BLUE}[SUCCESS] Great! Everything will be saved in: {save_path}{Colors.RESET}")

		# define df from .csv file 
		df = read_csv(file_path, pd)

		if df is not None:
			selected_columns = select_columns(df)

		# define save path for descriptives
		# note: for the visuals it is done inside the helper functions
		csv_name_without_extension = (file_path.split('/')[-1]).split('.')[0]
		descriptive_stats_file = os.path.join(save_path, f"descriptivestatistics-{csv_name_without_extension}.txt")

		with open(descriptive_stats_file, 'w') as stats_file:
			for column in selected_columns:
				if is_num(df[column], pd):
					visualyze_num(df, column, save_path, plt, sns)
					descrybe_num(df, column, stats_file)
				elif is_cat(df[column], pd):
					visualyze_cat(df, column, save_path, plt, sns)
					descrybe_cat(df, column, stats_file)
				else:
					print(f"{Colors.RED}[NOTICE] Column {column} is neither strictly numerical nor categorical. No visualizations or descriptives were generated.{Colors.RESET}")
	else:
		print(f"{Colors.RED}[ERROR] No CSV file selected. Exiting.{Colors.RESET}")
		sys.exit(1)

# make sure script runs properly
if __name__ == "__main__":
	dataview()