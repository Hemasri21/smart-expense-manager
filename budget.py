from database import connect
from rich.console import Console
from rich.table import Table

console = Console()

def set_budget(category, limit_amount):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO budgets (category, limit_amount) VALUES (?, ?) ON CONFLICT(category) DO UPDATE SET limit_amount=?",
        (category, limit_amount, limit_amount)
    )
    conn.commit()
    conn.close()
    console.print(f"[green]✅ Budget of ₹{limit_amount} set for '{category}'![/green]")

def check_budget():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT category, limit_amount FROM budgets")
    budgets = cursor.fetchall()

    if not budgets:
        console.print("[yellow]No budgets set yet![/yellow]")
        conn.close()
        return

    table = Table(title="🎯 Budget vs Spending")
    table.add_column("Category", style="magenta")
    table.add_column("Budget (₹)", style="blue")
    table.add_column("Spent (₹)", style="green")
    table.add_column("Status", style="white")

    for b in budgets:
        category, limit = b
        cursor.execute(
            "SELECT SUM(amount) FROM expenses WHERE category = ?", (category,)
        )
        result = cursor.fetchone()[0] or 0
        status = "[red]⚠️ OVER BUDGET[/red]" if result > limit else "[green]✅ Within Budget[/green]"
        table.add_row(category, str(limit), str(result), status)

    conn.close()
    console.print(table)