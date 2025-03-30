# english-word-ai

This project is designed to assist English learners by providing high-frequency vocabulary words, definitions, and example sentences in various grammatical constructions. The agent generates structured learning materials in Markdown format and saves them to a file named english_sentences.md.

### Features

* Selects five high-frequency English words suitable for learners.

* Uses Cambridge or Oxford dictionary sources to determine the words.

* Provides concise English definitions for each word.

* Outputs results in a clear, organized Markdown format.

### Installation & Requirements

To use this project, ensure you have the following installed:

You can install the necessary dependencies using:

```
pip install uv
uv sync
```

### Usage

Run the script to generate vocabulary and example sentences:

`python main.py generate-daily-words -o english_sentences.md -l B1`

The output will be saved in **english_sentences.md**.

#### Output Format

The generated Markdown file will follow this structure:

Word: consider

**Definition:** To spend time thinking about a possibility or making a decision.

| Tense                       | Example Sentence                                         |
|-----------------------------|----------------------------------------------------------|
| Present Simple              | I consider all options carefully. |
| Present Continuous              | She is considering a new job offer. |
| Present Perfect              | They have considered moving to another city. |

### TODO:
[X] Allow the user to specify the output file name.

[X] Allow the user to choose the language level for word selection.

[] Update the prompt to ensure words are not repeated.

[] Enable users to provide a text file with words to be used in examples.

[] Add devolepment packages such as Ruff.

[X] Add set_env command for model information