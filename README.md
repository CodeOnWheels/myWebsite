# Giovanni Cascio — Portfolio

A responsive, static portfolio. Deployable output is `dist/`. No runtime dependencies or tracking scripts. Instagram posts load directly from Instagram; visibility depends on Instagram embedding permissions and the visitor’s browser. Original links are always available.

## Overview

A personal portfolio built with HTML, CSS, JavaScript, and Python. Features include English/Traditional Chinese language switching, a downloadable resume, and a static journal generated from Markdown.

## Run locally

Requires Python 3; no third-party packages are needed.

```sh
git clone https://github.com/CodeOnWheels/myWebsite.git
cd myWebsite
python scripts/build-blog.py
python -m http.server 8000 --directory dist
```

Open http://localhost:8000.

## Project structure

- `dist/index.html` — portfolio content and entry page.
- `dist/assets/` — styling, language switching, translations, and resume.
- `content/posts/` — optional journal source; create it when adding a post.
- `scripts/build-blog.py` — Markdown-to-HTML journal generator.
- `scripts/prepare-pages.py` — separate build output for a GitHub Pages project path.
- `.github/workflows/pages.yml` — deployment workflow.

## Write and publish a blog post

1. Write an article in your preferred editor and save it as Markdown.
2. Add the `.md` file to `content/posts/`, using a unique lowercase hyphenated filename and the metadata below. Set `draft: false` when ready.
3. Run `python scripts/build-blog.py` from this directory. Preview the result locally, then deploy the site.

There is no on-site writing or publishing interface. Visitors can only read published articles.

Supported body formatting: paragraphs, `## headings`, `- lists`, and fenced code blocks. Raw HTML is escaped. This intentionally small format keeps posts safe and dependency-free.

Example metadata:

```text
---
title: My first field note
date: 2026-10-18
category: Notes
excerpt: A short description of the post.
draft: true
---

Write your article here.
```

The journal stays empty until a real post is published. Generated article pages live in `dist/journal/`; do not edit generated files directly.

## Content

The resume is in `dist/assets/Giovanni_Cascio_Resume_2026.pdf`. The robotics section uses an illustrative system diagram.

## Checks

- `python scripts/build-blog.py`
- Verify local links and anchor targets.

## GitHub Pages

The workflow in `.github/workflows/pages.yml` builds the blog and publishes a
Pages-specific copy of `dist/` on every push to `main`. The original `dist/`
keeps its root-relative paths for Sites hosting. `scripts/prepare-pages.py`
rebases links in the copied `_site/` output using the Pages base path, including
stylesheets, JavaScript, the resume download, and nested journal links.

One-time setup: open repository **Settings → Pages → Build and deployment**,
and set **Source** to **GitHub Actions**. Then open **Actions → Deploy portfolio
to GitHub Pages → Run workflow** if the latest push has already run.

Expected URL: https://codeonwheels.github.io/myWebsite/

Local build check:

```sh
python scripts/build-blog.py
python scripts/prepare-pages.py --base-path /myWebsite
```

Push source changes to `main` to update GitHub Pages automatically. The
published PDF is the original English resume, and Instagram embeds remain
hosted by Instagram.

## Troubleshooting Pages deployment

The repository uses a custom Actions workflow to publish `_site/`. In Settings → Pages, choose **GitHub Actions** as the build source. A branch-based Jekyll build targeting `/docs` will fail because this repository does not contain that directory.

If Configure Pages reports “Not Found,” check that Pages is enabled for this repository and configured for GitHub Actions. Then rerun the existing deployment workflow. Successful local generation alone does not confirm successful publishing.

