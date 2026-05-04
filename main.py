from database import create_tables
from expenses import add_expense, view_expenses, delete_expense
from reports import monthly_report, category_report
from budget import set_budget, check_budget
from rich.console import Console

console = Console()

def main():
    create_tables()

    while True:
        console.print("\n[bold cyan]===== 💰 Smart Expense Manager =====[/bold cyan]")
        console.print("[white]1. Add Expense[/white]")
        console.print("[white]2. View All Expenses[/white]")
        console.print("[white]3. Delete Expense[/white]")
        console.print("[white]4. Monthly Report[/white]")
        console.print("[white]5. Category-wise Report[/white]")
        console.print("[white]6. Set Budget[/white]")
        console.print("[white]7. Check Budget Status[/white]")
        console.print("[white]8. Exit[/white]")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            category = input("Category (food/travel/medicine/shopping/other): ")
            amount = float(input("Amount (₹): "))
            description = input("Description: ")
            add_expense(category, amount, description)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_expenses()
            eid = int(input("Enter ID to delete: "))
            delete_expense(eid)

        elif choice == "4":
            monthly_report()

        elif choice == "5":
            category_report()

        elif choice == "6":
            category = input("Category: ")
            limit = float(input("Budget Limit (₹): "))
            set_budget(category, limit)

        elif choice == "7":
            check_budget()

        elif choice == "8":
            console.print("[bold green]👋 Goodbye! Stay Smart with Money![/bold green]")
            break

        else:
            console.print("[red]❌ Invalid choice. Try again![/red]")

if __name__ == "__main__":
    main()