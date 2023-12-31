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
	ui_columns = input(f"{Colors.GREEN}Enter the column(s) you want to work with (use , to seperate; no quatation marks): {Colors.RESET}")

	# handle no columns selected
	if not ui_columns:
		print(f"{Colors.RED}[NOTICE] No columns selected. Exiting.{Colors.RESET}")
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
# generates: histogram, box plot, violin plot, KDE plot, line plot, CDF plot
	
	# - histogram - #
	## generate histogram
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.histplot(df[column], kde=True, color=color) # dynamic color
	plt.title(f"Histogram of {column}")

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save histogram
	hist_fname = f"{column}-histogram-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, hist_fname)) # dynamic save path
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved histogram of \'{column}\' column as \'{hist_fname}\' in: {save_path}{Colors.RESET}")

	# - boxplot - #
	## generate boxplot
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.boxplot(y=df[column], color=color) # dynamic color
	plt.title(f"Boxplot of {column}")

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save boxplot
	box_fname = f"{column}-boxplot-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, box_fname)) # dynamic save path
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved boxplot of \'{column}\' column as \'{box_fname}\' in: {save_path}{Colors.RESET}")


	# - violin plot - #
	## generate violin plot
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.violinplot(y=df[column], color=color) # dynamic color
	plt.title(f"Violin Plot of {column}")

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save boxplot
	violin_fname = f"{column}-violinplot-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, violin_fname)) # dynamic save path
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved violin plot of \'{column}\' column as \'{violin_fname}\' in: {save_path}{Colors.RESET}")


	# - KDE plot - #
	## generate KDE plot
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.kdeplot(df[column], color=color, fill=True) # dynamic color
	plt.title(f"KDE Plot of {column}")
	
	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save KDE plot
	kde_fname = f"{column}-kdeplot-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, kde_fname)) # dynamic save path
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved KDE plot of \'{column}\' column as \'{kde_fname}\' in: {save_path}{Colors.RESET}")


	# - line plot - #
	## generate line plot
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.lineplot(data=df[column], color=color) # dynamic color
	plt.title(f"Line Plot of {column}")

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save line plot
	line_fname = f"{column}-lineplot-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, line_fname)) # dynamic save path
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved line plot of \'{column}\' column as \'{line_fname}\' in: {save_path}{Colors.RESET}")


	# - CDF plot - #
	## generate CDF plot
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.ecdfplot(df[column], color=color) # dynamic color
	plt.title(f"CDF Plot of {column}")

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save CDF plot
	cdf_fname = f"{column}-cdfplot-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, cdf_fname)) # dynamic save path
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved CDF plot of \'{column}\' column as \'{cdf_fname}\' in: {save_path}{Colors.RESET}")





# [ visualyze_cat() ]:  generates appropriate visuals 	#
# 				 	  for felines 						#
def visualyze_cat(df, column, save_path, plt, sns, style, color):
# generates: count plot, pie chart, donut chart, bar plot, word cloud
	
	# - vertical count plot - #
	## generate count plot
	plt.figure(figsize=(10,6))
	sns.set_style(style) # dynamic style
	sns.countplot(y=df[column]) # dynamic color
	plt.title(f"Count Plot of {column}")

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save countplot
	count_fname = f"{column}-countplot-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, count_fname)) # dynamic save path
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved countplot of \'{column}\' column as \'{count_fname}\' in: {save_path}{Colors.RESET}")


	# - pie chart - #
	## generate pie chart (note: color and style limited)
	plt.figure(figsize=(8, 8))
	df[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
	plt.title(f"Pie Chart of {column}")
	plt.ylabel('')  # y label not needed in pie plot

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save pie chart
	pie_fname = f"{column}-piechart-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, pie_fname))
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved countplot of \'{column}\' column as \'{pie_fname}\' in: {save_path}{Colors.RESET}")


	# - donut chart - #
	plt.figure(figsize=(8, 8))
	plt.pie(df[column].value_counts(), labels=df[column].value_counts().index, autopct='%1.1f%%', startangle=90)
	plt.gca().add_artist(plt.Circle((0,0),0.70,fc='white'))
	plt.title(f"Donut Chart of {column}")

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save donut chart
	donut_fname = f"{column}-donutchart-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, donut_fname))
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved donut chart of \'{column}\' column as \'{donut_fname}\' in: {save_path}{Colors.RESET}")


	# - horizontal bar chart - #
	plt.figure(figsize=(10, 6))
	sns.set_style(style) # dynamic style
	sns.barplot(x=df[column].value_counts(), y=df[column].value_counts().index, color=color) # dynamic color
	plt.title(f"Bar Chart of {column}")
	plt.xlabel('Count')

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save bar chart
	bar_fname = f"{column}-barchart-{style}-{color}.png"
	plt.savefig(os.path.join(save_path, bar_fname))
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved bar chart of \'{column}\' column as \'{bar_fname}\' in: {save_path}{Colors.RESET}")


	# - word cloud - #
	from wordcloud import WordCloud # local import

	## generate word cloud
	wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(' '.join(df[column]))
	plt.figure(figsize=(10, 5))
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis('off')
	plt.title(f"Word Cloud of {column}")

	## DataView branding
	plt.text(x=0.5, y=-0.05, s="Made with DataView (github.com/ETA444)", 
				fontsize=10, ha='center', va='bottom', color='grey', 
					transform=plt.gca().transAxes)

	## save word cloud
	cloud_fname = f"{column}-wordcloud.png"
	plt.savefig(os.path.join(save_path, cloud_fname))
	plt.close()

	## inform user
	print(f"{Colors.BLUE}[SUCCESS] Saved word cloud of \'{column}\' column as \'{cloud_fname}\' in: {save_path}{Colors.RESET}")

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
	
	# set up a root window for tk but don't display it #
	root = tk.Tk()
	root.withdraw()

	# open a file dialog to select the CSV file #
	print(f"{Colors.BLUE}[CSV FILE] You will now be prompted to choose your CSV file.{Colors.RESET}")
	file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
	print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
	# main functionality #
	if file_path:
		
		# open a dialog to select the save path of the output #
		print(f"{Colors.CYAN}[SAVE PATH] You will now be prompted to choose your save path for the visualizations and descriptive statistics.{Colors.RESET}")
		save_path = filedialog.askdirectory(title="Select a directory to save visualizations and descriptive statistics")
    	
		if not save_path:
			print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
			print(f"{Colors.RED}[NOTICE] No save directory selected. Exiting.{Colors.RESET}")
			sys.exit(1)
		else:
			print(f"{Colors.BLUE}[SUCCESS] Great! Everything will be saved in: {save_path}{Colors.RESET}")
			print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
		# define df from .csv file 
		df = read_csv(file_path, pd)

		if df is not None:
			selected_columns = select_columns(df)
			# color and style dialog
			style = input(f"{Colors.MAGENTA}[CUSTOMIZATION-STYLE] What style would you like the plots to have? \n (darkgrid / whitegrid / dark / white / ticks / ...): {Colors.RESET}")
			print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
			color = input(f"{Colors.MAGENTA}[CUSTOMIZATION-COLOR] What color would you like the main color of the plots to be? \n (skyblue / salmon / lightgreen / sandybrown / orchid / steelblue / ...): {Colors.RESET}")
			print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
		
		# define save path for descriptives
		# note: for the visuals it is done inside the helper functions
		csv_name_without_extension = (file_path.split('/')[-1]).split('.')[0]
		descriptive_stats_file = os.path.join(save_path, f"descriptivestatistics-{csv_name_without_extension}.txt")

		with open(descriptive_stats_file, 'w') as stats_file:
			for column in selected_columns:
				if is_num(df[column], pd):
					visualyze_num(df, column, save_path, plt, sns, style, color)
					descrybe_num(df, column, stats_file)
				elif is_cat(df[column], pd):
					visualyze_cat(df, column, save_path, plt, sns, style, color)
					descrybe_cat(df, column, stats_file)
				else:
					print(f"{Colors.RED}[NOTICE] Column {column} is neither strictly numerical nor categorical. No visualizations or descriptives were generated.{Colors.RESET}")
		print(f"{Colors.WHITE}-----------------------------------------------------------------------------{Colors.RESET}")
		print(f"{Colors.BLUE}[SUCCESS] Plots and Descriptive Statistics have been generated! Opening the folder ...{Colors.RESET}")
		open_dir(save_path)
	else:
		print(f"{Colors.RED}[ERROR] No CSV file selected. Exiting.{Colors.RESET}")
		sys.exit(1)

# make sure script runs properly
if __name__ == "__main__":
	dataview()