from smolagents import LiteLLMModel
from smolagents.agents import CodeAgent
from tools import OutputWriter
from prompts import ENGLISH_TEACHER_TEMPLATE
from smolagents import DuckDuckGoSearchTool
import typer
from typing_extensions import Annotated
from enums import EnglishLevel


MODEL = ""
API_KEY = ""

model = LiteLLMModel(model_id=MODEL, api_key=API_KEY)
agent = CodeAgent(tools=[OutputWriter(), DuckDuckGoSearchTool()], model=model)
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
    prompt = ENGLISH_TEACHER_TEMPLATE.format(
        user_level=level.name,
        output_file=output_file,
    )
    typer.echo(f"Generating daily words for {level.name} level...")
    agent.run(prompt)


@app.command()
def hello(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
