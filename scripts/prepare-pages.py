#!/usr/bin/env python3
"""Copy static output and rebase root-relative HTML links for GitHub Pages."""
import argparse
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]


def prepare(base_path):
    base = '/' + base_path.strip('/') if base_path.strip('/') else ''
    if not re.fullmatch(r'(?:/[A-Za-z0-9._~-]+)*', base):
        raise ValueError('Base path must contain URL-safe path segments')
    output = ROOT / '_site'
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(ROOT / 'dist', output)
    # Keep external, fragment-only, and protocol-relative URLs unchanged.
    pattern = re.compile(r'(?P<attr>\b(?:href|src|action)\s*=\s*)(?P<quote>[\x22\x27])/(?P<path>(?!/)[^\x22\x27]*)(?P=quote)')
    for page in output.rglob('*.html'):
        content = page.read_text()
        content = pattern.sub(lambda m: m['attr'] + m['quote'] + base + '/' + m['path'] + m['quote'], content)
        page.write_text(content)
    (output / '.nojekyll').touch()
    print(f'Prepared GitHub Pages output at {output} with base path {base or "/"}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-path', default='/myWebsite')
    prepare(parser.parse_args().base_path)
