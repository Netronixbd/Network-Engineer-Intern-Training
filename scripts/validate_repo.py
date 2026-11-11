#!/usr/bin/env python3
"""Validate local Markdown links, required training assets and sample resources.

No third-party dependencies; intended for local usage and GitHub Actions.
"""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)')


def check_markdown_links() -> list[str]:
    problems = []
    for markdown in ROOT.rglob('*.md'):
        text = markdown.read_text(encoding='utf-8')
        # Markdown reference links are not used in this training repo.
        for found in LINK.finditer(text):
            raw = (found.group(1) or found.group(2)).strip()
            if raw.startswith(('https://', 'http://', 'mailto:', '#', 'data:')):
                continue
            raw = raw.split(' ', 1)[0]  # Ignore optional title
            path_part = unquote(urlsplit(raw).path)
            if not path_part:
                continue
            resolved = (markdown.parent / path_part).resolve()
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                problems.append(f'{markdown.relative_to(ROOT)} -> {raw}')
    return problems


def main() -> int:
    problems = check_markdown_links()
    labs = list((ROOT/'10-hands-on-labs').glob('lab-*.md'))
    diagrams = list((ROOT/'diagrams').glob('*.dot'))
    qtext = (ROOT/'11-assessment'/'01-viva-120-questions.md').read_text(encoding='utf-8')
    questions = re.findall(r'^### Q\d{3}\.', qtext, flags=re.MULTILINE)
    if len(labs) != 20:
        problems.append(f'Expected 20 labs; found {len(labs)}')
    if len(diagrams) != 15:
        problems.append(f'Expected 15 diagrams; found {len(diagrams)}')
    if len(questions) != 120:
        problems.append(f'Expected 120 viva Q&A; found {len(questions)}')
    expanded = (ROOT/'11-assessment'/'03-detailed-viva-100-qa.md').read_text(encoding='utf-8')
    expanded_questions = re.findall(r'^### Q\d{3}\.', expanded, flags=re.MULTILINE)
    if len(expanded_questions) != 100:
        problems.append(f'Expected 100 detailed Q&A; found {len(expanded_questions)}')
    for diagram in diagrams:
        for ext in ('.svg','.png'):
            if not diagram.with_suffix(ext).exists():
                problems.append(f'Missing preview {diagram.with_suffix(ext)}')
    if problems:
        print('VALIDATION FAILED:')
        for p in problems:
            print(' -', p)
        return 1
    print(f'PASS: {len(list(ROOT.rglob("*.md")))} Markdown files, 20 labs, '
          f'120 foundation Q&A, 100 expanded Q&A, 15 editable diagrams and all relative links valid')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
