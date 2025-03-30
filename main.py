from smolagents import LiteLLMModel
from smolagents.agents import CodeAgent
from tools import OutputWriter, FileReader
from prompts import ENGLISH_TEACHER_TEMPLATE
from smolagents import DuckDuckGoSearchTool
import typer
from typing_extensions import Annotated
from enums import EnglishLevel
from config import load_env
import os


MODEL = os.environ.get("ENGLISH_AI_MODEL", "gemini/gemini-2.0-flash-exp")
API_KEY = os.environ.get("ENGLISH_AI_API_KEY", "your_api_key_here")

model = LiteLLMModel(model_id=MODEL, api_key=API_KEY)
agent = CodeAgent(
    tools=[OutputWriter(), FileReader(), DuckDuckGoSearchTool()],
    model=model,
)
app = typer.Typer()


@app.command()
def generate_daily_words(
    output_file: Annotated[
        str,
        typer.Option("--output", "-o", help="Output file name"),
    ] = "english_sentences.md",
    level: Annotated[
        EnglishLevel,
        typer.Option(
            "--level",
            "-l",
            help="English level (A1, A2, B1, B2, C1, C2)",
            case_sensitive=False,
        ),
    ] = EnglishLevel.A1,
):
    """Generate daily words for a given English level.

    Args:
        output_file (str): The name of the output file. Default is "english_sentences.md".
        level (EnglishLevel): The English level for which to generate words. Default is A1.
    """
    prompt = ENGLISH_TEACHER_TEMPLATE.format(
        user_level=level.name,
        output_file=output_file,
    )
    typer.echo(f"Generating daily words for {level.name} level...")
    agent.run(prompt)


@app.command()
def set_env(
    config_file: Annotated[str, typer.Option(help="Path to config file")] = ".env",
):
    """Set environment variables from a config file.

    Args:
        config_file (str): The path to the config file. Default is ".env".
    """
    load_env(config_file)
    typer.echo("Environment variables set from config file.")


if __name__ == "__main__":
    app()
