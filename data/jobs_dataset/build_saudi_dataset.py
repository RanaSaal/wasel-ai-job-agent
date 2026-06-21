"""
Wasel — Saudi Jobs Dataset Builder
Parses the full 500-job Saudi CSV and writes saudi_jobs_full.json
Run: python data/jobs_dataset/build_saudi_dataset.py
"""
import json, csv, io, os

# ── Paste the raw CSV here (the full 500-row file) ───────────
# OR place the file at: data/jobs_dataset/saudi_jobs_raw.csv
# and the script will read from disk.

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH   = os.path.join(SCRIPT_DIR, "saudi_jobs_raw.csv")
OUT_PATH   = os.path.join(SCRIPT_DIR, "saudi_jobs_full.json")


def parse_jobs(csv_text: str) -> list:
    reader = csv.DictReader(io.StringIO(csv_text))
    jobs = []
    for row in reader:
        skills = [s.strip() for s in row.get("qualifications", "").split(",") if s.strip()]
        jobs.append({
            "job_id":          row.get("job_id", ""),
            "title":           row.get("job_title", ""),
            "company":         row.get("company_name", ""),
            "location":        row.get("location", ""),
            "description":     row.get("description_text", ""),
            "required_skills": skills,
            "preferred_skills": [],
            "experience_years": row.get("experience_years", ""),
            "salary_range":    row.get("salary_formatted", ""),
            "job_type":        row.get("job_type", "Full-time"),
            "industry":        row.get("industry", ""),
            "apply_link":      row.get("apply_link", ""),
        })
    return jobs


def main():
    if not os.path.exists(CSV_PATH):
        print(f"❌  CSV not found at: {CSV_PATH}")
        print("    Save your 500-row CSV there and rerun.")
        return

    with open(CSV_PATH, encoding="utf-8") as f:
        text = f.read()

    jobs = parse_jobs(text)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)

    print(f"✅  {len(jobs)} jobs written to {OUT_PATH}")


if __name__ == "__main__":
    main()
