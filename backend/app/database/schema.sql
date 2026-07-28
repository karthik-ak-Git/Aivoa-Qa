-- PharmaQMS AI Copilot — Supabase Database Schema
-- Run this in: Supabase Dashboard > SQL Editor

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================
-- 1. USERS
-- ============================================
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'analyst',
    department VARCHAR(100),
    is_active BOOLEAN NOT NULL DEFAULT true,
    avatar_url TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- ============================================
-- 2. COMPLAINTS
-- ============================================
CREATE TYPE complaint_status AS ENUM ('open','under_review','investigation','capa_required','resolved','closed','rejected');
CREATE TYPE complaint_priority AS ENUM ('low','medium','high','critical');
CREATE TYPE complaint_source AS ENUM ('phone','email','web','regulatory','internal','distributor','patient');

CREATE TABLE IF NOT EXISTS complaints (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    complaint_number VARCHAR(50) UNIQUE NOT NULL,
    title VARCHAR(500) NOT NULL,
    description TEXT NOT NULL,

    status complaint_status NOT NULL DEFAULT 'open',
    priority complaint_priority NOT NULL DEFAULT 'medium',
    source complaint_source NOT NULL DEFAULT 'web',
    category VARCHAR(100),
    subcategory VARCHAR(100),

    product_name VARCHAR(255),
    product_code VARCHAR(50),
    batch_number VARCHAR(50),
    manufacture_date VARCHAR(20),
    expiry_date VARCHAR(20),

    reporter_name VARCHAR(255),
    reporter_email VARCHAR(255),
    reporter_phone VARCHAR(50),
    reporter_type VARCHAR(50),

    ai_category VARCHAR(100),
    ai_confidence DOUBLE PRECISION,
    ai_suggested_root_cause TEXT,
    ai_suggested_capa TEXT,

    root_cause TEXT,
    corrective_action TEXT,
    preventive_action TEXT,
    resolution_notes TEXT,
    resolved_at TIMESTAMPTZ,

    attachments JSONB,
    tags JSONB,
    metadata JSONB,

    assignee_id UUID REFERENCES users(id) ON DELETE SET NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_complaints_number ON complaints(complaint_number);
CREATE INDEX IF NOT EXISTS idx_complaints_status ON complaints(status);
CREATE INDEX IF NOT EXISTS idx_complaints_category ON complaints(category);
CREATE INDEX IF NOT EXISTS idx_complaints_product ON complaints(product_name);
CREATE INDEX IF NOT EXISTS idx_complaints_assignee ON complaints(assignee_id);

-- ============================================
-- 3. INVESTIGATIONS
-- ============================================
CREATE TABLE IF NOT EXISTS investigations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    investigation_number VARCHAR(50) UNIQUE NOT NULL,
    title VARCHAR(500) NOT NULL,
    description TEXT,

    root_cause_category VARCHAR(100),
    root_cause_description TEXT,
    methodology VARCHAR(100),
    evidence JSONB,
    findings TEXT,

    man_method TEXT,
    machine_method TEXT,
    material_method TEXT,
    measurement_method TEXT,
    mother_nature_method TEXT,
    management_method TEXT,

    ai_root_cause_suggestion TEXT,
    ai_confidence DOUBLE PRECISION,

    status VARCHAR(50) DEFAULT 'open',
    completed_at TIMESTAMPTZ,

    complaint_id UUID NOT NULL REFERENCES complaints(id) ON DELETE CASCADE,
    investigator_id UUID REFERENCES users(id) ON DELETE SET NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_investigations_number ON investigations(investigation_number);
CREATE INDEX IF NOT EXISTS idx_investigations_complaint ON investigations(complaint_id);

-- ============================================
-- 4. CAPAs
-- ============================================
CREATE TYPE capa_type AS ENUM ('corrective','preventive','both');
CREATE TYPE capa_status AS ENUM ('open','in_progress','completed','effectiveness_check','closed','overdue');

CREATE TABLE IF NOT EXISTS capas (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    capa_number VARCHAR(50) UNIQUE NOT NULL,
    title VARCHAR(500) NOT NULL,
    description TEXT,

    capa_type capa_type NOT NULL DEFAULT 'corrective',
    status capa_status NOT NULL DEFAULT 'open',

    corrective_action TEXT,
    preventive_action TEXT,
    action_owner VARCHAR(255),
    target_date TIMESTAMPTZ,
    completed_date TIMESTAMPTZ,

    effectiveness_criteria TEXT,
    effectiveness_result TEXT,
    effectiveness_date TIMESTAMPTZ,
    is_effective BOOLEAN,

    ai_suggested_actions JSONB,
    ai_confidence DOUBLE PRECISION,

    evidence JSONB,
    attachments JSONB,

    complaint_id UUID NOT NULL REFERENCES complaints(id) ON DELETE CASCADE,
    investigation_id UUID REFERENCES investigations(id) ON DELETE SET NULL,
    created_by_id UUID REFERENCES users(id) ON DELETE SET NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_capas_number ON capas(capa_number);
CREATE INDEX IF NOT EXISTS idx_capas_complaint ON capas(complaint_id);
CREATE INDEX IF NOT EXISTS idx_capas_status ON capas(status);

-- ============================================
-- 5. KNOWLEDGE DOCUMENTS
-- ============================================
CREATE TABLE IF NOT EXISTS knowledge_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(500) NOT NULL,
    content TEXT NOT NULL,
    domain VARCHAR(100) NOT NULL,
    source VARCHAR(500) NOT NULL,
    source_url TEXT,

    chunk_index INTEGER NOT NULL DEFAULT 0,
    total_chunks INTEGER NOT NULL DEFAULT 1,
    chunk_size INTEGER NOT NULL DEFAULT 512,

    tags JSONB,
    metadata JSONB,
    language VARCHAR(10) NOT NULL DEFAULT 'en',
    is_active BOOLEAN NOT NULL DEFAULT true,

    embedding_id VARCHAR(100),

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_knowledge_domain ON knowledge_documents(domain);
CREATE INDEX IF NOT EXISTS idx_knowledge_embedding ON knowledge_documents(embedding_id);

-- ============================================
-- 6. CONVERSATIONS
-- ============================================
CREATE TABLE IF NOT EXISTS conversations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    conversation_id VARCHAR(50) UNIQUE NOT NULL,
    title VARCHAR(500),
    status VARCHAR(50) DEFAULT 'active',

    complaint_id UUID REFERENCES complaints(id) ON DELETE SET NULL,
    agent_used VARCHAR(100),
    metadata JSONB,

    user_id UUID REFERENCES users(id) ON DELETE SET NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_conversations_id ON conversations(conversation_id);

-- ============================================
-- 7. CHAT MESSAGES
-- ============================================
CREATE TABLE IF NOT EXISTS chat_messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    role VARCHAR(20) NOT NULL,
    content TEXT NOT NULL,

    agent_used VARCHAR(100),
    citations JSONB,
    confidence DOUBLE PRECISION,
    intent VARCHAR(100),

    tokens_used INTEGER,
    processing_time_ms DOUBLE PRECISION,
    metadata JSONB,

    conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_chat_messages_conv ON chat_messages(conversation_id);

-- ============================================
-- 8. AUDIT LOGS
-- ============================================
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(100) NOT NULL,
    entity_id VARCHAR(36),

    description TEXT,
    old_value JSONB,
    new_value JSONB,
    ip_address VARCHAR(50),
    user_agent TEXT,

    user_id UUID REFERENCES users(id) ON DELETE SET NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_audit_action ON audit_logs(action);
CREATE INDEX IF NOT EXISTS idx_audit_entity ON audit_logs(entity_type, entity_id);

-- ============================================
-- 9. AUTO-UPDATE TRIGGER
-- ============================================
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DO $$
DECLARE
    t TEXT;
BEGIN
    FOR t IN
        SELECT unnest(ARRAY[
            'users','complaints','investigations','capas',
            'knowledge_documents','conversations','chat_messages','audit_logs'
        ])
    LOOP
        EXECUTE format(
            'CREATE TRIGGER trigger_updated_at BEFORE UPDATE ON %I
             FOR EACH ROW EXECUTE FUNCTION update_updated_at()',
            t
        );
    END LOOP;
END;
$$;

-- ============================================
-- 10. ROW LEVEL SECURITY (RLS)
-- ============================================
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE complaints ENABLE ROW LEVEL SECURITY;
ALTER TABLE investigations ENABLE ROW LEVEL SECURITY;
ALTER TABLE capas ENABLE ROW LEVEL SECURITY;
ALTER TABLE knowledge_documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;
ALTER TABLE chat_messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE audit_logs ENABLE ROW LEVEL SECURITY;

-- Allow service role full access
CREATE POLICY "Service role full access" ON users FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Service role full access" ON complaints FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Service role full access" ON investigations FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Service role full access" ON capas FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Service role full access" ON knowledge_documents FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Service role full access" ON conversations FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Service role full access" ON chat_messages FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Service role full access" ON audit_logs FOR ALL USING (true) WITH CHECK (true);

-- Allow anon read access to knowledge_documents
CREATE POLICY "Anon read knowledge" ON knowledge_documents FOR SELECT USING (is_active = true);

-- ============================================
-- 11. KNOWLEDGE SOURCES (summary per source file)
-- ============================================
CREATE TABLE IF NOT EXISTS knowledge_sources (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source VARCHAR(500) UNIQUE NOT NULL,
    doc_count INTEGER NOT NULL DEFAULT 0,
    domains JSONB DEFAULT '[]',
    last_synced_at TIMESTAMPTZ DEFAULT now(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_knowledge_sources_name ON knowledge_sources(source);
ALTER TABLE knowledge_sources ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Service role full access" ON knowledge_sources FOR ALL USING (true) WITH CHECK (true);

-- ============================================
-- 12. UPSERT RPC FUNCTION
-- ============================================
CREATE OR REPLACE FUNCTION upsert_knowledge_source(
    p_source TEXT,
    p_doc_count INTEGER
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO knowledge_sources (source, doc_count, last_synced_at)
    VALUES (p_source, p_doc_count, now())
    ON CONFLICT (source)
    DO UPDATE SET
        doc_count = EXCLUDED.doc_count,
        last_synced_at = now(),
        updated_at = now();
END;
$$ LANGUAGE plpgsql;

-- Done!
SELECT 'PharmaQMS schema created successfully!' as result;
