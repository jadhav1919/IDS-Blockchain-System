# dashboard.py
import time, random
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from datetime import datetime

console = Console()

alert_file = "alerts.log"

# Some fake background network messages to make it cinematic
background_msgs = [
    "Scanning incoming packets...",
    "Analyzing TCP stream...",
    "Decrypting payload headers...",
    "Running anomaly detection model...",
    "Signature match found in stream...",
    "Hash validation against blockchain...",
    "Alert sent to security node..."
]

def load_alerts():
    alerts = []
    try:
        with open(alert_file, "r") as f:
            for line in f:
                if "ALERT:" in line:
                    parts = line.strip().split(" - ")
                    timestamp = parts[0] if len(parts) > 1 else datetime.now().strftime("%H:%M:%S")
                    msg = parts[-1].replace("ALERT:", "").strip()
                    alerts.append((timestamp, msg))
    except FileNotFoundError:
        pass
    # show last 100 alerts instead of 10
    return alerts[-100:]

def make_table(alerts):
    table = Table(title="[bold red]🚨 ACTIVE ALERT FEED 🚨[/bold red]", border_style="bright_red")
    table.add_column("Time", style="cyan", no_wrap=True)
    table.add_column("Detected Attack", style="bold yellow")

    if not alerts:
        table.add_row("—", "No alerts yet. System monitoring traffic...")
    else:
        for ts, msg in alerts:
            table.add_row(ts, f"[red]{msg}[/red]")

    return table

def make_status():
    msg = random.choice(background_msgs)
    dots = "." * random.randint(1, 3)
    return f"[green]{msg}{dots}[/green]"

console.clear()
console.print(Panel.fit("[bold green]🛡️ CYBER DEFENSE TERMINAL ONLINE 🛡️[/bold green]"))

with Live(console=console, refresh_per_second=2) as live:
    while True:
        alerts = load_alerts()
        table_panel = make_table(alerts)
        status_panel = Panel(make_status(), title="System Status", border_style="bright_green")

        layout = Group(table_panel, status_panel)

        full_display = Panel(
            layout,
            title=f"[white]Updated: {datetime.now().strftime('%H:%M:%S')}[/white]",
            border_style="bright_cyan"
        )

        live.update(full_display)
        time.sleep(2)

