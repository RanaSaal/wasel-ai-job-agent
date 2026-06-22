# Wasel AI

An Agentic AI-powered career assistant that helps job seekers analyze their resumes, discover relevant opportunities, identify skill gaps, improve application materials, and receive personalized career guidance.



---

## Overview

Wasel AI combines multiple AI agents working together through a LangGraph orchestration workflow to support users throughout their job search journey.

The platform analyzes resumes, matches users with relevant jobs, identifies missing skills, recommends learning resources, improves CV quality, generates cover letters, and provides an interactive career assistant.

---

## Key Features

### Resume Analysis

* Analyze uploaded resumes.
* Generate structured candidate profiles.
* Extract relevant skills and qualifications.
* Evaluate resume quality and provide improvement suggestions.

### Job Matching

* Match candidates with suitable job opportunities.
* Calculate compatibility scores.
* Highlight strengths and missing requirements.

### Skill Gap Analysis

* Compare candidate profiles with job requirements.
* Identify missing skills and competencies.
* Prioritize areas for improvement.

### Learning Recommendations

* Recommend personalized learning resources.
* Generate career development plans.
* Support continuous skill enhancement.

### Cover Letter Generation

* Generate tailored cover letters.
* Align content with job descriptions and candidate profiles.

### CV Improvement Assistant

* Provide actionable recommendations for resume enhancement.
* Suggest improvements in content, structure, and presentation.

### AI Career Chat Assistant

* Answer career-related questions.
* Provide guidance based on user context and project knowledge.
* Support interactive career planning.

### Retrieval-Augmented Generation (RAG)

* Retrieve contextual information from indexed knowledge sources.
* Improve response accuracy through semantic search using Qdrant.

### Memory Layer

* Maintain conversational context across sessions.
* Store user-related information using Supabase.

---

## System Architecture

```
Frontend (React)
      │
      ▼
FastAPI Backend
      │
      ├── /analyze
      │     │
      │     ├── Upload CV 
      │     │
      │     ▼
      │  LangGraph Orchestrator
      │     │
      │     ├── ResumeAgent
      │     │
      │     ├── JobAgent
      │     │     ├── JD Matching Path
      │     │     └── RAG Job Search Path → Qdrant
      │     │
      │     ├── CoverLetterAgent
      │     └── GapAgent
      │
      │     ▼
      │  Save Analysis → Supabase Database
      │
      ├── /chat
      │     ▼
      │  ChatAgent
      │     ├── Latest Analysis Tool → Supabase Database
      │     └── Learning Resources Tool → Qdrant
      │
      └── /cv-tips
            ▼
       CVImprovementAgent
            ▼
       Supabase Database
```

---

## Tech Stack

### Frontend

* React

### Backend

* FastAPI
* Python

### AI & Agent Framework

* LangChain
* LangGraph
* OpenAI

### Vector Database

* Qdrant Cloud

### Database & Memory (Storage)

* Supabase

---

## Project Structure

```text
wasel/
├── frontend/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── memory/
│   │   ├── rag/
│   │   └── tools/
│   └── main.py
├── data/
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

git clone <repository-url>
cd wasel

### Create Virtual Environment

python -m venv .venv

### Activate Environment

Windows:

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a .env file and configure:

OPENAI_API_KEY=

QDRANT_URL=
QDRANT_API_KEY=

SUPABASE_URL=
SUPABASE_KEY=

---

## Run Backend

cd backend
python -m uvicorn app.main:app --reload --port 8000

API Documentation:

http://localhost:8000/docs

---

## Run Frontend

cd frontend

npm install

npm run dev

Frontend URL:

http://localhost:5173


---


## How It Works

1. The user uploads a resume through the frontend.
2. The FastAPI backend receives the file and request metadata.
3. The LangGraph orchestrator starts the analysis workflow.
4. The Resume Agent extracts a structured candidate profile.
5. The Job Agent either:
    * analyzes a provided job description, or
    * retrieves relevant jobs using semantic search.
6. The Gap Agent identifies missing skills and builds a roadmap.
7. The Cover Letter Agent generates a cover letter when a job description is provided.
8. The final analysis is saved using Supabase.
9. The Chat Agent can later answer follow-up career questions using the saved analysis.
