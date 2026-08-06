# 📘 AI Study Guide & Mentor

An AI-powered personalized learning roadmap and mentoring application built using **LangChain**, **Google Gemini**, **Pydantic**, and **Streamlit**.

The application generates customized learning plans, provides an AI mentor for doubt solving, recommends projects and resources, and helps learners build a structured roadmap for mastering any technology or skill.

---

## 🚀 Live Demo

👉 **Hugging Face Space**

---

# ✨ Features

## 📚 Personalized Learning Roadmaps

Generate structured learning paths for any skill based on:

- Skill / Domain
- Current Level
- Learning Goal
- Learning Style

Supported skills include:

- Python
- SQL
- Data Science
- Machine Learning
- Deep Learning
- Generative AI
- LangChain
- Power BI
- DevOps
- Cyber Security
- NLP
- Salesforce
- Cloud Computing
- And many more...

---

## 🛣️ Structured Learning Phases

Creates step-by-step learning phases including:

- Beginner
- Intermediate
- Advanced
- Industry Tools
- Real-world Projects

Each phase contains:

- Phase Title
- Topics to Learn
- Expected Outcome

---

## 🧠 AI Mentor

Integrated AI Mentor to answer learning-related questions.

Examples:

- Explain Machine Learning
- What is Overfitting?
- Difference between CNN and RNN
- Python File Handling
- Statistics Basics
- SQL Queries

The mentor provides:

- Beginner-friendly explanations
- Code examples
- Real-world analogies
- Interview tips

---

## 📖 Recommended Resources

Suggests high-quality learning resources including:

- Documentation
- Online Courses
- Books
- Blogs
- Practice Websites

---

## 🎥 YouTube Recommendations

Recommends popular YouTube channels and playlists relevant to the selected technology.

---

## 💻 Project Recommendations

Generates beginner to advanced project ideas based on:

- Current Level
- Learning Goal
- Learning Style

---

## 📊 Learning Dashboard

Displays:

- Total Roadmaps Generated
- AI Mentor Questions Asked
- Last Response Time

---

## ✅ Structured Output Parsing

Uses **Pydantic** models to generate reliable structured responses from Gemini.

---

## 🎨 Modern Streamlit Interface

Features include:

- Responsive Layout
- Sidebar Learner Profile
- Dashboard Statistics
- Interactive Tabs
- Clean User Interface

---

# 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python
- LangChain
- Google Gemini API

### AI & LLM

- Google Gemini Flash

### Validation

- Pydantic

### Monitoring

- Langfuse

### Environment

- Python Dotenv

---

# 📂 Project Structure

```
AI-Study-Guide-Mentor/
│
├── app.py                 # Streamlit UI
├── chain.py               # LangChain Roadmap Generator
├── mentor.py              # AI Mentor
├── prompt.py              # Prompt Templates
├── parser.py              # Pydantic Output Parser
├── models.py              # Input Models
├── langfuse_config.py     # Langfuse configuration
├── requirements.txt
├── .env
│
├── .streamlit/
│   └── config.toml
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI-Study-Guide-Mentor.git
```

Move into the project folder

```bash
cd AI-Study-Guide-Mentor
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

LANGFUSE_PUBLIC_KEY=YOUR_PUBLIC_KEY

LANGFUSE_SECRET_KEY=YOUR_SECRET_KEY

LANGFUSE_HOST=https://cloud.langfuse.com
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📱 Application Workflow

1. Select your current learning level.
2. Choose your learning goal.
3. Select your preferred learning style.
4. Enter the skill or technology.
5. Click **Generate Roadmap**.
6. Explore:
   - Key Topics
   - Learning Phases
   - Resources
   - YouTube Channels
   - Projects
7. Ask questions to the AI Mentor for personalized guidance.

---

# 📸 Screenshots

Add screenshots of:

<img width="1912" height="915" alt="Screenshot 2026-08-06 121119" src="https://github.com/user-attachments/assets/307da173-af0a-406d-9895-db963fa8c4d4" />
<img width="1910" height="896" alt="Screenshot 2026-08-06 121227" src="https://github.com/user-attachments/assets/e65f6f21-1a90-4ffd-ba4a-233dec42b164" />
<img width="1915" height="912" alt="Screenshot 2026-08-06 121302" src="https://github.com/user-attachments/assets/2b027f4f-638c-41c4-a2fa-59361c845288" />
<img width="1913" height="877" alt="Screenshot 2026-08-06 121400" src="https://github.com/user-attachments/assets/ab8f1006-7e8d-4c2a-a20a-bb7c16e90f1a" />
<img width="1917" height="911" alt="Screenshot 2026-08-06 121434" src="https://github.com/user-attachments/assets/01e0e328-ea06-4bfa-9cfc-deb1a9743277" />
<img width="1886" height="912" alt="Screenshot 2026-08-06 121551" src="https://github.com/user-attachments/assets/f97aaafb-94f4-4852-a84f-c48a80b51165" />

# 🎯 Example Skills

- Python
- SQL
- Machine Learning
- Deep Learning
- Data Science
- Generative AI
- LangChain
- Power BI
- Tableau
- NLP
- DevOps
- AWS
- Azure
- Docker
- Kubernetes

---

# 🚀 Future Enhancements

- User Authentication
- Learning Progress Tracking
- Weekly Study Planner
- Interactive Coding Challenges
- Flashcards
- Quiz Generator
- PDF Roadmap Export
- Voice-based AI Mentor
- Multi-language Support
- Learning History
- Resume Skill Mapping

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 👩‍💻 Author

**Swathi Gounikadi**

AI & Machine Learning Enthusiast

- Python
- Machine Learning
- Deep Learning
- Generative AI
- LangChain
- Streamlit
- Google Gemini

---

⭐ If you found this project useful, don't forget to **Star** the repository!
