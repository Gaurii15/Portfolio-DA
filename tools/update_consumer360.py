import re

with open('project-consumer360.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Header
header_pattern = r'<!-- PROJECT HEADER -->.*?</div>\s*</div>'

new_header = """<!-- PROJECT HEADER -->
    <div class="cs-header reveal">
      <h1 class="cs-title">Consumer360 – Customer Segmentation & Churn Analysis</h1>
      <p class="cs-desc">An end-to-end retail analytics solution that analyzes customer behavior, segments customers using RFM analysis, and identifies churn risks through an integrated pipeline of SQL, Python, and Power BI.</p>

      <div class="cs-tags">
        <span class="cs-tag">Customer Segmentation (RFM Analysis)</span>
        <span class="cs-tag">Churn Analysis</span>
        <span class="cs-tag">Customer Lifetime Value (CLV)</span>
        <span class="cs-tag">SQL Data Processing</span>
        <span class="cs-tag">ETL Pipeline Development</span>
        <span class="cs-tag">Data Visualization (Power BI)</span>
        <span class="cs-tag">Business Intelligence & Analytics</span>
      </div>
    </div>"""

content = re.sub(header_pattern, new_header, content, flags=re.DOTALL, count=1)

# Replace the content sections from <!-- CONTENT SECTIONS --> to the bottom div

pattern2 = r'<!-- CONTENT SECTIONS -->.*?<div style="text-align: center; margin-top: 60px; margin-bottom: 40px;">'

new_content = """<!-- CONTENT SECTIONS -->
      <div class="cs-content-wrap">

        <div class="cs-section reveal">
          <h2 class="cs-section-title">📌 Problem Statement</h2>
          <p class="cs-text">Retail businesses often lack visibility into customer behavior, making it difficult to identify high-value customers and detect early signs of churn.</p>
          <p class="cs-text" style="margin-top: 15px;"><strong>Key challenges include:</strong></p>
          <ul class="cs-text">
            <li>Inability to identify profitable customer segments</li>
            <li>Lack of insights into customer engagement and retention</li>
            <li>Difficulty in designing targeted marketing strategies</li>
            <li>Absence of a unified Customer 360° analytical view</li>
          </ul>
          <p class="cs-text" style="margin-top: 15px;"><strong>This project addresses:</strong> How can businesses segment customers effectively and proactively reduce churn using data-driven insights?</p>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">⚙️ Approach & Methodology</h2>
          <ul class="cs-text">
            <li>Extracted and cleaned retail data using SQL</li>
            <li>Performed data aggregation and transformation for analysis</li>
            <li>Conducted RFM (Recency, Frequency, Monetary) analysis using Python</li>
            <li>Calculated Customer Lifetime Value (CLV) for segment evaluation</li>
            <li>Segmented customers into: Champions, Loyal Customers, At Risk, Low Engagement</li>
            <li>Built automated ETL pipeline for data processing and refresh</li>
            <li>Developed interactive Power BI dashboards for business insights</li>
          </ul>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">🧠 Concepts & Skills Applied</h2>
          <div class="concepts-grid">
            <div class="concept-chip">
              <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14.5v-9l6 4.5-6 4.5z"/></svg> RFM Analysis
            </div>
            <div class="concept-chip">
              <svg viewBox="0 0 24 24"><path d="M4 10h3v7H4zM10.5 10h3v7h-3zM2 19h20v3H2zM17 10h3v7h-3zM12 1L2 6v2h20V6L12 1z"/></svg> SQL Processing
            </div>
            <div class="concept-chip">
              <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg> Power BI
            </div>
            <div class="concept-chip">
              <svg viewBox="0 0 24 24"><path d="M3 3h18v18H3V3zm16 16V5H5v14h14zm-4-4h-4v-4h4v4zm-6 0H5v-4h4v4zm6-6h-4V5h4v4zm-6 0H5V5h4v4z"/></svg> ETL Pipeline
            </div>
          </div>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">📊 Key Insights</h2>
          <ul class="insights-list">
            <li><strong>Champion customers</strong> contribute the highest revenue and CLV</li>
            <li><strong>At-Risk customers</strong> show declining engagement and higher recency values</li>
            <li><strong>West and South regions</strong> generate the highest sales</li>
            <li><strong>Electronics and Clothing</strong> dominate total revenue contribution</li>
            <li>A small percentage of customers contribute a large portion of revenue <strong>(Pareto Principle)</strong></li>
            <li><strong>Loyal customers</strong> provide stable and recurring revenue</li>
            <li><strong>Low-engagement customers</strong> indicate untapped growth opportunities</li>
          </ul>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">📈 Dashboard Highlights</h2>
          <p class="cs-text"><strong>⭐ Retail Performance Dashboard</strong></p>
          <ul class="cs-text">
            <li>Total Sales, Orders, Customers, Quantity</li>
            <li>Monthly Sales Trends</li>
            <li>Sales by Region & Country</li>
            <li>Product & Category Performance</li>
          </ul>
          <p class="cs-text" style="margin-top: 15px;"><strong>⭐ Customer Segmentation Dashboard</strong></p>
          <ul class="cs-text">
            <li>RFM-based customer segmentation</li>
            <li>CLV analysis</li>
            <li>Churn Risk vs Active Customers</li>
            <li>Segment-wise contribution and behavior</li>
          </ul>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">💼 Business Recommendations & Impact</h2>
          <ul class="cs-text">
            <li>Launch targeted retention campaigns for At-Risk customers</li>
            <li>Introduce loyalty programs for Champions and Loyal segments</li>
            <li>Increase marketing investment in high-performing regions</li>
            <li>Promote high-performing product categories strategically</li>
            <li>Implement personalized product recommendations</li>
            <li>Monitor churn-risk segments proactively</li>
          </ul>
          <p class="cs-text" style="margin-top: 15px;"><strong>Expected Impact:</strong><br>
          • Improved customer retention and reduced churn<br>
          • Increased revenue through targeted marketing<br>
          • Better customer segmentation and engagement strategies<br>
          • Enhanced decision-making using Customer 360° insights</p>
        </div>

        <div class="cs-section reveal">
          <h2 class="cs-section-title">⚡ Advanced Features</h2>
          <ul class="cs-text">
            <li><strong>RFM-based segmentation</strong> for customer classification</li>
            <li><strong>Customer Lifetime Value (CLV)</strong> calculation</li>
            <li><strong>Automated ETL pipeline</strong> using Python & Task Scheduler</li>
            <li><strong>Multi-tool integration</strong> (SQL + Python + Power BI)</li>
            <li><strong>Real-world retail analytics</strong> workflow simulation</li>
            <li><strong>Dynamic Power BI dashboards</strong> for business decision-making</li>
          </ul>
        </div>

        <div style="text-align: center; margin-top: 60px; margin-bottom: 40px;">"""

content = re.sub(pattern2, new_content, content, flags=re.DOTALL)

with open('project-consumer360.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated project-consumer360.html")
