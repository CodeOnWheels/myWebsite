# Giovanni Cascio — Portfolio

A responsive, static portfolio. Deployable output is `dist/`. No runtime dependencies or tracking scripts. Instagram posts load directly from Instagram; visibility depends on Instagram embedding permissions and the visitor’s browser. Original links are always available.

## Write and publish a blog post

1. Open `/write.html` using the footer’s **Write** link.
2. Write a title, date, category, excerpt, and body. The page saves a device-local draft and exports a Markdown file. It does **not** publish directly or sync drafts across devices.
3. Add the exported `.md` file to `content/posts/`, using a unique lowercase hyphenated filename. Set `draft: false` when ready.
4. Run `python scripts/build-blog.py` from this directory, then deploy the updated site through Sites. Alternatively, attach the exported file in the portfolio chat and ask to publish it.

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
- `node --check dist/assets/editor.js`
- Verify local links and anchor targets.

Hosting identity is retained in `.openai/hosting.json`. New Sites are owner-private until their audience is explicitly changed.
