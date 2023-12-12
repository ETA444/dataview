# required packages dialogue & installation #
puts "This program makes use of the following gems: \n - csv \n - colorize \n - rubyplot \n - descriptive_statistics"
puts "Do you want to install them? (y/n): "
package_install = gets.chomp.downcase
if package_install == 'y'
	puts 'Installing ...'
	gem 'csv'
	gem 'colorize'
	gem 'rubyplot'
	gem 'descriptive_statistics'
	require 'csv'
	require 'colorize'
	require 'rubyplot'
	require 'descriptive_statistics'
	puts 'Installations complete!'.colorize(:light_blue)
	puts '------------------------'
else
	# check for the installations regardless #
	begin
  		require 'csv'
	rescue LoadError
  		puts "The 'csv' gem is not installed. Please run 'gem install csv' to install it."
  		exit
	end

	begin
		require 'colorize'
	rescue LoadError
  		puts "The 'colorize' gem is not installed. Please run 'gem install colorize' to install it."
  		exit
	end

	begin
		require 'rubyplot'
	rescue LoadError
  		puts "The 'rubyplot' gem is not installed. Please run 'gem install rubyplot' to install it."
  		exit
	end

	begin
		require 'descriptive_statistics'
	rescue LoadError
  		puts "The 'descriptive_statistics' gem is not installed. Please run 'gem install descriptive_statistics' to install it."
  		exit
	end

end

# welcome dialogue and info gathering/preparation #
puts "Welcome to DataView! (version 1.0)".colorize(:light_blue)

## get the file path
puts "Please enter the full file path to your CSV file: ".colorize(:green)
file_path = gets.chomp
puts "Great, got it.".colorize(:light_blue)
puts "------------------------"

## handle .csv without headers
puts "Does your CSV file have headers? (y/n): ".colorize(:green)
headers = gets.chomp.downcase

if headers == 'y'
	begin 
		csv_data = CSV.read(file_path, headers: true)
	rescue # file path custom error handling
		puts "Error reading file. Please check the file path and try again.".colorize(:red)
		exit
	end
else
	puts "DataView relies on headers to work. Please add headers or use another file.".colorize(:red)
	exit
end

## choosing the columns to work with
puts "Available columns: #{csv_data.headers.join(', ')}".colorize(:yellow)
puts "------------------------"
puts "Note: ".colorize(:light_blue)
puts "(1) DataView 1.0 only works with clean data.".colorize(:light_blue)
puts "(2) DataView 1.0 needs you to distinguish between column data type to generate appropriate visualizations and descriptive statistics.".colorize(:light_blue)
puts "------------------------"

## get column names (*distinction between numerical and categorical columns)
### numerical
puts "Please enter the numerical column names, seperated by commas. (type 'none' to skip): ".colorize(:green)
num_columns = gets.chomp.split(',').map(&:strip)

if num_columns == 'none'
	## categorical columns
	puts "Please enter the categorical column names, seperated by commas: ".colorize(:green)
	cat_columns = gets.chomp.split(',').map(&:strip)

	if cat_columns == 'none'
		puts "You can't skip both data types.".colorize(:red)
	end
else
	puts "Please enter the categorical column names, seperated by commas. (type 'none' to skip): ".colorize(:green)
	cat_columns = gets.chomp.split(',').map(&:strip)
end

# start handling the data #
puts "Got it!".colorize(:light_blue)
puts "Generating visualizations ...".colorize(:light_blue)


## generative functions using rubyplot and descriptive_statistics

### for numerical ###
# for numerical data some useful visualizations may be the histogram and boxplot
# the usual descriptives are also mean-ingful :D (mean, median, etc.)
def generate_histogram(data, column_name)
	# creating the histogram
	histogram = Rubyplot::Histogram.new
 	histogram.data column_name, data

	# naming convention of files
	histogram.write("#{column_name}-histogram-#{rand(100..999)}.png")
end

def generate_boxplot(data, column_name)
	
	# creating the boxplot
	boxplot = Rubyplot::BoxPlot.new
	boxplot.data column_name, data

	# naming convention of the files
	boxplot.write("#{column_name}-boxplot-#{rand(100..999)}.png")

end

def calculate_descriptive_statistics(data, column_name)
	# descstats object
	stats = data.descriptive_statistics
	
	# create the file and input the data
	File.open("descriptivestatistics-#{column_name}.txt", 'w') do |file|
		file.puts "Statistics for #{column_name}:"
		stats.each { |key, value| file.puts "#{key}: #{value}" }
	end
end

### for categorical ###
# for categorical the above functions are not very useful
# I create seperate visualiztion such as a bar chart
# for the descriptives I focus on frequency and count of categories

def generate_bar_chart(data, column_name)
	# count the frequency of each category
	category_counts = data.each_with_object(Hash.new(0)) { |value, counts| counts[value] += 1 }

	# create a bar chart
	bar_chart = Rubyplot::Bar.new
	category_counts.each do |category, count|
		bar_chart.data category, [count]
	end

	# naming convention of the files
	bar_chart.write("#{column_name}-barchart-#{rand(100..999)}.png")
end

def calculate_categorical_statistics(data, column_name)
	# count the frequency of each category
	category_counts = data.each_with_object(Hash.new(0)) { |value, counts| counts[value] += 1 }

	# create file and input the data
	File.open("categoricalstats-#{column_name}.txt", 'w') do |file|
		file.puts "Category counts for #{column_name}:"
		category_counts.each { |category, count| file.puts "#{category}: #{count}" }
	end
end


## logic flow: numerical vs. categorical
## Handling the data based on either scenario

if num_columns != 'none'
	num_columns.each do |col|
		data = csv_data[col] #get the data
		generate_histogram(data, col) #histogram per column
		generate_boxplot(data, col) #boxplot per column
		calculate_descriptive_statistics(data, col) # descstats per column
  	end
end

if cat_columns != 'none'
	num_columns.each do |col|
		data = csv_data[col] #get the data
		generate_histogram(data, col) #histogram per column
		generate_boxplot(data, col) #boxplot per column
		calculate_descriptive_statistics(data, col) # descstats per column
  	end
end





