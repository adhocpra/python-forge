import pandas as pd
import matplotlib.pyplot as plt
import qrcode
import os

CSV_FILE = "expenses.csv"

# ---------- Expense Class ----------
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = float(amount)
        self.category = category

    def to_dict(self):
        return {"name": self.name, "amount": self.amount, "category": self.category}


# ---------- Load / Save ----------
def load_expenses():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["name", "amount", "category"])


def save_expense(expense):
    df = load_expenses()
    new_row = pd.DataFrame([expense.to_dict()])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    print(f"  Saved: {expense.name} - Rs.{expense.amount} [{expense.category}]")


# ---------- Add Expenses ----------
def add_expenses():
    print("\n--- Add Expenses (type 'done' to stop) ---")
    while True:
        name = input("Expense name: ").strip()
        if name.lower() == "done":
            break
        try:
            amount = float(input("Amount (Rs.): "))
        except ValueError:
            print("  Invalid amount. Try again.")
            continue
        category = input("Category (Food/Travel/Shopping/Other): ").strip().capitalize()
        expense = Expense(name, amount, category)
        save_expense(expense)


# ---------- Show Summary ----------
def show_summary():
    df = load_expenses()
    if df.empty:
        print("No expenses found.")
        return

    print("\n--- Expense Summary ---")
    summary = df.groupby("category")["amount"].sum()
    for cat, total in summary.items():
        print(f"  {cat}: Rs.{total:.2f}")
    print(f"  TOTAL: Rs.{df['amount'].sum():.2f}")


# ---------- Bar Chart ----------
def plot_chart():
    df = load_expenses()
    if df.empty:
        print("No data to plot.")
        return

    summary = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(7, 4))
    plt.bar(summary.index, summary.values, color=["#4CAF50", "#2196F3", "#FF9800", "#E91E63"])
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (Rs.)")
    plt.tight_layout()
    plt.savefig("expense_chart.png")
    plt.show()
    print("  Chart saved as expense_chart.png")


# ---------- QR Code ----------
def generate_qr():
    df = load_expenses()
    if df.empty:
        print("No expenses to encode.")
        return

    total = df["amount"].sum()
    summary = df.groupby("category")["amount"].sum()
    lines = [f"{cat}: Rs.{amt:.2f}" for cat, amt in summary.items()]
    lines.append(f"Total: Rs.{total:.2f}")
    text = "Expense Summary\n" + "\n".join(lines)

    img = qrcode.make(text)
    img.save("expense_summary_qr.png")
    print("  QR code saved as expense_summary_qr.png")


# ---------- Main Menu ----------
def main():
    print("====== Expense Tracker ======")
    while True:
        print("\n1. Add expenses")
        print("2. Show summary")
        print("3. Plot chart")
        print("4. Generate QR code")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            add_expenses()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            plot_chart()
        elif choice == "4":
            generate_qr()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()