import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Add base class for hamburger to hide it on desktop
base_hamburger_css = '''
    .hamburger {
      display: none;
      background: rgba(0, 91, 234, 0.1);
      border: 1px solid rgba(0, 91, 234, 0.2);
      border-radius: 8px;
      padding: 6px;
      color: var(--primary);
      cursor: pointer;
      margin-left: 12px;
      transition: all 0.3s;
    }
    .hamburger:hover {
      background: var(--primary);
      color: white;
    }
    .hamburger svg {
      display: block;
    }
'''
content = re.sub(r'(\.btn-nav:hover\s*\{[^}]*\})', r'\1' + '\n' + base_hamburger_css, content)

# 3. Clean up the inline styles from the HTML to rely on the CSS classes instead
# This finds the hamburger button and replaces it entirely with a clean version
clean_button = '<button class="hamburger" id="hamburger" aria-label="Menu">\n        <svg viewBox="0 0 24 24" width="34" height="34" fill="currentColor">'
content = re.sub(r'<button class="hamburger" id="hamburger".*?<svg viewBox="0 0 24 24" width="34" height="34" fill="currentColor">', clean_button, content, flags=re.DOTALL)

# 4. Update the media query class for .hamburger
content = content.replace('.hamburger {\n        display: block !important;\n      }', '.hamburger {\n        display: flex !important;\n        align-items: center;\n        justify-content: center;\n      }')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done fixing hamburger CSS')
