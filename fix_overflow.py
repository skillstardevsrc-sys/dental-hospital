import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure html and body explicitly hide horizontal overflow
html_body_fix = r'''
html, body {
  overflow-x: hidden;
  width: 100%;
  max-width: 100%;
  position: relative;
}
'''

# Update html css
content = re.sub(r'(html\s*\{[^}]+\})', html_body_fix + r'\n\1', content)

# Check if there is anything that is translating X which might cause overflow
# Actually html,body overflow-x hidden fixes the gap in 99% of cases.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done fixing overflow.')
