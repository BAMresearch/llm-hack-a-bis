## Local-LLM tutorial

### From a lab note to a validated draft

Use a small local model to extract metadata, then check both its structure and
its facts. 

### 1. Set up the exercise

Finish the Ollama setup [above](#before-you-arrive), keep Ollama running, and
create a separate folder for this exercise. Download
[starter.py](assets/tutorial/starter.py) and
[the tutorial requirements](assets/tutorial/requirements.txt) into that folder.

Install the requirements in a virtual or conda environment, and run the starter script with `python /path/to/starter.py`.

The script calls Ollama at `http://127.0.0.1:11434`, uses synthetic notes, and
writes `results.json` in your working folder. It does not connect to openBIS.

The initial model download with `ollama pull` needs internet; this script's inference runs locally. On some
CPUs, running all ten cases can take several minutes.

### 2. Understand the core pattern

The schema describes the fields we want. Ollama returns structured JSON, and
Pydantic validates that it matches the schema. Save this shorter example as
`example.py` if you want to try it on its own, and run it with the same Python
environment as the starter.

```python
from ollama import Client
from pydantic import BaseModel

class Draft(BaseModel):
    sample_name: str | None
    material: str | None

client = Client(host="http://127.0.0.1:11434")
response = client.chat(
    model="qwen3:4b",
    messages=[{"role": "user", "content":
        "Extract facts; use null if missing. "
        "Sample S-001 is NiO."}],
    format=Draft.model_json_schema(),
    think=False,
    options={"temperature": 0},
)
draft = Draft.model_validate_json(
    response.message.content
)
print(draft.model_dump())
```

This should extract `S-001` and `NiO`. Schema validation checks the shape and
types; it does not guarantee that the extracted facts are correct. 

### 3. Evaluate and experiment

The full starter extracts five fields: sample name, material, method,
temperature, and operator. Its ten cases include missing metadata, an unlisted
method, and an instruction embedded in a lab note.

- Inspect `results.json` and compare the expected and actual values.
- Report schema-valid cases out of 10, exact records out of 10, correct fields
  out of 50, and mean runtime. The first request may include model loading.
- Change one prompt or schema choice, rerun, and compare the same cases.
- Try a simple rule-based baseline for sample identifiers or methods.

You can chose a different model to run `starter.py` by doing (in our example, `qwen3:4b`):
```bash
ollama pull qwen3:4b
MODEL=qwen3:4b python starter.py
```

In PowerShell, set the variable before running:

```powershell
ollama pull qwen3:4b
$env:MODEL = "qwen3:4b"
python starter.py
```
