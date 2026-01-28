# PRD: Javis Research-Engine (Perplexity for AI Engineers)

## 1. Product Vision
To provide AI Engineers with a search-focused interface that doesn't just "talk," but crawls, cites, and synthesizes technical documentation and research papers into actionable insights.

## 2. Core Features (MVP)
1.  **Technical Search**: Deep crawling of ArXiv (PDF extraction), GitHub (code analysis), and technical blogs.
2.  **Citation-First UI**: Every technical claim must link back to a specific source or paper section.
3.  **Local Context Integration**: The ability to search through local experimental logs and prior research notes.
4.  **Optimized Inference**: Integration of the Speculative Decoding (EAGLE-2) logic we just built for low-latency responses.

## 3. Tech Stack
- **Frontend**: Next.js (shadcn/ui) for a clean, Perplexity-like interface.
- **Backend / Search**: Tavily API or Brave Search + Custom ArXiv Scraper.
- **LLM Engine**: vLLM (running Qwen-2.5 14B or Llama-3 8B) with Speculative Decoding.
- **Database**: LanceDB or Chroma (Vector search for paper embeddings).

---

# Execution Plan (Phase 1-3)

## Phase 1: Scaffolding (Current)
- [ ] Initialize the Next.js frontend and FastAPI backend.
- [ ] Set up the basic search tool for the LLM.

## Phase 2: PDF & Code Intelligence
- [ ] Implement an ArXiv PDF parser to extract equations and tables.
- [ ] Implement a GitHub repo "deep-read" to analyze implementation details.

## Phase 3: The "Javis" Integration
- [ ] Connect the inference engine we built (`run_inference.py`) to the backend.
- [ ] Deploy the UI for local/team testing.
