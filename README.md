# Giovanni Cascio — Portfolio

A responsive, static portfolio. Deployable output is `dist/`. No runtime dependencies or tracking scripts. Instagram posts load directly from Instagram; visibility depends on Instagram embedding permissions and the visitor’s browser. Original links are always available.

## Write and publish a blog post

1. Write an article in your preferred editor and save it as Markdown.
2. Add the `.md` file to `content/posts/`, using a unique lowercase hyphenated filename and the metadata below. Set `draft: false` when ready.
3. Run `python scripts/build-blog.py` from this directory, then deploy through Sites. Alternatively, attach your article in the portfolio chat and ask to publish it.

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

Resume content is sourced from the supplied Giovanni_Cascio_Resume_2026.pdf. The downloadable original is in `dist/assets/`. The robot diagram is illustrative, not a photograph of the competition robot. No travel or photography captions are inferred from the Instagram posts.

## Checks

- `python scripts/build-blog.py`
- Verify local links and anchor targets.

Hosting identity is retained in `.openai/hosting.json`. New Sites are owner-private until their audience is explicitly changed.

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
