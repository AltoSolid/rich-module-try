# Record the time when a particular task is finished executing.
from rich.console import Console
from time import sleep

cs = Console()

tasks = ["gathering IPs", "gathering emails", "gathering domains", "gathering Subdomains", "gathering Phone numbers"]

with cs.status("[bold green]Scraping data...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(2)
        cs.log(f"[green]Finishing [/green]{task}")
    cs.log(f"[bold][red]Done!")