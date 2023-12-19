# Welcome to `DataView 1.0`
### Quick way to get basic visualizations and descriptive statistics from a .csv file.

- **Mission:** My mission with DataView is to create a simple way to gain a birds-eye view of a dataset through visualizations and descriptive statistics. With DataView you have beautiful Seaborn plots just a few prompts away.
- **Languages:** This idea started off as a Ruby script, however due to limitations of Ruby when it comes to data science, I have chosen to consolidate it and continue in Python exclusively. The Ruby script is kept as the legacy of the idea (`archive/dataview.rb`).

## Features

- **Visualizations**: Generate various plots for numerical and categorical data, and save them as .PNG.
- **Descriptive Statistics**: Calculate and save descriptive statistics into a .TXT.
- **Customization**: User can choose plot styles and colors.
- **Naming:** From file names, to plot axes and titles, DataView names everything thoughtfully, systematically and intuitively.
- **Ease of Use**: With a few prompts in your terminal you choose your .CSV, then the save path of the output and the colors and style of the plots. Next you specify the columns you want DataView to do its magic on and it's done!

---
## Directory Structure

```
DataView/
│
├── archive/
│   └── dataview.rb # legacy Ruby script
│
├── helpers/
│   ├── utilities.py  # utility functions
│   │   ├── dataview_logo()
│   │   ├── check_libraries()
│   │   ├── install_libraries()
│   │   ├── open_dir()
│   │   ├── read_csv()
│   │   ├── select_columns()
│   │   ├── is_num()
│   │   └── is_cat()
│   │
│   └── generative.py  # visualization and desc. stat.
│       ├── visualyze_num()
│       ├── visualyze_cat()
│       ├── descrybe_num()
│       └── descrybe_cat()
│
├── other/ # other repo resources
│   └── dataview-github-banner-1.PNG 
│
├── test-files/
│   ├── input/  # sample .CSV's
│   │   ├── demographic-data.csv
│   │   ├── movieratings-data.csv
│   │   └── organizations-data.csv
│   │
│   └── output/  # output of DataView on sample .CSV's
│       ├── demographic-data_dataview-output/
│       │   └── ..
│       ├── movieratings-data_dataview-output/
│       │   └── ..
│       └── organizations-data_dataview-output/
│           └── ..
│
│
├── dataview.py        # Main script to run DataView
├── requirements.txt   # Required Python libraries
└── README.md          # Documentation and usage guide

```

### Utilities Module: `utilities.py`
Contains helper functions like: 
- `dataview_logo`: print DataView ASCII logo.
- `check_libraries`: check if user has the necessary libraries.
- `install_libraries`: install missing libraries.
- `open_dir`: opens folder where output was saved taking OS into account.
- `read_csv`: opening a .csv file custom error handling.
- `select_columns`: show available columns in .csv and ask user which columns they will work with.
- `is_num`: identifies numerical columns.
- `is_cat`: identifies feline columns.

As well as class(es):
- `Colors`: contains all the color codes used for prints.

### Generative Module: `generative.py`
Includes functions for generating visualizations and descriptive statistics:
- `visualyze_num`: generates visuals for numerical data, namely:
	- histogram
	- box plot
	- violin plot
	- KDE plot
	- line plot
	- CDF plot
- `visualyze_cat`: generates visuals for categorical data, namely:
	- count plot
	- pie chart
	- donut chart
	- bar plot
	- word cloud
- `descrybe_num`: calculate descriptive statistics for numerical data.
- `descrybe_cat`: calculate descriptive statistics for categorical data.

---
## Installation and Usage

### Prerequisites
- Python 3.x
- Libraries utilized by DataView:
	- pandas
	- matplotlib
	- seaborn
	- numpy
	- wordcloud
	- sys
	- os
	- subprocess
	- tkinter

### Setup
1. Clone the repository:
   ``` bash
   git clone https://github.com/ETA444/dataview.git
   ```
2. Navigate to the DataView directory:
   ```bash
   cd dataview
   ```
3. Install the required libraries*:
   ```bash
   pip install -r requirements.txt
   ```
\* *The script has a built in way of checking and installing (with consent) the missing packages, however you can opt to install them manually, as instructed above.*
### Running DataView
Execute the script and follow the on-screen instructions:
```bash
python dataview.py
```

#### DataView Prompt Sequence
1.  **CSV File:** Opens a browse window so the user can choose the .CSV file
2. **Output Save Path:** Opens a browse window so the user can choose where to save the plots and descriptive statistics files.
3. **Column/Variable Selection:** Lists available variables in the .csv and requests user to type in the names of the desired columns, separated by commas.
4. **Customization - Style:** Asks user to choose an SNS style for the plots.
5. **Customization - Color:** Asks use to choose color for the plots.

---
## Contributing
Contributions to DataView are welcome. Feel free to fork the repository, make changes, and submit pull requests.

