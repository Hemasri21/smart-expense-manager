from database import connect
from rich.table import Table
from rich.console import Console

console = Console()

def monthly_report():
    month = input("Enter month (YYYY-MM): ")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT category, SUM(amount) FROM expenses WHERE date LIKE ? GROUP BY category",
        (f"{month}%",)
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print("[yellow]No expenses found for this month![/yellow]")
        return

    table = Table(title=f"📊 Monthly Report - {month}")
    table.add_column("Category", style="magenta")
    table.add_column("Total Spent (₹)", style="green")

    total = 0
    for row in rows:
        table.add_row(row[0], str(row[1]))
        total += row[1]

    console.print(table)
    console.print(f"\n[bold cyan]💰 Total Spent: ₹{total}[/bold cyan]")

def category_report():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        console.print("[yellow]No data found![/yellow]")
        return

    table = Table(title="📂 Spending by Category")
    table.add_column("Category", style="magenta")
    table.add_column("Total Spent (₹)", style="green")

    for row in rows:
        table.add_row(row[0], str(row[1]))

    console.print(table)