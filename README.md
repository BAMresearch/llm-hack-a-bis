# LLM Hack a BIS

Static event page for Thursday **12 November 2026, 10:00–17:00 (Europe/Berlin)**.
Content is Markdown, converted to HTML with one small Python dependency.
No Node.js, Ruby, database, browser JavaScript, or external fonts are needed.

## Preview and edit locally

From this repository, using Python 3.11 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python build.py --serve
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python build.py --serve
```

Open **http://localhost:8000**. Edit a file, save, and refresh the browser to see
your changes. The preview rebuilds on each page request; there is no automatic
browser reload. Stop with **Ctrl+C**. To use a different port:
`python build.py --serve --port 8080`.

## What to edit

| File | Purpose |
| --- | --- |
| `content/index.md` | All participant content: introduction, preparation, agenda, Miro link, demo guidance |
| `assets/style.css` | Colors, typography, spacing, and mobile layout |
| `templates/index.html` | Page shell, navigation, browser title, description, and footer |
| `build.py` | Markdown conversion and local preview server |
| `.github/workflows/pages.yml` | Build and GitHub Pages deployment |

**Before publishing:** replace the pending venue and Miro link in
`content/index.md`. The working-session times are suggested; adjust them as
needed. Python and Ollama installation instructions on the page are for
participants; only Python is needed to develop this website.

Use `## Heading` for sections, `### Heading` for subheadings, normal Markdown
links and lists, fenced code blocks, and Markdown tables. Heading IDs are
generated automatically (for example, `## Before you arrive` becomes
`#before-you-arrive`). Update navigation links in the template if you rename
their headings. Ordinary paragraphs do not need HTML; the introductory title
uses `<br>` for its line break.

The two introductory links use Markdown attribute lists (`{: .button .primary}`
and `{: .button .secondary}`) for their button styles. Keep those attributes when
editing their labels. The build script wraps the introduction in the hero panel
and each `##` section in a responsive layout. At laptop widths, headings sit
beside their content; on phones they stack. The maximum page width is 1240px.

## Build a static copy

```bash
python build.py
```

This generates `dist/index.html`, `dist/assets/`, and `.nojekyll`. The generated
`dist/` directory is ignored by Git; edit the source files above. It can be
served by any static web server. Asset links are relative, so the site also
works under a GitHub Pages repository path such as `/llm-hack-a-bis/`.

## Publish with GitHub Pages

1. In the GitHub repository, open **Settings → Pages**.
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. Commit and push the source files to `main`. If the default branch has a
   different name, change `branches: [main]` in `.github/workflows/pages.yml`.
4. The **Deploy event page** workflow builds and publishes `dist/`. Find the
   site URL in the workflow deployment or **Settings → Pages**.

Subsequent pushes to `main` publish automatically. You can also run the workflow
manually from the Actions tab. No publishing has been performed from this
checkout; you control when to commit and push.

### GitHub setup checklist (for the maintainer)

These instructions stay in this README; they are not included in the event page.

- Keep `.github/workflows/pages.yml` in the repository. It defines the Python
  build, uploads `dist/`, and deploys it with GitHub Pages. No custom secrets or
  access tokens are needed.
- Under **Settings → Actions → General**, ensure GitHub Actions and the actions
  used by this workflow are allowed by the repository/organization policy.
- Under **Settings → Pages**, choose **GitHub Actions**, rather than deployment
  from a branch. You do not need a `gh-pages` branch or generated HTML in Git.
- Push your changes to `main`, then open **Actions → Deploy event page** to
  follow the build and deployment. A successful deployment displays the URL.
- A project repository normally appears at
  `https://YOUR-OWNER.github.io/llm-hack-a-bis/`. Use the actual URL reported by
  GitHub; a custom domain or organization setup may change it.
- If deployment needs approval, check the **github-pages** environment under
  **Settings → Environments** for reviewer or branch restrictions.
- If a deployment fails, open the failed step in Actions. Check that Pages is
  enabled, its source is GitHub Actions, and the workflow branch matches your
  default branch. Repository availability for Pages depends on visibility and
  your GitHub plan.

The deployment follows the official
[GitHub Pages custom workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
