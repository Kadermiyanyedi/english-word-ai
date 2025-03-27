from smolagents import Tool
from structlog import get_logger

logger = get_logger()


class OutputWriter(Tool):
    name = "output_writer"
    description = """
    This tool write output to english_sentences.md file."""

    inputs = {
        "content": {
            "type": "string",
            "description": "The content to write to the file.",
        }
    }

    output_type = "string"

    def forward(self, content: str):
        filename = "english_sentences.md"
        with open(filename, "a+", encoding="utf-8") as file:
            file.write(content)
        logger.info(f"Output written to {filename}")
