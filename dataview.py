# --- required libraries --- #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- legend --- #
# ui = user input

# --- colors for output --- #
# example usage: print(f"{Colors.GREEN}This is green text!{Colors.RESET}")
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


# --- accessory functions --- #
 
# [read_csv()]: opening a .csv file custom error handling #
def read_csv(file_path):
	try:
		return pd.read_csv(file_path)
	except Exception as e:
		print(f"{Colors.RED}An error occured importing the .csv: {e}")
		return None

# [choose_columns()]: show available columns in .csv and ask #
# 					  user which columns they will work with #
def choose_columns(df):
	print(f"{Colors.BLUE}Available columns: ", df.columns.tolist())
	ui_columns = input(f"{Colors.GREEN}Enter the column(s) you want to work with (use , to seperate): ")
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
	print(f"{Colors.BLUE} Saved histogram of \'{column}\' column as \'{hist_fname}\'")

	# boxplot #
	plt.figure(figsize=(10,6))
	sns.boxplot(y=df[column])
	plt.title(f"Boxplot of {column}")
	box_fname = f"{column}-boxplot.png"
	plt.savefig(box_fname)
	plt.close()
	print(f"{Colors.BLUE} Saved boxplot of \'{column}\' column as \'{box_fname}\'")


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
	print(f"{Colors.BLUE} Saved countplot of \'{column}\' column as \'{count_fname}\'")

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

# --- main function --- #



# --- test area --- #

# test colors print(f"{Colors.GREEN} Hello !{Colors.RESET}")