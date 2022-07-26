from . import Expense


def expenses():
    expenses = Expense.Expenses()
    expenses.read_expenses(data/spending_data.csv)


def spending_categories([]):
    for expense in expenses.list:
        spending_categories.append(expense.category)
