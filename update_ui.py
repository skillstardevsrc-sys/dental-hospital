import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML: Add hamburger button to nav
nav_right_pattern = r'(<div class=\"nav-right\">.*?)(</div>\s*</nav>)'
hamburger_html = '''
      <button class=\"hamburger\" id=\"hamburger\" aria-label=\"Menu\" style=\"display:none; background:none; border:none; color:var(--text); cursor:pointer; margin-left:12px;\">
        <svg viewBox=\"0 0 24 24\" width=\"28\" height=\"28\" fill=\"currentColor\">
          <path d=\"M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z\"/>
        </svg>
      </button>
    '''
content = re.sub(nav_right_pattern, r'\g<1>' + hamburger_html + r'\g<2>', content, flags=re.DOTALL)

# 2. Update CSS: Make nav-links a dropdown on mobile
nav_css_pattern = r'(\.nav-links \{\s*display: none\s*\})'
nav_css_replacement = '''
      .nav-links {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: var(--bg);
        flex-direction: column;
        padding: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        gap: 16px;
      }
      .nav-links.active {
        display: flex !important;
      }
      .hamburger {
        display: block !important;
      }
'''
content = re.sub(nav_css_pattern, nav_css_replacement, content)

# 3. Add JS for hamburger menu
js_pattern = r'(// Smile Analyzer Logic)'
js_replacement = '''
    // Hamburger Menu Logic
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.querySelector('.nav-links');
    if(hamburger) {
      hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
      });
      // Close nav when clicking a link
      navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          navLinks.classList.remove('active');
        });
      });
    }
    
    \g<1>'''
content = re.sub(js_pattern, js_replacement, content)

# 4. Grids to horizontal scroll in mobile view
grid_css = '''
    @media (max-width: 768px) {
      .why-grid, .bento-grid, .doctor-stats, .counter-grid, .faq-grid {
        display: flex !important;
        flex-direction: row !important;
        overflow-x: auto !important;
        scroll-snap-type: x mandatory !important;
        padding-bottom: 20px !important;
        gap: 16px !important;
        scrollbar-width: none;
      }
      .why-grid::-webkit-scrollbar, .bento-grid::-webkit-scrollbar, .doctor-stats::-webkit-scrollbar, .counter-grid::-webkit-scrollbar, .faq-grid::-webkit-scrollbar {
        display: none;
      }
      .why-grid > *, .bento-grid > *, .doctor-stats > *, .counter-grid > *, .faq-grid > * {
        flex: 0 0 85% !important;
        scroll-snap-align: center !important;
      }
    }
'''
style_end_pattern = r'(</style>)'
content = re.sub(style_end_pattern, grid_css + r'\g<1>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done updating index.html')
