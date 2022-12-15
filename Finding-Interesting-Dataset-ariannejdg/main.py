import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

ph_covid_expenses_data = pandas.read_csv("covid_expenses1.csv")