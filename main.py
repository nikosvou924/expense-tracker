from __future__ import annotations
from typing import List, Dict, Any


def print_menu() -> None:
    print("\n=== Expense Tracker ===")
    print("1) Add expense")
    print("2) Show summary")
    print("3) Show totals by category")
    print("4) List all expenses")
    print("5) Exit")


def read_non_empty_text(prompt: str) -> str:
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Wrong input: please type something (not empty).")


def read_non_negative_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Wrong input: please enter a number (e.g., 3.5).")
            continue

        if value < 0:
            print("Wrong input: amount must be non-negative.")
            continue

        return value


def add_expense(expenses: List[Dict[str, Any]]) -> None:
    amount = read_non_negative_float("Amount (€): ")
    category = read_non_empty_text("Category (e.g., food, coffee): ").lower()
    note = input("Note (optional): ").strip()

    expense = {"amount": amount, "category": category, "note": note}
    expenses.append(expense)

    print(f"Saved: €{amount:.2f} in '{category}'" + (f" ({note})" if note else ""))


def show_summary(expenses: List[Dict[str, Any]]) -> None:
    if not expenses:
        print("No expenses yet.")
        return

    amounts = [e["amount"] for e in expenses]
    total = sum(amounts)
    count = len(amounts)
    average = total / count
    min_expense = min(amounts)
    max_expense = max(amounts)

    print("\n--- Summary ---")
    print(f"Count:   {count}")
    print(f"Total:   €{total:.2f}")
    print(f"Average: €{average:.2f}")
    print(f"Min:     €{min_expense:.2f}")
    print(f"Max:     €{max_expense:.2f}")


def show_by_category(expenses: List[Dict[str, Any]]) -> None:
    if not expenses:
        print("No expenses yet.")
        return

    totals: Dict[str, float] = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0.0) + e["amount"]

    print("\n--- Totals by category ---")
    for cat in sorted(totals):
        print(f"{cat:>12}: €{totals[cat]:.2f}")


def list_expenses(expenses: List[Dict[str, Any]]) -> None:
    if not expenses:
        print("No expenses yet.")
        return

    print("\n--- All expenses ---")
    for i, e in enumerate(expenses, start=1):
        amount = e["amount"]
        category = e["category"]
        note = e["note"]
        if note:
            print(f"{i:>3}) €{amount:>7.2f}  [{category}]  - {note}")
        else:
            print(f"{i:>3}) €{amount:>7.2f}  [{category}]")


def main() -> None:
    expenses: List[Dict[str, Any]] = []

    while True:
        print_menu()
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            show_by_category(expenses)
        elif choice == "4":
            list_expenses(expenses)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Wrong input: choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
