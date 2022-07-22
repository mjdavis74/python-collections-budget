from . import Expense
import collections


expenses = Expense.Expenses()
    expenses.read_expenses(data/spending_data.csv)

def spending_categories():
    for expense in expenses.list:
        spending_categories.append(expense.category)


def spending_counter():
    collections.Counter(spending_categories)
        print(spending_counter)
