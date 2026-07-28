# Quality Metrics Extended

## Advanced Quality Metrics and KPIs

---

## Source References
- FDA 21 CFR Part 211
- ICH Q10
- EU GMP Chapter 1
- Date Retrieved: 2026-07-28
- Confidence: 0.93

---

## Key Performance Indicators (KPIs)

### 1. Quality System Metrics

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| **CAPA Closure Rate** | (Closed CAPAs / Total CAPAs) × 100 | ≥90% | Monthly |
| **CAPA On-Time Closure** | (On-time closures / Total closures) × 100 | ≥85% | Monthly |
| **Deviation Rate** | (Total deviations / Total batches) × 100 | <2% | Monthly |
| **Deviation Closure Rate** | (Closed deviations / Total deviations) × 100 | ≥95% | Monthly |
| **OOS Rate** | (OOS results / Total tests) × 100 | <1% | Monthly |
| **Complaint Rate** | (Total complaints / Total units sold) × 1M | <100 PPM | Monthly |
| **Complaint Response Time** | Average days to respond | <30 days | Monthly |
| **Recall Effectiveness** | (Units recovered / Units distributed) × 100 | ≥95% | Per recall |
| **Supplier Qualification Rate** | (Qualified suppliers / Total suppliers) × 100 | ≥95% | Quarterly |
| **Training Compliance** | (Trained personnel / Total personnel) × 100 | ≥95% | Monthly |

### 2. Manufacturing Metrics

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| **Batch Success Rate** | (Successful batches / Total batches) × 100 | ≥98% | Monthly |
| **First Pass Yield** | (Batches passing first time / Total batches) × 100 | ≥95% | Monthly |
| **Right First Time (RFT)** | (RFT batches / Total batches) × 100 | ≥95% | Monthly |
| **OEE (Overall Equipment Effectiveness)** | Availability × Performance × Quality | ≥75% | Monthly |
| **Unplanned Downtime** | (Unplanned downtime hours / Total hours) × 100 | <5% | Monthly |
| **Changeover Time** | Average time for product change | Reduce 10% YoY | Quarterly |
| **Scrap Rate** | (Scrap quantity / Total production) × 100 | <2% | Monthly |
| **Rework Rate** | (Rework quantity / Total production) × 100 | <1% | Monthly |

### 3. Laboratory Metrics

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| **Sample Turnaround Time** | Average days from receipt to result | <7 days | Monthly |
| **Method Success Rate** | (Successful methods / Total methods) × 100 | ≥98% | Quarterly |
| **Instrument Calibration Compliance** | (Calibrated on time / Total calibrations) × 100 | ≥100% | Monthly |
| **Stability Study Compliance** | (Studies on time / Total studies) × 100 | ≥100% | Quarterly |
| **OOS Investigation Rate** | (OOS investigations / Total OOS) × 100 | 100% | Monthly |
| **OOS Closure Rate** | (Closed investigations / Total investigations) × 100 | ≥95% | Monthly |

### 4. Supply Chain Metrics

| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| **Supplier Quality Agreement Coverage** | (SQAs in place / Total critical suppliers) × 100 | 100% | Quarterly |
| **Incoming Material Rejection Rate** | (Rejected materials / Total received) × 100 | <2% | Monthly |
| **Supplier CAPA Rate** | (Supplier CAPAs / Total supplier issues) × 100 | Track | Quarterly |
| **Supply Continuity** | (Orders fulfilled on time / Total orders) × 100 | ≥98% | Monthly |
| **Inventory Accuracy** | (Accurate counts / Total counts) × 100 | ≥99% | Quarterly |

---

## Quality Dashboards

### Dashboard 1: Executive Quality Overview

```
+----------------------------------+----------------------------------+
| Quality System Health            | CAPA Status                      |
| • CAPA Closure Rate: 92%        | • Open: 15                       |
| • Deviation Rate: 1.8%          | • In Progress: 8                 |
| • Complaint Rate: 85 PPM        | • Closed (MTD): 25              |
+----------------------------------+----------------------------------+
| Manufacturing Performance       | Regulatory Compliance            |
| • Batch Success: 98.5%          | • Audit Findings: 5             |
| • RFT: 96%                      | • Warning Letters: 0             |
| • OEE: 78%                      | • Recalls: 0                     |
+----------------------------------+----------------------------------+
```

### Dashboard 2: Detailed Quality Metrics

| Category | Metric | Current | Target | Trend |
|----------|--------|---------|--------|-------|
| **Quality** | CAPA Closure | 92% | 90% | ↑ |
| **Quality** | Deviation Rate | 1.8% | <2% | ↓ |
| **Quality** | OOS Rate | 0.8% | <1% | ↓ |
| **Manufacturing** | Batch Success | 98.5% | ≥98% | ↑ |
| **Manufacturing** | RFT | 96% | ≥95% | ↑ |
| **Manufacturing** | OEE | 78% | ≥75% | ↑ |
| **Laboratory** | TAT | 5 days | <7 days | ↓ |
| **Supply Chain** | Supplier Qual | 96% | ≥95% | ↑ |

---

## Trend Analysis

### 1. Quality Trend Monitoring

| Trend Type | Method | Frequency | Action |
|------------|--------|-----------|--------|
| **Upward Trend** | Regression analysis | Monthly | Investigate if >2σ |
| **Downward Trend** | Regression analysis | Monthly | Monitor |
| **Seasonal** | Time series | Quarterly | Plan mitigation |
| **Cyclical** | Pattern analysis | Annually | Process improvement |

### 2. Statistical Process Control (SPC)

| Control Chart | Application | Control Limits |
|---------------|-------------|----------------|
| **X-bar chart** | Process mean | UCL/LCL = X̄ ± 3σ |
| **R-chart** | Process variability | UCL = D4 × R̄, LCL = D3 × R̄ |
| **p-chart** | Attribute data | UCL/LCL = p̄ ± 3√(p̄(1-p̄)/n) |
| **c-chart** | Defects per unit | UCL/LCL = c̄ ± 3√c̄ |

### 3. Capability Indices

| Index | Formula | Interpretation |
|-------|---------|----------------|
| **Cp** | (USL - LSL) / 6σ | Process potential |
| **Cpk** | min[(USL - X̄)/3σ, (X̄ - LSL)/3σ] | Process centering |
| **Pp** | (USL - LSL) / 6σ (overall) | Overall capability |
| **Ppk** | min[(USL - X̄)/3σ, (X̄ - LSL)/3σ] (overall) | Overall centering |

| Cpk Value | Interpretation | Action |
|-----------|----------------|--------|
| ≥1.67 | Excellent | Continue monitoring |
| 1.33-1.67 | Good | Monitor |
| 1.0-1.33 | Marginal | Improve |
| <1.0 | Poor | Immediate improvement |

---

## Quality Risk Metrics

### 1. Risk Assessment Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Risk Assessment Completion** | (Completed / Total identified) × 100 | 100% |
| **High Risk Closure Rate** | (Closed high risks / Total high risks) × 100 | 100% |
| **Risk Review Compliance** | (Reviews completed on time / Total reviews) × 100 | ≥95% |
| **Residual Risk Acceptance** | (Accepted residual risks / Total residual risks) × 100 | ≥90% |

### 2. Risk KPIs

| KPI | Target | Frequency |
|-----|--------|-----------|
| **Risk Assessment Timeliness** | 100% on time | Quarterly |
| **Risk Mitigation Effectiveness** | ≥80% effective | Semi-annually |
| **Risk Communication** | 100% stakeholders informed | Ongoing |

---

## Benchmarking

### Industry Benchmarks

| Metric | Industry Average | Best-in-Class | Your Organization |
|--------|------------------|---------------|-------------------|
| **CAPA Closure Rate** | 85% | 95% | 92% |
| **Deviation Rate** | 2.5% | <1% | 1.8% |
| **Complaint Rate** | 150 PPM | <50 PPM | 85 PPM |
| **Batch Success Rate** | 95% | 99% | 98.5% |
| **OEE** | 65% | 85% | 78% |
| **Training Compliance** | 90% | 100% | 96% |

---

## Quality Metrics Reporting

### Monthly Quality Report Structure

| Section | Content |
|---------|---------|
| **Executive Summary** | Key highlights |
| **Quality System Metrics** | CAPA, deviation, complaint metrics |
| **Manufacturing Metrics** | Batch, OEE, yield metrics |
| **Laboratory Metrics** | TAT, OOS, calibration metrics |
| **Supply Chain Metrics** | Supplier, incoming material metrics |
| **Trend Analysis** | 6-12 month trends |
| **Action Items** | Improvement actions |

### Quarterly Quality Review

| Section | Content |
|---------|---------|
| **Quarterly Summary** | Performance vs. targets |
| **Trend Analysis** | Quarter-over-quarter trends |
| **Benchmarking** | Industry comparison |
| **Risk Assessment** | Updated risk profile |
| **Strategic Initiatives** | Improvement projects |

---

## Metadata

```json
{
  "document_id": "quality_metrics_extended",
  "category": "quality_metrics",
  "subcategory": "advanced_quality_kpis",
  "source_type": "FDA/ICH/EU_GMP",
  "authority": "FDA/ICH/EU GMP",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.93,
  "tags": ["Quality_Metrics", "KPIs", "Dashboard", "Trend_Analysis", "SPC", "Capability", "Benchmarking"]
}
```