#!/usr/bin/env python3
"""Build safe static articles from content/posts/*.md; no dependencies required."""
from pathlib import Path
from html import escape
from datetime import date
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'

def render(body):
    output, paragraph, items, code = [], [], [], None
    def flush():
        if paragraph:
            output.append('<p>' + '<br>'.join(escape(x) for x in paragraph) + '</p>')
            paragraph.clear()
        if items:
            output.append('<ul>' + ''.join('<li>' + escape(x) + '</li>' for x in items) + '</ul>')
            items.clear()
    for line in body.splitlines():
        if line.startswith('```'):
            flush()
            if code is None: code = []
            else:
                output.append('<pre><code>' + escape('\n'.join(code)) + '</code></pre>')
                code = None
        elif code is not None: code.append(line)
        elif not line.strip(): flush()
        elif line.startswith('## '):
            flush(); output.append('<h2>' + escape(line[3:]) + '</h2>')
        elif line.startswith('- '):
            if paragraph: flush()
            items.append(line[2:])
        else:
            if items: flush()
            paragraph.append(line)
    flush()
    if code is not None: raise ValueError('Unclosed code fence')
    return '\n'.join(output)

def build():
    posts = []
    for source in (ROOT / 'content/posts').glob('*.md'):
        text = source.read_text()
        if not text.startswith('---\n'): raise ValueError(f'{source}: missing metadata')
        _, raw, body = text.split('---', 2)
        meta = dict(line.split(':', 1) for line in raw.strip().splitlines() if ':' in line)
        meta = {k.strip(): v.strip() for k,v in meta.items()}
        if meta.get('draft', 'true').lower() != 'false': continue
        title = meta['title']
        published = date.fromisoformat(meta['date'])
        slug = source.stem
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug): raise ValueError('Use a lowercase hyphenated filename')
        article = render(body.strip())
        posts.append((published, slug, title, meta.get('excerpt',''), meta.get('category','Notes'), article))
    posts.sort(reverse=True)
    outdir = DIST / 'journal'
    outdir.mkdir(exist_ok=True)
    for existing in outdir.glob('*.html'): existing.unlink()
    rows=[]
    for published,slug,title,excerpt,category,body in posts:
        safe_title, safe_category = escape(title), escape(category)
        label = published.strftime('%b %d, %Y').upper()
        page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{safe_title} — Giovanni Cascio</title><meta name="description" content="{escape(excerpt, quote=True)}"><link rel="stylesheet" href="/assets/style.css"></head><body><header class="nav"><a class="wordmark" href="/">GC<span class="dot">✳</span></a><a href="/#journal">← All field notes</a></header><main class="article"><span class="eyebrow">{safe_category} / <time datetime="{published.isoformat()}">{label}</time></span><h1>{safe_title}</h1><div>{body}</div><p><a href="/#journal">← Back to the journal</a></p></main></body></html>'''
        (outdir / f'{slug}.html').write_text(page)
        rows.append(f'<a class="post-row" href="/journal/{slug}.html"><span class="eyebrow">{label}<br>{safe_category}</span><div><h3>{safe_title}</h3><p>{escape(excerpt)}</p></div><span class="arrow" aria-hidden="true">↗</span></a>')
    index = DIST / 'index.html'
    text = index.read_text()
    if rows:
        replacement='\n'.join(rows)
    else:
        replacement='<div class="empty-journal"><span class="journal-symbol" aria-hidden="true">↳</span><div><h3>The notebook is open.</h3><p>No posts published yet. Future notes on code, robotics, photography, and life beyond the classroom will live here.</p></div><span class="eyebrow">MORE TO COME</span></div>'
    text = re.sub(r'<!-- BLOG_START -->.*?<!-- BLOG_END -->', '<!-- BLOG_START -->'+replacement+'<!-- BLOG_END -->', text, flags=re.S)
    index.write_text(text)
    print(f'Built {len(posts)} published article(s).')

if __name__ == '__main__': build()
