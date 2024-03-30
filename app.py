from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (you can replace this with database integration)
a=int(input("enter amount for food"))
b=int(input("enter amount for education"))
c=int(input("enter amount for Other expense"))
budgets = {"Food": a, "Education": b, "Other Expense": c}
expenses = []

@app.route('/')
def index():
    total_budget = sum(budgets.values())
    total_expense = sum(expenses)
    remaining_budget = total_budget - total_expense
    return render_template('index.html', budgets=budgets, expenses=expenses, remaining_budget=remaining_budget)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    category = request.form['category']
    amount = float(request.form['amount'])
    expenses.append(amount)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
