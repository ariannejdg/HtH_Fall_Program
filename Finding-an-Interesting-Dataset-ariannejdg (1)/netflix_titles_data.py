import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

netflix_titles_data = pandas.read_csv("netflix_titles.csv")