import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# a) Line Plot (Total Profit)
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline Plot
plt.plot(df['month'], df['facecream'], label='Face Cream')
plt.plot(df['month'], df['facewash'], label='Face Wash')
plt.plot(df['month'], df['toothpaste'], label='Toothpaste')
plt.legend()
plt.title("Product Sales Data")
plt.show()

# c) Bar Chart (Face Cream & Face Wash)
plt.bar(df['month'], df['facecream'], label='Face Cream')
plt.bar(df['month'], df['facewash'], label='Face Wash')
plt.legend()
plt.title("Face Cream & Face Wash Sales")
plt.show()

# d) Pie Chart (Total Sales of each product)
products = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
total_sales = [df[p].sum() for p in products]

plt.pie(total_sales, labels=products, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()