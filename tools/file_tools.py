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


class FileReader(Tool):
    name = "file_reader"
    description = "This tool reads the content of a file."

    inputs = {
        "file_path": {
            "type": "string",
            "description": "The path to the file to read.",
        },
    }

    output_type = "string"

    def forward(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        logger.info(f"File {file_path} read successfully")
        return content
