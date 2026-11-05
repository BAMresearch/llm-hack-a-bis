# Small models.<br>Useful experiments.

LLM Hack a BIS brings research data and local AI together. Bring a problem,
form a team, and build something useful with openBIS.

**Thursday 12 November 2026 · 10:00–17:00 · Berlin time**

[Get ready →](#before-you-arrive){: .button .primary} [See the agenda ↓](#the-agenda){: .button .secondary}
{: .hero-actions}

## The idea

A day to explore what local language models can do for research data.
Start with a small question, try an approach, and share what you learn.
A useful experiment is a great result—even if it is not a finished tool.

## Projects & teams

Project descriptions, ideas, and team coordination live on our **Miro board**.
We will use it throughout the workshop to choose a problem and capture results.

**Miro board link coming soon.**

<!-- Replace the line above with: [Open the Miro board →](https://miro.com/app/board/YOUR_BOARD_ID/) -->

## Before you arrive

Bring your laptop and charger. Please try the setup before Thursday so we can
spend more of the day building together.

### 1. Install Ollama

Go to [ollama.com/download](https://ollama.com/download), choose your operating
system, download the installer, and run it. On Windows, use the Windows download
and follow the installer prompts. José has tested this installation on a BAM
Windows workstation/laptop and it worked.

Open Ollama, then open a new PowerShell or terminal window and check:

```text
ollama --version
```

If the command is not found, close and reopen your terminal after installation.
If installation is blocked or the check fails, bring the error message to the
workshop so we can troubleshoot together.

### 2. Download and try a local model

Download the model before the workshop; this may take a while:

```text
ollama pull qwen3:4b
ollama run qwen3:4b
```

Try a short prompt, such as “Suggest three ways to improve research metadata.”
Type `/bye` to leave the chat. Performance depends on your laptop; if it is too
slow, we can look at a smaller model together.

### 3. Check Python if you plan to code

For Python-based experiments, bring Python 3.11 or newer and an editor you like.
Check your version in a terminal:

```text
python --version
```

On Windows, try `py --version` if `python` is not available. If you need Python,
the [official Python downloads page](https://www.python.org/downloads/) has
installers. Install the packages your team needs once you have chosen a project.

## The agenda

| Time | What we will do |
| --- | --- |
| 10:00–10:30 | Welcome, local LLM introduction, and setup check |
| 10:30–12:00 | Explore the Miro board, form teams, and start experimenting |
| 12:00–13:00 | Pizza break |
| 13:00–17:00 | Build, test, and discuss your short demo |

## Build small. Share what you learn.

Choose one concrete task and a small example to test it. Keep a record of the
prompt, model, and result so you can explain what worked and what still needs work.

For your demo, aim for **4 minutes to present and 2 minutes for questions**.
Show the problem, a short example, and one thing you learned. A failed experiment
with a clear lesson is welcome too.

## Useful links

- [Ollama downloads](https://ollama.com/download)
- [Qwen3 4B model](https://ollama.com/library/qwen3:4b)
- [Structured outputs with Ollama](https://docs.ollama.com/capabilities/structured-outputs)
- [pyBIS documentation](https://openbis.readthedocs.io/en/6.x/software-developer-documentation/apis/python-v3-api.html)
