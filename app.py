import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Jesse Domingo | Interactive Resume", page_icon="🧭", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 52%, #ffffff 100%);
    }
    .main .block-container {
        max-width: 960px;
        padding-top: 1.5rem;
        padding-bottom: 2.25rem;
    }
    .hero {
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 1.35rem 1.45rem;
        background: rgba(255,255,255,0.92);
        box-shadow: 0 14px 35px rgba(15, 23, 42, 0.07);
        margin-bottom: 0.95rem;
    }
    .section-card {
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        background: #ffffff;
        padding: 1rem 1.05rem;
        margin-bottom: 0.75rem;
        height: 100%;
    }
    .section-title {
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        color: #475569;
        margin-bottom: 0.35rem;
    }
    .section-card p, .section-card li {
        color: #334155;
        line-height: 1.45;
    }
    .list-tight {
        margin: 0.25rem 0 0 1rem;
        padding: 0;
    }
    .prompt-label {
        font-size: 0.95rem;
        color: #334155;
        margin: 0.2rem 0 0.5rem 0;
    }
    .cta-wrap {
        display: flex;
        justify-content: center;
        margin-top: 0.5rem;
    }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #0f766e, #1d4ed8);
        border: 0;
        color: #ffffff;
        border-radius: 10px;
        padding: 0.55rem 1.2rem;
        font-weight: 600;
    }
    div.stButton > button[kind="primary"]:hover {
        filter: brightness(0.96);
    }
    .response-box {
        border: 1px solid #dbeafe;
        background: #f8fbff;
        border-radius: 14px;
        padding: 0.95rem 1rem;
    }
    .empty-state {
        border: 1px dashed #cbd5e1;
        border-radius: 12px;
        color: #64748b;
        background: #f8fafc;
        padding: 0.9rem 1rem;
        margin-top: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=api_key)

profile_context = """
NAME: Jesse Domingo

HEADLINE:
Technical Support Engineer | Technical Program Management | AI Operations

PROFESSIONAL SUMMARY:
Jesse is a technical support and operations professional with experience resolving complex system failures, improving platform reliability, and streamlining workflows through automation and data analysis. He has a strong background in debugging, root cause analysis, healthcare SaaS, cross-functional coordination, and technical communication.

LOCATION:
Washington, United States

CONTACT:
LinkedIn: https://linkedin.com/in/jesse-domingo

CORE STRENGTHS:
- Root cause analysis
- Debugging production issues
- Cross-functional incident coordination
- Support engineering
- Technical communication
- Process improvement
- Healthcare SaaS workflows
- API and SQL-based investigation

TECHNICAL SKILLS:
- SQL
- Python
- APIs / REST
- Postman
- GitHub
- Jira
- Debugging and log analysis
- VB.NET / C++

WORK STYLE:
- Analytical and structured
- Strong at breaking down messy technical problems
- Comfortable working across technical and non-technical teams
- Focused on practical solutions and operational reliability
- Good at translating technical issues into clear stakeholder communication

WORK EXPERIENCE:

Technical Support Engineer
Humata Health (formerly Olive AI)
- Led cross-team incident investigations across engineering, product, and operations
- Resolved complex production issues in healthcare SaaS systems
- Coordinated debugging across APIs, automation pipelines, and databases
- Used SQL, Postman, and logs to diagnose failures
- Implemented process improvements that reduced time to resolution
- Communicated findings to technical and business stakeholders
- Supported incident response during production outages
- Mentored new team members on escalation workflows

Technical Support Analyst
Olive AI
- Managed escalated technical issues in a healthcare automation platform
- Investigated production defects through log analysis, payload validation, and diagnostics
- Partnered with engineering and product teams to reproduce bugs and validate fixes
- Created technical documentation and reports for stakeholders

Software Implementation Consultant
FAST Enterprises
- Worked on a large-scale government system
- Debugged and fixed application logic
- Improved reliability and system behavior

Owner / Founder
The Cryptic Cube
- Built and operated an escape room business
- Designed puzzle systems and customer experiences
- Managed operations, finances, and process improvement

LEADERSHIP AND COACHING:
- Speech and Debate Coach
- Eagle Scout

CURRENT PROJECTS:
- Built an AI-powered web app that answers questions about Jesse’s background
- Interested in AI workflow automation, support tooling, and agent-based systems

CAREER GOALS:
Jesse wants roles in technical support engineering and technical program management, especially where he can work with AI agents, AI operations, workflow automation, and cross-functional technical coordination.

RULES:
- Only answer using this context
- Do not invent facts
- If something is not supported by the context, say so clearly
"""

st.markdown(
    """
    <div class="hero">
        <h1 style="margin:0;">Jesse Domingo | Technical Support, Incident Response, and AI Workflow Builder</h1>
        <p style="margin:0.45rem 0 0 0;color:#334155;">
            Interactive resume for recruiters and hiring managers evaluating Jesse for technical support engineering,
            technical program management, and operations-focused AI roles.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">Why this interactive resume exists</div>
        <p style="margin:0;">
            Most resumes bury real impact in dense bullet points. This profile is designed to help you quickly evaluate
            how Jesse handles production issues, collaborates cross-functionally, and improves reliability in
            healthcare and automation-heavy environments.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left_col, right_col = st.columns(2, gap="small")

with left_col:
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">Core strengths</div>
            <ul class="list-tight">
                <li>Technical support in high-stakes production environments</li>
                <li>Incident response coordination across engineering, product, and operations</li>
                <li>Root cause analysis using SQL, APIs, and logs</li>
                <li>Clear communication with technical and non-technical stakeholders</li>
                <li>Healthcare SaaS systems and workflow reliability</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">Projects (AI + automation)</div>
            <ul class="list-tight">
                <li>Built this AI-driven interactive resume assistant to support recruiter discovery</li>
                <li>Actively exploring AI operations, support tooling, and agent-based workflows</li>
                <li>Focused on practical automation that shortens debugging and escalation cycles</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">Experience highlights</div>
            <ul class="list-tight">
                <li><strong>Humata Health (Olive AI):</strong> Led cross-team investigations and reduced time to resolution during production incidents.</li>
                <li><strong>Olive AI:</strong> Managed escalations, reproduced defects, and partnered with engineering on fixes.</li>
                <li><strong>FAST Enterprises:</strong> Improved behavior and reliability in a large government system implementation.</li>
                <li><strong>The Cryptic Cube:</strong> Ran full business operations with process ownership and customer focus.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">Ways to explore this profile</div>
            <p style="margin:0;">Use the suggested questions below or type your own for a focused, recruiter-ready summary.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

behavior = """
Answer clearly, confidently, and professionally based on the context.
Keep responses concise and structured for recruiters.
When useful, format with short bullets.
"""

st.markdown("#### Suggested questions")
st.markdown('<p class="prompt-label">Recruiter-oriented prompts to quickly evaluate role fit and impact:</p>', unsafe_allow_html=True)

suggested_questions = [
    "What production issues has Jesse solved?",
    "How does Jesse approach incident response?",
    "What are Jesse’s strongest technical and cross-functional skills?",
    "What kinds of roles is Jesse best suited for?",
    "What AI or automation projects has Jesse built?",
    "Why would Jesse be a strong hire?",
]

suggest_cols = st.columns(2, gap="small")
for idx, prompt_text in enumerate(suggested_questions):
    with suggest_cols[idx % 2]:
        if st.button(prompt_text, key=f"prompt_{idx}"):
            st.session_state["question_input"] = prompt_text
            st.session_state["run_insight"] = True

question = st.text_input(
    "Ask a question about Jesse’s background",
    value=st.session_state.get("question_input", ""),
    placeholder="Example: How does Jesse partner with engineering and operations during incidents?",
)

run_from_button = False
with st.container():
    st.markdown('<div class="cta-wrap">', unsafe_allow_html=True)
    run_from_button = st.button("Generate profile insight", type="primary")
    st.markdown("</div>", unsafe_allow_html=True)

should_run = run_from_button or st.session_state.pop("run_insight", False)

if should_run:
    if not question.strip():
        st.warning("Please enter a question to continue.")
    else:
        prompt = f"""
You are an AI assistant representing Jesse Domingo on his personal website.

{behavior}

Use only the profile context below.
Do not make up facts.
If the answer is not supported by the context, say that clearly.

PROFILE CONTEXT:
{profile_context}

QUESTION:
{question}
"""

        try:
            with st.spinner("Building a recruiter-ready answer..."):
                response = client.responses.create(model="gpt-5.4-mini", input=prompt)

            st.subheader("Profile insight")
            st.markdown(f'<div class="response-box">{response.output_text}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.markdown(
        '<div class="empty-state">No response yet. Select a suggested question or write your own to generate a targeted profile insight.</div>',
        unsafe_allow_html=True,
    )
