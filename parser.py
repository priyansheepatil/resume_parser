import re
import spacy

nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()



def extract_email(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(email_pattern, text)
    return match.group(0) if match else None



def extract_phone(text):
    phone_pattern = r"\+?\d[\d -]{8,}\d"
    match = re.search(phone_pattern, text)
    return match.group(0) if match else None



def extract_name(text):
    
    name_pattern = r"Name\s*[:\-]\s*([A-Za-z\s]+)"
    match = re.search(name_pattern, text, re.IGNORECASE)
    if match:
        name = match.group(1).strip()

        
        end_words = ["contact", "email", "linkedin", "github"]
        parts = name.split()
        clean_parts = []

        for p in parts:
            if p.lower() in end_words:
                break
            clean_parts.append(p)

        return " ".join(clean_parts)

    
    header_pattern = r"([A-Za-z]{2,}\s[A-Za-z]{2,}(?:\s[A-Za-z]{2,})?)\s*Contact"
    match = re.search(header_pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            
            if "cloud" not in ent.text.lower() and "computing" not in ent.text.lower():
                return ent.text.strip()

    return None



def extract_skills(text):
    skills = [
        "python", "java", "c++", "sql", "html", "css", "javascript",
        "machine learning", "data analysis", "excel", "communication",
        "tensorflow", "django", "react", "git",
    ]

    found = []
    text_lower = text.lower()

    for skill in skills:
        if skill.lower() in text_lower:
            found.append(skill.capitalize())

    return list(set(found))



def parse_resume(text):
    text = clean_text(text)

    data = {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text),
    }

    return data
