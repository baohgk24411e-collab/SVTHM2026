# -*- coding: utf-8 -*-
import os
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r'd:\SVTHM2026'
html_files = glob.glob(os.path.join(ROOT_DIR, '*.html'))

print(f"Checking {len(html_files)} HTML files in {ROOT_DIR}...")
missing_count = 0

for h in html_files:
    fname = os.path.basename(h)
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check script references
    scripts = re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', content)
    for s in scripts:
        if not s.startswith('http'):
            clean_s = s.replace('/', os.sep)
            full_path = os.path.join(ROOT_DIR, clean_s)
            if not os.path.exists(full_path):
                print(f"[{fname}] Missing script: {s}")
                missing_count += 1
                
    # Check CSS references
    css_links = re.findall(r'<link[^>]*href=[\'"]([^\'"]+\.css)[\'"]', content)
    for c in css_links:
        if not c.startswith('http'):
            clean_c = c.replace('/', os.sep)
            full_path = os.path.join(ROOT_DIR, clean_c)
            if not os.path.exists(full_path):
                print(f"[{fname}] Missing CSS: {c}")
                missing_count += 1

if missing_count == 0:
    print("ALL HTML script and CSS references are 100% valid!")
else:
    print(f"Found {missing_count} missing references.")

