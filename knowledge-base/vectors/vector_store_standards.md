# Vector Store Standards

## Comprehensive Standards for Vector Database Management in Pharmaceutical QMS

---

## Source References
- Pinecone: Vector Database Documentation
- Weaviate: Vector Search Engine
- ChromaDB: Open-source Embedding Database
- Qdrant: Vector Similarity Search
- FAISS: Facebook AI Similarity Search
- pgvector: PostgreSQL Vector Extension
- Milvus: Vector Database
- Weaviate: GraphQL API Documentation
- Date Retrieved: 2026-07-28
- Confidence: 0.93

---

## 1. Vector Store Categories

### 1.1 Core Vector Store Categories

| Category | Purpose | Content Type | Update Frequency |
|----------|---------|--------------|------------------|
| **Semantic Search** | Knowledge base semantic queries | Documents, paragraphs, sentences | Daily/Batch |
| **Complaint Understanding** | Complaint text classification | Complaint text, ADR reports | Real-time/Batch |
| **Document Similarity** | Document similarity detection | Regulatory documents, SOPs, deviations | Daily/Batch |
| **Product Matching** | Product master data search | Product names, specifications, ingredients | Daily/Batch |
| **Root Cause Analysis** | Investigation similarity search | Investigation reports, RCA documents | Daily/Batch |
| **Regulatory Intelligence** | Regulatory document search | FDA, EMA, ICH, WHO guidance | Weekly |
| **Training Content** | Training material search | SOPs, training documents, assessments | Daily |
| **Equipment Knowledge** | Equipment documentation search | Manual specs, maintenance logs, validation docs | Weekly |
| **Risk Assessment** | Risk document similarity | FMEA, risk assessments, incident reports | Daily |

---

## 2. Embedding Models

### 2.1 Model Selection Guide

| Model Family | Dimensions | Performance | Cost | Use Case |
|--------------|------------|-------------|------|----------|
| **OpenAI text-embedding-3-small** | 1536 | Good | Low | General purpose |
| **OpenAI text-embedding-3-large** | 3072 | Best | High | High-precision search |
| **Cohere embed-multilingual-v3.0** | 1024 | Good | Medium | Multilingual content |
| **BGE-large-en-v1.5** | 1024 | Good | Free (open-source) | On-premise, cost-sensitive |
| **E5-large-v2** | 1024 | Good | Free (open-source) | On-premise, cost-sensitive |
| **GTE-large** | 1024 | Good | Free (open-source) | On-premise, cost-sensitive |
| **Jina-embeddings-v2-base-en** | 768 | Good | Free (open-source) | Long-context documents |

### 2.2 Model Evaluation Criteria

| Criterion | Weight | Assessment Method |
|-----------|--------|-------------------|
| **Semantic Accuracy** | 30% | Benchmark on pharma-specific queries |
| **Retrieval Precision@10** | 25% | Gold-standard query-document pairs |
| **Multilingual Support** | 15% | Content in English, French, German, Japanese |
| **Latency (p95)** | 15% | < 100ms for single document embedding |
| **Cost per 1M Tokens** | 10% | $0.01–$0.10 per 1M tokens |
| **Context Length** | 5% | 512–8192 tokens depending on model |

---

## 3. Chunking Strategies

### 3.1 Chunking Methods

| Method | Chunk Size | Overlap | Use Case |
|--------|------------|---------|----------|
| **Fixed-size** | 512 tokens | 50 tokens | General purpose, quick setup |
| **Semantic** | 100–1000 tokens | 50–200 tokens | High-quality semantic search |
| **Recursive** | 500 tokens | 50 tokens | Hierarchical documents (SOPs, regulations) |
| **Paragraph** | Variable | None | Documents with clear paragraph structure |
| **Sentence** | Variable | None | Fine-grained search |
| **Document** | Full document | None | Document-level similarity |
| **Custom (pharma)** | Configurable | Configurable | Pharmaceutical-specific content |

### 3.2 Pharma-Specific Chunking Rules

| Content Type | Recommended Method | Chunk Size | Overlap | Notes |
|--------------|-------------------|------------|---------|-------|
| **SOPs** | Semantic | 800–1200 tokens | 100 tokens | Chunk by logical sections |
| **Deviation Reports** | Paragraph | 500–1000 tokens | 0 | Chunk by sections (Description, Investigation, CAPA) |
| **Regulatory Documents** | Recursive | 1000 tokens | 100 tokens | Respect document hierarchy |
| **Batch Records** | Fixed-size | 512 tokens | 50 tokens | Chunk by step/stage |
| **Complaint Texts** | Sentence | 200–500 tokens | 50 tokens | Fine-grained search |
| **Stability Data** | Fixed-size | 512 tokens | 50 tokens | Time-series chunking |
| **Training Materials** | Semantic | 500–1000 tokens | 100 tokens | Chunk by learning objectives |
| **Equipment Manuals** | Semantic | 800–1200 tokens | 100 tokens | Chunk by section/subsection |
| **Risk Assessments** | Paragraph | 500–1000 tokens | 0 | Chunk by risk item |

---

## 4. Vector Store Implementation

### 4.1 Technology Comparison

| Technology | Performance | Scalability | Features | Use Case |
|------------|-------------|-------------|----------|----------|
| **Pinecone** | High | High (managed) | Metadata filtering, hybrid search | Production SaaS |
| **Weaviate** | High | High (distributed) | GraphQL, hybrid search, multi-tenancy | Production (complex queries) |
| **Qdrant** | High | High (distributed) | Payload filtering, named vectors, hybrid search | Production (high performance) |
| **ChromaDB** | Medium | Low (single node) | Simple API, metadata filtering | Development/small projects |
| **pgvector** | Medium | Medium (PostgreSQL) | SQL queries, PostgreSQL ecosystem | PostgreSQL-based projects |
| **Milvus** | High | High (distributed) | GPU acceleration, partition keys | Large-scale production |
| **FAISS** | High | Medium (single node) | Facebook optimization, GPU support | Research, high-performance computing |

### 4.2 Recommended Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Application Layer                       │
│  (QMS Web UI, AI Agents, Search Interface, API Gateway)     │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                     Vector Store Layer                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Pinecone    │  │ Weaviate    │  │ PostgreSQL (pgvec)  │ │
│  │ (Primary)   │  │ (Hybrid)    │  │ (Structured + Vec) │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                     Embedding Layer                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ OpenAI      │  │ BGE/E5      │  │ Custom Fine-tuned   │ │
│  │ (Cloud)     │  │ (On-prem)   │  │ (Domain-specific)   │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                     Data Layer                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Document DB │  │ Object Store│  │ Data Warehouse      │ │
│  │ (MongoDB)   │  │ (S3/Blob)   │  │ (Snowflake/BigQuery)│ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Metadata Filtering

### 5.1 Common Metadata Fields

| Field | Type | Example | Filter Operations |
|-------|------|---------|-------------------|
| **category** | string | "deviation" | eq, in, neq |
| **product** | string | "Lipitor 10mg" | eq, in, contains |
| **batch** | string | "LOT20260715A" | eq, in |
| **severity** | string | "Critical" | eq, in, neq |
| **status** | string | "Closed" | eq, in, neq |
| **date** | date | "2026-07-28" | gte, lte, between |
| **author** | string | "J. Smith" | eq, in |
| **department** | string | "Quality Assurance" | eq, in |
| **site** | string | "US-Site-A" | eq, in |
| **regulatory_body** | string | "FDA" | eq, in |

### 5.2 Filtering Patterns

```python
# Example: Filter deviations for Lipitor product, Critical severity, FDA-related
filters = {
    "must": [
        {"field": "category", "operator": "eq", "value": "deviation"},
        {"field": "product", "operator": "contains", "value": "Lipitor"},
        {"field": "severity", "operator": "in", "value": ["Critical", "Major"]},
        {"field": "date", "operator": "gte", "value": "2024-01-01"},
        {"field": "regulatory_body", "operator": "in", "value": ["FDA", "EMA"]}
    ]
}
```

---

## 6. Hybrid Search

### 6.1 Hybrid Search Strategy

| Component | Weight | Purpose |
|-----------|--------|---------|
| **Dense (Semantic) Search** | 70% | Meaning-based retrieval |
| **Sparse (BM25/Keyword) Search** | 20% | Exact term matching |
| **Metadata Filtering** | 10% | Structured constraint enforcement |

### 6.2 Hybrid Search Configuration

```yaml
hybrid_search:
  dense:
    model: "text-embedding-3-large"
    k: 20
    weight: 0.7
  sparse:
    algorithm: "BM25"
    k: 20
    weight: 0.2
  metadata:
    enabled: true
    weight: 0.1
  reranking:
    enabled: true
    model: "cohere-rerank-v3.5"
    top_n: 10
  fusion:
    method: "RRF"  # Reciprocal Rank Fusion
    rrf_k: 60
```

---

## 7. Data Quality & Monitoring

### 7.1 Vector Quality Metrics

| Metric | Definition | Target | Measurement |
|--------|------------|--------|-------------|
| **Embedding Coverage** | % documents with valid embeddings | 100% | Count(embeddings) / Count(documents) |
| **Embedding Freshness** | Time since last embedding update | < 24 hours | Current time - max(embedding_timestamp) |
| **Retrieval Precision@5** | % relevant results in top 5 | > 80% | Manual evaluation on gold set |
| **Retrieval Recall@20** | % relevant results found in top 20 | > 90% | Manual evaluation on gold set |
| **Latency (p95)** | 95th percentile query latency | < 200ms | Metrics aggregation |
| **Index Size** | Total vector count | Monitor | System metrics |
| **Memory Usage** | Vector store memory consumption | < 80% capacity | System metrics |

### 7.2 Monitoring & Alerting

| Alert | Threshold | Action |
|-------|-----------|--------|
| **Embedding Latency High** | p95 > 500ms | Check embedding model, scale workers |
| **Retrieval Quality Drop** | Precision@5 < 70% | Re-evaluate embedding model, check data quality |
| **Index Staleness** | Last update > 48 hours | Trigger re-indexing pipeline |
| **Memory Critical** | Usage > 90% | Scale vector store, optimize indexes |
| **Embedding Failures** | > 5% of batch fails | Check input data quality, model availability |

---

## 8. Security & Compliance

### 8.1 Security Requirements

| Requirement | Implementation |
|-------------|----------------|
| **Encryption at Rest** | AES-256 for vector storage |
| **Encryption in Transit** | TLS 1.2+ for all connections |
| **Access Control** | RBAC with least-privilege |
| **Audit Logging** | All queries, updates, deletions logged |
| **Data Classification** | Vectors classified by data sensitivity |
| **PII Handling** | No PII in raw vectors; PII metadata encrypted |
| **Backup & Recovery** | Daily backups with 30-day retention |
| **Network Security** | Private endpoints, VPC peering, firewall rules |

---

## Metadata

```json
{
  "document_id": "vector_store_standards",
  "category": "vectors",
  "subcategory": "vector_standards",
  "source_type": "Compiled_Technical_Standards",
  "authority": "Pinecone/Weaviate/Qdrant/ChromaDB/pgvector/FAISS/Milvus",
  "version": "2026.1",
  "format": "Markdown",
  "retrieved": "2026-07-28",
  "confidence": 0.93,
  "tags": ["Vector_Database", "Embeddings", "Semantic_Search", "Pinecone", "Weaviate", "Qdrant", "ChromaDB", "pgvector", "Milvus", "FAISS", "Chunking", "Hybrid_Search", "RAG", "AI_Search", "Vector_Storage"]
}
```