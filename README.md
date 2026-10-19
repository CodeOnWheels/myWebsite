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
