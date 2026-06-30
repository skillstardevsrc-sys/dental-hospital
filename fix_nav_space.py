import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Hide .btn-nav on small screens so the hamburger menu fits in the navbar
# We'll insert this rule into the max-width: 768px media query we added earlier
fix_nav_btn_css = '''
      #navbar .btn-nav {
        display: none !important;
      }
'''

content = content.replace('.faq-grid::-webkit-scrollbar {\n        display: none;\n      }', '.faq-grid::-webkit-scrollbar {\n        display: none;\n      }\n' + fix_nav_btn_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done fixing navbar space')
