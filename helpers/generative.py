# This module is focused on the core functionality of DataView, 
# generating visualizations and descriptive statistics 
# for numerical and categorical data.

# --- imports --- #
import os
import sys
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import wordcloud
from wordcloud import WordCloud


# --- generative helpers --- #

# [ visualyze_num() ]:  generates appropriate visuals  	#
# 				 	  for numerical data 				#
def visualyze_num (df, column, save_path, style, color):
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
def visualyze_cat(df, column, save_path, style, color):
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