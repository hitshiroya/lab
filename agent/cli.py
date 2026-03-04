import sys
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule
from rich.text import Text
from rich import box

from config import Config

console = Console()

BANNER = """
  ███████╗███╗   ███╗ █████╗ ██████╗ ████████╗██╗   ██╗
  ██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝╚██╗ ██╔╝
  ███████╗██╔████╔██║███████║██████╔╝   ██║    ╚████╔╝ 
  ╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║     ╚██╔╝  
  ███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║      ██║   
  ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   
"""

TAGLINE = "your smart assistant at your fingertips"

HELP_TEXT = """
[bold cyan]Commands[/bold cyan]
  [green]exit[/green]  /  [green]quit[/green]  /  [green]q[/green]    →  leave the session
  [green]clear[/green]                          →  clear the screen
  [green]history[/green]                        →  show conversation history
  [green]help[/green]                           →  show this message

[bold cyan]Tips[/bold cyan]
  • just type naturally — ask anything
  • multi-line input: end your line with [yellow]\\[/yellow] and keep going
  • [dim]Part 2 will bring full agentic powers (file ops, Playwright, test generation)[/dim]
"""


def print_banner() -> None:
    console.print(f"[bold magenta]{BANNER}[/bold magenta]")
    console.print(
        Panel(
            Text(TAGLINE, justify="center", style="italic dim white"),
            border_style="magenta",
            box=box.MINIMAL,
        )
    )
    console.print()
    _print_session_info()
    console.print()


def _print_session_info() -> None:
    provider_label = f"[bold green]{Config.PROVIDER.upper()}[/bold green]"
    model_label = f"[bold yellow]{Config.active_model()}[/bold yellow]"
    workspace_label = f"[dim]{Config.WORKSPACE}[/dim]"

    console.print(
        Panel(
            f"  provider  {provider_label}   model  {model_label}\n"
            f"  workspace {workspace_label}",
            border_style="dim",
            box=box.SIMPLE,
            padding=(0, 1),
        )
    )


def print_help() -> None:
    console.print(Panel(HELP_TEXT, title="[bold]help[/bold]", border_style="cyan", box=box.ROUNDED))


def print_error(message: str) -> None:
    console.print(f"\n[bold red]✗[/bold red]  {message}\n")


def print_thinking() -> None:
    console.print("[dim]  thinking...[/dim]", end="\r")


def clear_thinking() -> None:
    console.print(" " * 20, end="\r")


def render_history(history: list[dict]) -> None:
    if not history:
        console.print("[dim]  no history yet[/dim]\n")
        return
    for i, turn in enumerate(history):
        role = turn["role"]
        content = turn["content"]
        if role == "user":
            console.print(f"[bold cyan]  [{i+1}] you[/bold cyan]  {content[:80]}{'...' if len(content) > 80 else ''}")
        else:
            console.print(f"[bold magenta]  [{i+1}] smarty[/bold magenta]  {content[:80]}{'...' if len(content) > 80 else ''}")
    console.print()


def stream_and_render(user_input: str, history: list[dict]) -> str:
    from llm import stream_response

    console.print()
    console.print(Rule(style="dim magenta"))
    console.print()

    full_response = ""
    buffer = ""
    started = False

    try:
        for chunk in stream_response(user_input, history):
            if not started:
                clear_thinking()
                started = True
            full_response += chunk
            buffer += chunk
            console.print(chunk, end="", markup=False, highlight=False)

        console.print()
        console.print()
        console.print(Rule(style="dim magenta"))
        console.print()

    except KeyboardInterrupt:
        console.print("\n\n[dim]  interrupted[/dim]\n")

    return full_response


def get_multiline_input(prompt_str: str) -> str:
    lines = []
    first = True
    while True:
        try:
            if first:
                line = console.input(prompt_str)
                first = False
            else:
                line = console.input("[dim]  ...[/dim] ")
        except (EOFError, KeyboardInterrupt):
            raise KeyboardInterrupt

        if line.endswith("\\"):
            lines.append(line[:-1])
        else:
            lines.append(line)
            break

    return "\n".join(lines)


@click.command()
@click.option("--provider", default=None, help="Override LLM provider: groq or ollama")
@click.option("--model", default=None, help="Override model name")
def run(provider: Optional[str], model: Optional[str]) -> None:
    if provider:
        Config.PROVIDER = provider.lower()
    if model:
        if Config.PROVIDER == "groq":
            Config.GROQ_MODEL = model
        else:
            Config.OLLAMA_MODEL = model

    valid, error = Config.validate()
    if not valid:
        print_error(error)
        sys.exit(1)

    print_banner()

    history: list[dict] = []
    prompt_str = "\n[bold magenta]  ›[/bold magenta] "

    while True:
        try:
            user_input = get_multiline_input(prompt_str).strip()
        except KeyboardInterrupt:
            console.print("\n\n[dim]  use 'exit' to quit[/dim]\n")
            continue

        if not user_input:
            continue

        cmd = user_input.lower()

        if cmd in ("exit", "quit", "q"):
            console.print()
            console.print(Panel(
                "[bold magenta]  later, dev.  keep building.[/bold magenta]",
                border_style="magenta",
                box=box.MINIMAL,
            ))
            console.print()
            break

        if cmd == "clear":
            console.clear()
            print_banner()
            continue

        if cmd == "history":
            render_history(history)
            continue

        if cmd == "help":
            print_help()
            continue

        print_thinking()

        response = stream_and_render(user_input, history)

        if response:
            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    run()
