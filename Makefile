.PHONY: install setup-db build-rag backend frontend dev

# ── Install ──────────────────────────────────────────────────

install:
	@echo "Installing backend..."
	cd backend && pip install -r requirements.txt
	@echo "Installing frontend..."
	cd frontend && npm install
	@echo "✅ All dependencies installed"

# ── Setup ────────────────────────────────────────────────────

setup-db:
	@echo "Setting up Supabase schema..."
	cd backend && python scripts/setup_supabase.py

build-rag:
	@echo "Building Qdrant RAG indices..."
	cd backend && python scripts/build_qdrant_index.py

setup: install setup-db build-rag
	@echo "✅ Wasel setup complete"

# ── Run ──────────────────────────────────────────────────────

backend:
	cd backend && uvicorn app.main:app --reload --port 8000

frontend:
	cd frontend && npm run dev

# Open two terminals and run `make backend` + `make frontend`
# OR use: make dev (requires tmux or parallel)
