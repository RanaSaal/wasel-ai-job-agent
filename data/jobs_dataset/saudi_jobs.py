"""
Convert the Saudi jobs CSV (from document) to the Qdrant-ready JSON format Wasel expects.
Run: python data/jobs_dataset/saudi_jobs.py
"""
import json, csv, io

RAW_CSV = """job_id,job_title,company_name,location,description_text,qualifications,experience_years,salary_formatted,job_type,industry,apply_link
1,Software Engineer,Saudi Aramco,Dhahran,Design and develop scalable backend services for oil & gas digital platforms. Work with distributed systems and cloud infrastructure.,"Python, Java, SQL, REST APIs, Docker, AWS",3-5,15000-22000 SAR,Full-time,Energy,https://careers.aramco.com/job/1
2,Data Scientist,stc,Riyadh,Build ML models to analyze customer behavior and improve telecom services. Collaborate with product and engineering teams.,"Python, Machine Learning, TensorFlow, SQL, Statistics, Pandas",2-4,14000-20000 SAR,Full-time,Telecom,https://careers.stc.com.sa/job/2
3,Frontend Developer,Noon,Riyadh,Develop responsive e-commerce UI components. Maintain and improve customer-facing web application performance.,"React, TypeScript, CSS, HTML, Git, Redux",2-4,12000-18000 SAR,Full-time,E-commerce,https://careers.noon.com/job/3
4,DevOps Engineer,STC Solutions,Riyadh,"Manage CI/CD pipelines, containerized workloads, and cloud infrastructure for enterprise clients.","Kubernetes, Docker, Jenkins, AWS, Terraform, Linux",3-5,16000-24000 SAR,Full-time,IT Services,https://careers.stcsolutions.com.sa/job/4"""

# Parse and print count
reader = csv.DictReader(io.StringIO(RAW_CSV))
jobs = []
for row in reader:
    skills = [s.strip() for s in row['qualifications'].split(',') if s.strip()]
    jobs.append({
        "job_id": row['job_id'],
        "title": row['job_title'],
        "company": row['company_name'],
        "location": row['location'],
        "description": row['description_text'],
        "required_skills": skills,
        "preferred_skills": [],
        "experience_years": row['experience_years'],
        "salary_range": row['salary_formatted'],
        "job_type": row['job_type'],
        "industry": row['industry'],
        "apply_link": row['apply_link'],
    })
print(json.dumps(jobs[:2], indent=2))
