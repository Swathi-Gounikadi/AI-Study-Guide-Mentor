import streamlit as st
import time
from models import UserInput
from chain import generate_learning_path
from mentor import ask_mentor
import traceback
# =========================
# PAGE CONFIG
# =========================
import streamlit as st

st.set_page_config(
    page_title="AI Study Guide & Mentor",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background-color:#ffffff;
}

/* Main Title */
.main-title{
    text-align:center;
    font-size:65px;
    font-weight:900;
    color:#DC2626;
    font-family:'Segoe UI',sans-serif;
    margin-bottom:5px;
}

/* Subtitle */
.sub-title{
    text-align:center;
    font-size:28px;
    color:#555555;
    font-weight:500;
    margin-bottom:35px;
}

/* Button */
.stButton>button{
    background:#DC2626 !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    font-size:18px !important;
    font-weight:bold !important;
}

.stButton>button:hover{
    background:#B91C1C !important;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#FFF5F5;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
🚀 AI Study Guide & Mentor
</div>

<div class="sub-title">
Personalized Roadmaps • AI Mentor • Projects • Resources
</div>
""", unsafe_allow_html=True)
# =========================
# SESSION STATE
# =========================

if "roadmap_count" not in st.session_state:
    st.session_state.roadmap_count = 0

if "mentor_count" not in st.session_state:
    st.session_state.mentor_count = 0

if "last_response_time" not in st.session_state:
    st.session_state.last_response_time = 0

if "response" not in st.session_state:
    st.session_state.response = None

if "mentor_response" not in st.session_state:
    st.session_state.mentor_response = ""


# =========================
# SIDEBAR
# =========================

st.sidebar.header("📘 Learner Profile")

level = st.sidebar.selectbox("Current Level",
    ["Beginner", "Intermediate", "Advanced"])

goal_option = st.sidebar.selectbox("Learning Goal",
    [
        "Get Started", "Build Projects", "Crack Interviews",
        "Become Job Ready", "Become Data Analyst", "Become Data Scientist",
        "Become ML Engineer", "Become AI Engineer", "Master the Skill", "Custom"
    ]
)

if goal_option == "Custom":
    goal = st.sidebar.text_input("Enter Custom Goal")
else:
    goal = goal_option

style = st.sidebar.radio("Learning Style", ["Theory Based", "Project Based"])

st.sidebar.divider()
if st.sidebar.button("🔄 Reset Learning Session"):
    st.session_state.response = None
    st.session_state.mentor_response = ""
    st.sidebar.success("Chat history cleared!")

# =========================
# MAIN LAYOUT
# =========================

main_col, dash_col = st.columns([3, 1], gap="large")

with main_col:
    skill = st.text_input("Enter Skill",
        placeholder="e.g. Data Science , GenAI, Python, SQL..."
    )
    generate_clicked = st.button("🚀 Generate Roadmap")

with dash_col:
    st.markdown(f"""
    <div class="dash-title">📊 Monitoring Dashboard</div>
    <div class="stat-panel">
      <div class="stat-label">📚 Roadmaps Generated</div>
      <div class="stat-value">{st.session_state.roadmap_count}</div>
    </div>
    <div class="stat-panel">
      <div class="stat-label">💬 Mentor Questions</div>
      <div class="stat-value">{st.session_state.mentor_count}</div>
    </div>
    <div class="stat-panel">
      <div class="stat-label">⚡ Last Response Time</div>
      <div class="stat-value">{st.session_state.last_response_time}s</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# GENERATE ROADMAP
# =========================
if generate_clicked:

    try:
        user_input = UserInput(
            skill=skill,
            level=level,
            goal=goal,
            style=style
        )

        with st.spinner("Generating your personalised roadmap..."):
            start_time = time.time()
            response = generate_learning_path(user_input)
            st.session_state.response = response
            st.session_state.roadmap_count += 1
            end_time = time.time()
            st.session_state.last_response_time = round(end_time - start_time, 2)

    except Exception as e:
        st.error(str(e))
        st.code(traceback.format_exc())

if "response" in st.session_state and st.session_state.response is not None:
    response = st.session_state.response

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["🧠 Topics", "📚 Roadmap", "🎥 Resources", "💻 Projects", "🤖 AI Mentor"]
        )

    # ---- TOPICS TAB ----
    with tab1:
        st.subheader("🧠 Key Topics")
        for topic in response.key_topics:
            st.info(topic)

    # ---- ROADMAP TAB ----
    with tab2:
        st.subheader("📅 Learning Phases")
        for phase in response.learning_phases:
            st.markdown(f"### {phase.title}")
            st.write("📚 Topics To Cover:")

            for topic in phase.topics:
                st.write(f"• {topic}")
            st.success(f"🎯 Outcome: {phase.outcome}")
            st.divider()
        st.subheader("📝 Summary")
        st.write(response.learning_goal_summary)
    
    
    # ---- RESOURCES TAB ----
    with tab3:
        st.subheader("📖 Recommended Resources")
        for resource in response.recommended_resources:
            st.write(f"🔗 {resource}")

        st.subheader("🎥 Best YouTube Channels")
        for channel in response.youtube_channels:
            st.write(f"📺 {channel}")

    # ---- PROJECTS TAB ----
    with tab4:
        st.subheader("💻 Recommended Projects")
        for project in response.recommended_projects:
            st.write(f"🚀 {project}")

    # ---- AI MENTOR TAB ----
    with tab5:
        st.subheader("🤖 Ask AI Mentor")
        st.write("Have a doubt? Ask anything below.")
        mentor_question = st.text_input("Your Question",
            placeholder="e.g. What's the difference between supervised and unsupervised learning?",
            key="mentor_question")

        if st.button("💬 Ask Mentor", key="mentor_button"):
            if mentor_question.strip():
                st.session_state.mentor_count += 1

                with st.spinner("Mentor is thinking..."):
                    answer = ask_mentor(mentor_question)

                # Ensure only plain text is displayed
                if isinstance(answer, list):
                    text = ""
                    for item in answer:
                        if isinstance(item, dict):
                            text += item.get("text", "")
                        else:
                            text += str(item)
                    answer = text

                st.session_state.mentor_response = answer

            else:
                st.warning("Please type a question first.")

        if st.session_state.mentor_response:
            st.success("AI Mentor Response")
            st.markdown(st.session_state.mentor_response)