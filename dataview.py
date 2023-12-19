# --- nonconditional library imports --- #
import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog

# --- helper function imports --- #
from helpers.utilities import check_libraries, install_libraries, open_dir, dataview_logo, read_csv, select_columns, is_num, is_cat
from helpers.generative import visualyze_cat, visualyze_num, descrybe_num, descrybe_cat

# --- classes --- #
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

# --- main function --- #
def dataview():

	# - library check dialogue - #
	print(f"{Colors.YELLOW}[SETUP] Performing library check ...{Colors.RESET}")
	missing_libraries = check_libraries()

	# - missing libraries handling - #
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


	# - welcome dialogue - #
	print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
	dataview_logo()
	print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
	print(f"{Colors.WHITE} Welcome to DataView! (version 1.0){Colors.RESET}")
	#print(f"Functionality: ")
	print(f"{Colors.BLUE}[DATA-quality] DataView only works with clean data in CSV format.")
	print(f"[DATA-types] DataView distinguishes between numerical and categorical data and generates the appropriate plots and descriptive statistics.{Colors.RESET}")
	print(f"{Colors.CYAN}[OUTPUT] DataView saves the plots to a folder chosen by you.{Colors.RESET}")
	print(f"{Colors.GREEN}[PLOTS-Numerical] For numerical data, DataView generates: histograms, box plots, violin plots, KDE plots, line plots and CDF plots.")
	print(f"{Colors.GREEN}[PLOTS-Categorical] For categorical data, DataView generates: count plots, pie charts, donut charts, bar plots and word clouds.{Colors.RESET}")
	print(f"{Colors.MAGENTA}[CUSTOMIZATION-Style & Color] You can choose the style and color of the plots.{Colors.RESET}")
	print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
	
	# - select CSV file: setting up tk - #
	root = tk.Tk()
	root.withdraw()

	# - select CSV file: dialogue - #
	print(f"{Colors.BLUE}[CSV FILE] You will now be prompted to choose your CSV file.{Colors.RESET}")
	file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
	print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
	
	if file_path:
		
		# - select SAVE path - #
		print(f"{Colors.CYAN}[SAVE PATH] You will now be prompted to choose your save path for the visualizations and descriptive statistics.{Colors.RESET}")
		save_path = filedialog.askdirectory(title="Select a directory to save visualizations and descriptive statistics")
    	
    	# - checking SAVE path - #
		if not save_path:
			print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
			print(f"{Colors.RED}[NOTICE] No save directory selected. Exiting.{Colors.RESET}")
			sys.exit(1)
		else:
			print(f"{Colors.BLUE}[SUCCESS] Great! Everything will be saved in: {save_path}{Colors.RESET}")
			print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
		
		# - create local dataframe to work with - #
		df = read_csv(file_path)

		# - style and color customization - #
		if df is not None:
			selected_columns = select_columns(df)
			# color and style dialog
			style = input(f"{Colors.MAGENTA}[CUSTOMIZATION-STYLE] What style would you like the plots to have? \n (darkgrid / whitegrid / dark / white / ticks / ...): {Colors.RESET}")
			print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
			color = input(f"{Colors.MAGENTA}[CUSTOMIZATION-COLOR] What color would you like the main color of the plots to be? \n (skyblue / salmon / lightgreen / sandybrown / orchid / steelblue / ...): {Colors.RESET}")
			print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
		
		# - set up descriptives save path - #
		# note: for the visuals it is done inside the helper functions
		csv_name_without_extension = (file_path.split('/')[-1]).split('.')[0]
		descriptive_stats_file = os.path.join(save_path, f"descriptivestatistics-{csv_name_without_extension}.txt")

		# - generate ouput - #
		with open(descriptive_stats_file, 'w') as stats_file:
			for column in selected_columns:
				if is_num(df[column]):
					visualyze_num(df, column, save_path, style, color)
					descrybe_num(df, column, stats_file)
				elif is_cat(df[column]):
					visualyze_cat(df, column, save_path, style, color)
					descrybe_cat(df, column, stats_file)
				else:
					print(f"{Colors.RED}[NOTICE] Column {column} is neither strictly numerical nor categorical. No visualizations or descriptives were generated.{Colors.RESET}")
		print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
		print(f"{Colors.BLUE}[SUCCESS] Plots and Descriptive Statistics have been generated! Opening the folder ...{Colors.RESET}")
		open_dir(save_path)
	else:
		print(f"{Colors.RED}[ERROR] No CSV file selected. Exiting.{Colors.RESET}")
		sys.exit(1)

if __name__ == "__main__":
	dataview()