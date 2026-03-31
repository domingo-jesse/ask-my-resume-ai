import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Get to Know Jesse", page_icon="👋", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 55%, #ffffff 100%);
    }
    .hero {
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 1.4rem;
        background: rgba(255,255,255,0.88);
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
        margin-bottom: 1rem;
    }
    .card {
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        background: #ffffff;
        padding: 1rem;
        height: 100%;
    }
    .chip {
        display: inline-block;
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        color: #3730a3;
        font-size: 0.85rem;
        padding: 0.3rem 0.6rem;
        border-radius: 999px;
        margin: 0.1rem 0.35rem 0.3rem 0;
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
Technical Program Manager | Technical Operations | Support Engineering

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
Jesse is interested in roles that combine technical problem-solving, operations, support engineering, AI workflow automation, and cross-functional coordination.

RULES:
- Only answer using this context
- Do not invent facts
- If something is not supported by the context, say so clearly
"""

st.markdown(
    """
    <div class="hero">
        <h1 style="margin:0;">Get to Know Jesse</h1>
        <p style="margin:0.5rem 0 0 0;color:#334155;">
            Welcome! This is a conversational profile assistant that helps you quickly explore Jesse Domingo's
            experience, strengths, and career direction in a clear, professional way.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
        <div class="card">
            <h4 style="margin-top:0;">What you can ask</h4>
            <p style="color:#475569;">Background, leadership, technical strengths, or role fit.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="card">
            <h4 style="margin-top:0;">Response style</h4>
            <p style="color:#475569;">Choose interview prep, role fit analysis, or general Q&A.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="card">
            <h4 style="margin-top:0;">Profile focus</h4>
            <p style="color:#475569;">Technical operations, support engineering, and cross-team execution.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

mode = st.radio(
    "Conversation mode",
    ["General Q&A", "Interview Mode", "Role Fit"],
    horizontal=True,
)

if mode == "Interview Mode":
    behavior = """
Act like a hiring manager interviewing Jesse.
Answer the question, then include 1 thoughtful follow-up question when useful.
"""
elif mode == "Role Fit":
    behavior = """
Evaluate Jesse's fit for roles based on the context.
Be specific about strengths, likely fit, and any gaps.
"""
else:
    behavior = """
Answer clearly and professionally based on the context.
"""

st.markdown("**Quick prompts**")
st.markdown(
    """
    <span class="chip">Support engineering impact</span>
    <span class="chip">Healthcare SaaS experience</span>
    <span class="chip">Technical strengths</span>
    <span class="chip">Best-fit roles</span>
    <span class="chip">Interview prep</span>
    """,
    unsafe_allow_html=True,
)

suggested_questions = [
    "What experience does Jesse have in production incident response?",
    "What roles is Jesse best suited for right now?",
    "What are Jesse's strongest technical skills?",
    "What interview questions would be most useful to ask Jesse?",
]

suggest_cols = st.columns(2)
for idx, prompt_text in enumerate(suggested_questions):
    with suggest_cols[idx % 2]:
        if st.button(prompt_text, key=f"prompt_{idx}"):
            st.session_state["question_input"] = prompt_text

question = st.text_input(
    "Ask about Jesse's profile",
    value=st.session_state.get("question_input", ""),
    placeholder="Example: How does Jesse partner with engineering during incidents?",
)

if st.button("Get insight", type="primary"):
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
            with st.spinner("Putting together a thoughtful response..."):
                response = client.responses.create(model="gpt-5.4-mini", input=prompt)

            st.subheader("Profile insight")
            st.write(response.output_text)

        except Exception as e:
            st.error(f"Error: {e}")
