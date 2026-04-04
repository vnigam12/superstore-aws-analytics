# QuickSight Dashboard Design – Superstore Analytics

## Objective
Design an interactive dashboard to analyze sales, profit, and customer trends using the Superstore dataset. The goal is to enable business stakeholders to make data-driven decisions.

---

## Dataset Overview
- Source: Sample Superstore dataset
- Grain: Order-level data
- Key Dimensions:
  - Region
  - Category / Sub-Category
  - Segment
  - Customer Name
  - Order Date
- Key Metrics:
  - Sales
  - Profit
  - Quantity
  - Discount

---

## Dashboard Layout

### Section 1: KPI Summary (Top Panel)
**Purpose:** Provide a quick snapshot of business performance

**Visuals:**
- Total Sales (KPI)
- Total Profit (KPI)
- Profit Ratio (%) (KPI)
- Total Orders (KPI)

---

### Section 2: Sales Performance

**1. Sales by Region**
- Type: Bar Chart / Map
- X-axis: Region
- Y-axis: Total Sales
- Insight: Identify top-performing regions

**2. Monthly Sales Trend**
- Type: Line Chart
- X-axis: Order Date (Month)
- Y-axis: Sales
- Insight: Seasonality and growth trends

---

### Section 3: Profitability Analysis

**1. Profit by Category**
- Type: Bar Chart
- X-axis: Category
- Y-axis: Profit
- Insight: Which categories drive profitability

**2. Profit vs Discount**
- Type: Scatter Plot
- X-axis: Discount
- Y-axis: Profit
- Insight: Impact of discounting on profit

---

### Section 4: Customer Insights

**1. Top Customers**
- Type: Table
- Columns: Customer Name, Sales, Profit
- Insight: High-value customers

**2. Sales by Segment**
- Type: Pie Chart / Donut Chart
- Segments: Consumer, Corporate, Home Office
- Insight: Revenue contribution by segment

---

### Section 5: Product Analysis

**1. Top Sub-Categories**
- Type: Horizontal Bar Chart
- Metric: Sales or Profit
- Insight: Best-performing products

---

## Filters (Interactive Controls)

- Region
- Category
- Segment
- Order Date (Date Range)

Filters should apply across all visuals for interactivity.

---

## Design Guidelines

- Use consistent color palette:
  - Sales → Blue
  - Profit → Green
  - Loss → Red
- Avoid clutter; limit visuals per section
- Add clear titles and labels
- Use tooltips for deeper insights

---

## Calculated Fields

**1. Profit Ratio**