import pandas as pd
import matplotlib.pyplot as plt

# Enter the name of the CSV file and read the Excel file into a Pandas DataFrame
filename = input('Enter the CSV file name:')
df = pd.read_csv(filename.strip())


# Group the data by 'Category' and sum the 'Amount' column for each category
category_totals = df.groupby('Category')['Amount'].sum()

# Change all negative values to positive
category_totals = abs(category_totals)

#Sort values from smallest to largest
category_totals = category_totals.sort_values()
#
# # Print out the total for each unique category
for category, total in category_totals.items():
    print(f"{category}: {total:.2f}")


plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%')
plt.title('Total Amount by Category')

# Show the chart
plt.show()
