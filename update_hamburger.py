import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the hamburger icon bigger and change its color to primary so it stands out more
old_hamburger = r'style="display:none; background:none; border:none; color:var\(--text\); cursor:pointer; margin-left:12px;"'
new_hamburger = r'style="display:none; background:rgba(0, 91, 234, 0.1); border:1px solid rgba(0, 91, 234, 0.2); border-radius:8px; padding:6px; color:var(--primary); cursor:pointer; margin-left:12px; transition:all 0.3s;" onmouseover="this.style.background=\'var(--primary)\'; this.style.color=\'white\'" onmouseout="this.style.background=\'rgba(0, 91, 234, 0.1)\'; this.style.color=\'var(--primary)\'"'

# Replace the style string
content = re.sub(old_hamburger, new_hamburger, content)

# Change svg size to be bolder/larger slightly (maybe 32x32)
content = content.replace('width="28" height="28"', 'width="34" height="34"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated hamburger visibility')
