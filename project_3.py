from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ─── DATASET ───────────────────────────────────────────────
# Each job role has a string of associated skills
# Think of each string as one "document" for TF-IDF

job_roles = {
    "Data Scientist": "python machine learning statistics sql pandas numpy data analysis",
    "Backend Developer": "python flask java sql apis rest git databases",
    "Frontend Developer": "html css javascript react ui ux git responsive design",
    "DevOps Engineer": "aws docker kubernetes linux ci cd git cloud automation",
    "Machine Learning Engineer": "python machine learning deep learning tensorflow pytorch algorithms",
    "Data Analyst": "sql excel python pandas data visualization power bi tableau",
    "Cloud Architect": "aws azure cloud kubernetes docker networking security automation",
    "Full Stack Developer": "html css javascript react python flask sql git apis",
    "Cybersecurity Analyst": "networking security linux ethical hacking firewalls python encryption",
    "AI Engineer": "python machine learning nlp deep learning tensorflow transformers llm"
}

# ─── STEP 1: INGESTION ─────────────────────────────────────
# Take minimum 3 skill inputs from user

print("=== Tech Stack Recommender ===")
print("Enter your top skills (minimum 3):")

skill1 = input("Skill 1: ").strip().lower()
skill2 = input("Skill 2: ").strip().lower()
skill3 = input("Skill 3: ").strip().lower()

# Combine user skills into one string — same format as job role strings
user_profile = skill1 + " " + skill2 + " " + skill3

print(f"\nYour profile: {user_profile}")

# ─── STEP 2: SCORING ───────────────────────────────────────
# Prepare all documents — job roles + user profile together
# TfidfVectorizer needs to see ALL text at once to build a shared vocabulary

role_names = list(job_roles.keys())       # ["Data Scientist", "Backend Developer", ...]
role_descriptions = list(job_roles.values())  # ["python machine learning...", ...]

# Add user profile at the end of the list temporarily for vectorization
all_documents = role_descriptions + [user_profile]

# Fit TF-IDF on all documents — builds the shared vocabulary + weights
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_documents)

# Separate the vectors back out
# All rows except last = job role vectors
# Last row = user profile vector
role_vectors = tfidf_matrix[:-1]       # shape: (10, vocabulary_size)
user_vector = tfidf_matrix[-1]         # shape: (1, vocabulary_size)

# Calculate cosine similarity between user vector and every job role vector
scores = cosine_similarity(user_vector, role_vectors)[0]
# scores is now an array of 10 similarity values, one per job role

# ─── STEP 3: SORTING ───────────────────────────────────────
# Pair each role name with its similarity score
# Then sort by score, highest first

scored_roles = list(zip(role_names, scores))
scored_roles.sort(key=lambda x: x[1], reverse=True)

# ─── STEP 4: FILTERING ─────────────────────────────────────
# Display only the Top 3 most relevant roles

print("\n=== Top 3 Recommended Career Paths ===")
for i, (role, score) in enumerate(scored_roles[:3], start=1):
    print(f"{i}. {role} — Match Score: {round(score * 100, 2)}%")

print("\n=== Full Ranking (All Roles) ===")
for i, (role, score) in enumerate(scored_roles, start=1):
    print(f"{i}. {role} — {round(score * 100, 2)}%")