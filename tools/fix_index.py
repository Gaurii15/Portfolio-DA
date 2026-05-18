import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace from the end of the Instagram link to the end of the file.
# We'll match from `<a href="#" aria-label="Instagram">` to the end.

pattern = r'<a href="#" aria-label="Instagram">.*?</html>'

correct_html = """<a href="#" aria-label="Instagram">
            <svg viewBox="0 0 24 24">
              <path
                d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
            </svg>
          </a>
        </div>
      </div>

      <div class="hero-img-col reveal-right fade-in-slow">
        <!-- Faded Translucent Background Words -->
        <div class="bg-words-container">
          <span class="bg-word">Analysis</span>
          <span class="bg-word">Insights</span>
          <span class="bg-word">Impact</span>
          <span class="bg-word">Data</span>
          <span class="bg-word">Models</span>
          <span class="bg-word">Trends</span>
          <span class="bg-word">Dashboard</span>
        </div>

        <!-- Floating mini cards -->
        <div class="mini-card card-1 float-anim">
          <div class="mini-card-icon">
            <svg viewBox="0 0 24 24">
              <path
                d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-1.25 17.292l-4.5-4.364 1.857-1.858 2.643 2.506 5.643-5.784 1.857 1.857-7.5 7.643z" />
            </svg>
          </div>
          <div class="mini-card-content">
            <h4>Insights</h4>
            <p>Generated</p>
          </div>
        </div>

        <div class="mini-card card-2 float-anim">
          <div class="mini-card-icon">
            <svg viewBox="0 0 24 24">
              <path
                d="M18 10v-4c0-3.313-2.687-6-6-6s-6 2.687-6 6v4h-3v14h18v-14h-3zm-10-4c0-2.206 1.794-4 4-4s4 1.794 4 4v4h-8v-4zm5 11.259v2.741h-2v-2.741c-.596-.346-1-.984-1-1.716 0-1.104.896-2 2-2s2 .896 2 2c0 .732-.404 1.37-1 1.716z" />
            </svg>
          </div>
          <div class="mini-card-content">
            <h4>Dashboards</h4>
            <p>Created</p>
          </div>
        </div>

        <div class="mini-card card-3 float-anim">
          <div class="mini-card-icon">
            <svg viewBox="0 0 24 24">
              <path
                d="M21.698 10.658l2.302 1.342-12.002 7-11.998-7 2.301-1.342 9.697 5.658 9.7-5.658zm-9.7 10.657l-9.697-5.658-2.301 1.343 11.998 7 12.002-7-2.302-1.342-9.7 5.657zm12.002-14.315l-12.002-7-11.998 7 11.998 7 12.002-7z" />
            </svg>
          </div>
          <div class="mini-card-content">
            <h4>Data Driven</h4>
            <p>Decisions</p>
          </div>
        </div>

        <div class="circular-img-wrapper float-anim" style="animation-duration: 8s;">
          <img src="Self_img/corporateimage.jpeg" alt="Gauri Profile Image">
        </div>
      </div>
    </section>

    <div class="achievements-container reveal" style="transition-delay: 0.5s;">
      <div class="achievements-grid">
        <div class="achievement-card">
          <span class="ach-top"><span class="stat-count" data-target="147" data-suffix="K+">0</span> ROWS</span>
          <span class="ach-bottom">DATA ANALYZED</span>
        </div>
        <div class="achievement-card">
          <span class="ach-top"><span class="stat-count" data-target="4" data-suffix="+">0</span> PROJECTS</span>
          <span class="ach-bottom">END-TO-END ANALYTICS</span>
        </div>
        <div class="achievement-card">
          <span class="ach-top">INSIGHT DELIVERY</span>
          <span class="ach-bottom">DATA → DECISIONS</span>
        </div>
        <div class="achievement-card">
          <span class="ach-top">AI WORKFLOW</span>
          <span class="ach-bottom">AUTOMATION & PRODUCTIVITY</span>
        </div>
      </div>
    </div>
  </div>

  <script src="js/animations.js"></script>
</body>

</html>"""

content = re.sub(pattern, correct_html, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed index.html structure.")
