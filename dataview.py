# --- required libraries --- #
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
 
# [read_csv(): opening a .csv file custom error handling #
def read_csv(file_path):
	try:
		return pd.read_csv(file_path)
	except Exception as e:
		print(f"{Colors.RED}An error occured importing the .csv: {e}")
		return None

# [()]:



# --- main function --- #



# --- test area --- #

# test colors print(f"{Colors.GREEN} Hello !{Colors.RESET}")