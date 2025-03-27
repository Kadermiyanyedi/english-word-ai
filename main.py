from smolagents import LiteLLMModel
from smolagents.agents import CodeAgent
from tools import OutputWriter
from prompts import ENGLISH_TEACHER_TEMPLATE
from smolagents import DuckDuckGoSearchTool
import typer

MODEL = ""
API_KEY = ""

model = LiteLLMModel(model_id=MODEL, api_key=API_KEY)
agent = CodeAgent(tools=[OutputWriter(), DuckDuckGoSearchTool()], model=model)
app = typer.Typer()


@app.command()
def generate_daily_words():
    agent.run(ENGLISH_TEACHER_TEMPLATE)


@app.command()
def hello(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
