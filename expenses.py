from database import connect
from datetime import date
from rich.table import Table
from rich.console import Console

console = Console()

def add_expense(category, amount, description):
    conn = connect()
    cursor = conn.cursor()
    today = str(date.today())
    cursor.execute(
        "INSERT INTO expenses (category, amount, description, date) VALUES (?, ?, ?, ?)",
        (category, amount, description, today)
    )
    conn.commit()
    conn.close()
    console.print(f"\n[green]✅ Expense of ₹{amount} added under '{category}'![/green]")

def view_expenses():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print("[yellow]No expenses found![/yellow]")
        return

    table = Table(title="💸 All Expenses")
    table.add_column("ID", style="cyan")
    table.add_column("Category", style="magenta")
    table.add_column("Amount (₹)", style="green")
    table.add_column("Description", style="white")
    table.add_column("Date", style="blue")

    for row in rows:
        table.add_row(str(row[0]), row[1], str(row[2]), row[3], row[4])

    console.print(table)

def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    console.print(f"[red]🗑️ Expense ID {expense_id} deleted.[/red]")