import re

with open('project-shipment.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Title
content = content.replace(
    '<title>Consumer360 Retail Analytics | Case Study</title>',
    '<title>Shipment Risk Analysis | Case Study</title>'
)

# Replace Header
header_old = """    <!-- PROJECT HEADER -->
    <div class="cs-header reveal">
      <h1 class="cs-title">Consumer360 : Retail Analytics - Customer Segmentation & Churn Analysis</h1>
      <p class="cs-desc">Developed an end-to-end retail analytics system to analyze customer purchasing behavior,
        perform RFM-based segmentation, and identify churn-risk customers. Built automated ETL pipelines and interactive
        dashboards to deliver a complete Customer 360° view for business decision-making.</p>

      <div class="cs-tags">
        <span class="cs-tag">SQL</span>
        <span class="cs-tag">Python (Pandas, NumPy)</span>
        <span class="cs-tag">Power BI</span>
        <span class="cs-tag">RFM Analysis</span>
        <span class="cs-tag">Customer Segmentation</span>
        <span class="cs-tag">ETL Pipeline</span>
        <span class="cs-tag">Data Visualization</span>
      </div>
    </div>"""

header_new = """    <!-- PROJECT HEADER -->
    <div class="cs-header reveal">
      <h1 class="cs-title">Shipment Risk Analysis & Late Delivery Prediction</h1>
      <p class="cs-desc">A data-driven supply chain analytics solution that predicts late deliveries and categorizes shipment risk using machine learning, combined with an interactive Power BI dashboard for business insights and decision-making.</p>

      <div class="cs-tags">
        <span class="cs-tag">Python</span>
        <span class="cs-tag">Machine Learning</span>
        <span class="cs-tag">Power BI</span>
        <span class="cs-tag">Supply Chain Analytics</span>
        <span class="cs-tag">Predictive Modeling</span>
        <span class="cs-tag">Data Visualization</span>
      </div>
    </div>"""
content = content.replace(header_old, header_new)

# Replace the content section from dashboard slider to the end of the content wrapper
# We'll use regex to match from <!-- DASHBOARD SLIDER --> up to <div style="text-align: center; margin-top: 60px; margin-bottom: 40px;">

content_new = """    <!-- HERO IMAGE -->
    <div class="slider-wrapper reveal">
      <div class="slider-viewport" style="height: 500px; overflow: hidden; border-radius: var(--border-radius-lg); box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6); position: relative; border: 1px solid rgba(192, 183, 232, 0.1);">
        <img src="https://images.unsplash.com/photo-1586528116311-ad8ed7c83a50?q=80&w=1200&auto=format&fit=crop" alt="Shipment Risk Analysis" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
    </div>

      <!-- CONTENT SECTIONS -->
      <div class="cs-content-wrap">

        <div class="cs-section reveal">
          <h2 class="cs-section-title">📌 Problem Statement</h2>
          <p class="cs-text">Late deliveries significantly impact customer satisfaction, operational efficiency, and logistics costs. In the absence of predictive systems, businesses rely on reactive approaches, leading to missed opportunities for optimization.</p>
          <p class="cs-text" style="margin-top: 15px;"><strong>This project addresses:</strong> How can we predict shipment delays in advance and proactively manage high-risk deliveries?</p>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">⚙️ Approach & Methodology</h2>
          <ul class="cs-text">
            <li>Performed data cleaning and preprocessing on 180K+ shipment records</li>
            <li>Conducted exploratory data analysis to identify delay patterns</li>
            <li>Engineered features like Shipping Delay (Actual vs Scheduled)</li>
            <li>Built classification models: Logistic Regression (baseline) and Random Forest (final model)</li>
            <li>Achieved ~70% accuracy in predicting late deliveries</li>
            <li>Generated prediction probabilities and categorized risk: High Risk (>70%), Medium Risk (40–70%), Low Risk (<40%)</li>
            <li>Developed interactive Power BI dashboards for visualization and insights</li>
          </ul>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">🧠 Concepts & Skills Applied</h2>
          <div class="concepts-grid">
            <div class="concept-chip">
              <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14.5v-9l6 4.5-6 4.5z"/></svg> Predictive Analytics
            </div>
            <div class="concept-chip">
              <svg viewBox="0 0 24 24"><path d="M4 10h3v7H4zM10.5 10h3v7h-3zM2 19h20v3H2zM17 10h3v7h-3zM12 1L2 6v2h20V6L12 1z"/></svg> Machine Learning
            </div>
            <div class="concept-chip">
              <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg> Feature Engineering
            </div>
            <div class="concept-chip">
              <svg viewBox="0 0 24 24"><path d="M3 3h18v18H3V3zm16 16V5H5v14h14zm-4-4h-4v-4h4v4zm-6 0H5v-4h4v4zm6-6h-4V5h4v4zm-6 0H5V5h4v4z"/></svg> Power BI
            </div>
          </div>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">📊 Key Insights</h2>
          <ul class="insights-list">
            <li><strong>38.29% of shipments are delivered late</strong>, exceeding operational benchmarks</li>
            <li><strong>Over 10,000 shipments classified as High Risk</strong>, requiring immediate attention</li>
            <li><strong>Standard Class shipping</strong> contributes the highest delay rate</li>
            <li><strong>Same Day shipping</strong> shows the best performance</li>
            <li><strong>Medium-risk shipments</strong> represent the biggest opportunity for improvement</li>
            <li><strong>Shipping schedule and mode</strong> are the strongest predictors of delays</li>
          </ul>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">📈 Dashboard Highlights</h2>
          <ul class="cs-text">
            <li>Executive Overview with KPIs and Late Delivery Rate</li>
            <li>Risk Distribution (High / Medium / Low)</li>
            <li>Shipping Mode Performance Analysis</li>
            <li>Regional Delivery Performance</li>
            <li>Strategic Insights & Recommendations</li>
          </ul>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">💼 Business Recommendations & Impact</h2>
          <ul class="cs-text">
            <li>Prioritize monitoring of high-risk shipments</li>
            <li>Optimize Standard Class logistics operations</li>
            <li>Implement automated risk alert systems</li>
            <li>Upgrade shipping mode for high-value orders</li>
            <li>Closely monitor medium-risk shipments</li>
          </ul>
          <p class="cs-text" style="margin-top: 15px;"><strong>Expected Impact:</strong><br>
          • 15–20% reduction in late deliveries<br>
          • 12–18% improvement in operational efficiency<br>
          • 8–12% reduction in logistics costs<br>
          • 10–15% improvement in customer satisfaction</p>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">⚡ Advanced Features</h2>
          <ul class="cs-text">
            <li><strong>Machine Learning-based</strong> delay prediction</li>
            <li><strong>Risk categorization</strong> using probability thresholds</li>
            <li><strong>Feature importance analysis</strong> for explainability</li>
            <li><strong>Interactive Power BI dashboard</strong> for decision support</li>
            <li><strong>End-to-end pipeline:</strong> Data → Model → Insights → Business Action</li>
          </ul>
        </div>"""

pattern = r'<!-- DASHBOARD SLIDER -->.*?<div style="text-align: center; margin-top: 60px; margin-bottom: 40px;">'
content = re.sub(pattern, content_new + '\n\n        <div style="text-align: center; margin-top: 60px; margin-bottom: 40px;">', content, flags=re.DOTALL)

# Update Github Link
content = content.replace(
    '<a href="https://github.com/Gaurii15/Consumer360-Retail-Analytics-Customer-Segmentation-Churn-Analysis"',
    '<a href="https://github.com"'
)

with open('project-shipment.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated project-shipment.html")
