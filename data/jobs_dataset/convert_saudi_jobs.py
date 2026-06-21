"""
Converts the raw Saudi jobs CSV string → saudi_jobs_full.json
Run once: python data/jobs_dataset/convert_saudi_jobs.py
"""
import json, csv, io, sys, os

CSV_PATH = os.path.join(os.path.dirname(__file__), "saudi_jobs_raw.csv")
OUT_PATH  = os.path.join(os.path.dirname(__file__), "saudi_jobs_full.json")

if not os.path.exists(CSV_PATH):
    print(f"Place the raw CSV at: {CSV_PATH}")
    sys.exit(1)

with open(CSV_PATH, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    jobs = []
    for row in reader:
        skills = [s.strip() for s in row["qualifications"].split(",") if s.strip()]
        jobs.append({
            "job_id":          row["job_id"],
            "title":           row["job_title"],
            "company":         row["company_name"],
            "location":        row["location"],
            "description":     row["description_text"],
            "required_skills": skills,
            "preferred_skills": [],
            "experience_years": row.get("experience_years", ""),
            "salary_range":    row.get("salary_formatted", ""),
            "job_type":        row.get("job_type", "Full-time"),
            "industry":        row.get("industry", ""),
            "apply_link":      row.get("apply_link", ""),
        })

with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

print(f"✅ Converted {len(jobs)} jobs → {OUT_PATH}")
