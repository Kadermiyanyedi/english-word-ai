from smolagents import Tool
from structlog import get_logger

logger = get_logger()


class OutputWriter(Tool):
    name = "output_writer"
    description = "This tool write output to output file."

    inputs = {
        "content": {
            "type": "string",
            "description": "The content to write to the file.",
        },
        "output_file": {
            "type": "string",
            "description": "The name of the output file. It should be decided in user query.",
        },
    }

    output_type = "string"

    def forward(self, content: str, output_file: str):
        with open(output_file, "a+", encoding="utf-8") as file:
            file.write(content)
        logger.info(f"Output written to {output_file}")
