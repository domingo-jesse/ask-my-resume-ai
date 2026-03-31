import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Jesse Domingo | AI Resume", page_icon="🧭", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: #f6f8fc;
    }
    .main .block-container {
        max-width: 860px;
        padding-top: 2.2rem;
        padding-bottom: 2.8rem;
    }
    .hero {
        border: 1px solid #dde3ee;
        border-radius: 16px;
        padding: 1.4rem;
        background: #ffffff;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
        margin-bottom: 1.4rem;
    }
    .section-card {
        border: 1px solid #dde3ee;
        border-radius: 16px;
        background: #ffffff;
        padding: 1.1rem 1.2rem;
        margin-bottom: 1.15rem;
    }
    .section-title {
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.07em;
        text-transform: uppercase;
        color: #475569;
        margin-bottom: 0.55rem;
    }
    .section-card ul {
        margin: 0;
        padding-left: 1rem;
    }
    .section-card li {
        color: #1f2937;
        line-height: 1.35;
        margin-bottom: 0.4rem;
    }
    .section-card li:last-child {
        margin-bottom: 0;
    }
    .prompt-label {
        color: #475569;
        margin: 0 0 0.6rem 0;
        font-size: 0.95rem;
    }
    div.stButton > button {
        border-radius: 10px;
    }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #0f172a, #1d4ed8);
        border: 0;
        color: #ffffff;
        font-weight: 600;
        padding: 0.55rem 1.2rem;
    }
    .response-box {
        border: 1px solid #dbe4ff;
        background: #f8faff;
        border-radius: 14px;
        padding: 0.95rem 1rem;
    }
    .empty-state {
        border: 1px dashed #cbd5e1;
        border-radius: 12px;
        color: #64748b;
        background: #f8fafc;
        padding: 0.9rem 1rem;
        margin-top: 0.65rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=api_key)

profile_context = """
NAME: Jesse Domingo
TITLE: Technical Support Engineer | AI Workflow Builder
VALUE STATEMENT: I solve production issues fast and build automation that keeps systems stable.

KEY STRENGTHS:
- Debugged production issues using logs, SQL, and APIs
- Led incident response across engineering, product, and operations
- Turned root-cause findings into fixes that reduced repeat outages
- Communicated technical issues clearly to non-technical stakeholders
- Improved support workflows with practical AI and automation

EXPERIENCE HIGHLIGHTS:
- Humata Health (Olive AI): Led cross-team production investigations and reduced time to resolution
- Olive AI: Managed escalations, reproduced defects, and partnered with engineering on fixes
- FAST Enterprises: Debugged government software issues and improved system reliability
- The Cryptic Cube: Ran operations, process design, and customer experience as founder

PROJECTS:
- Built this AI resume assistant so recruiters can evaluate fit in minutes
- Prototyped AI workflows to speed triage, escalation, and issue summaries
- Applied automation ideas to shorten manual support steps

RULES:
- Only answer using this context
- Do not invent facts
- If something is not supported by the context, say so clearly
"""

st.markdown(
    """
    <div class="hero">
        <h1 style="margin:0;">Jesse Domingo</h1>
        <p style="margin:0.35rem 0 0 0;font-size:1.05rem;color:#1f2937;"><strong>Technical Support Engineer | AI Workflow Builder</strong></p>
        <p style="margin:0.5rem 0 0 0;color:#475569;">I solve production issues fast and build automation that keeps systems stable.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">Key strengths</div>
        <ul>
            <li>Debugged production issues using logs, SQL, and APIs.</li>
            <li>Led incident response across engineering, product, and operations.</li>
            <li>Turned root-cause findings into fixes that reduced repeat outages.</li>
            <li>Communicated technical issues clearly to technical and non-technical teams.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">Experience highlights</div>
        <ul>
            <li>Humata Health (Olive AI): Led production investigations and reduced time to resolution.</li>
            <li>Olive AI: Managed escalations, reproduced defects, and validated engineering fixes.</li>
            <li>FAST Enterprises: Debugged application logic and improved reliability in a government system.</li>
            <li>The Cryptic Cube: Built and ran operations with end-to-end process ownership.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">Projects</div>
        <ul>
            <li>Built this AI resume assistant to answer recruiter questions with clear evidence.</li>
            <li>Prototyped AI workflows that speed triage, escalation, and issue summaries.</li>
            <li>Improved support automation reliability by reducing manual handoffs.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

behavior = """
Answer clearly, confidently, and professionally based on the context.
Keep responses concise and structured for recruiters.
Use short bullets when helpful.
"""

st.markdown("### Suggested questions")
st.markdown('<p class="prompt-label">Start with one of these recruiter-focused prompts:</p>', unsafe_allow_html=True)

suggested_questions = [
    "What problems has Jesse solved in production?",
    "How does Jesse approach incident response?",
    "What has Jesse built with AI or automation?",
    "Why would Jesse be a strong hire?",
]

suggest_cols = st.columns(2, gap="small")
for idx, prompt_text in enumerate(suggested_questions):
    with suggest_cols[idx % 2]:
        if st.button(prompt_text, key=f"prompt_{idx}"):
            st.session_state["question_input"] = prompt_text
            st.session_state["run_insight"] = True

question = st.text_input(
    "AI interaction box",
    value=st.session_state.get("question_input", ""),
    placeholder="Ask about production incidents, AI projects, or role fit.",
)

run_from_button = st.button("Generate answer", type="primary")
should_run = run_from_button or st.session_state.pop("run_insight", False)

if should_run:
    if not question.strip():
        st.warning("Enter a question to continue.")
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
            with st.spinner("Generating answer..."):
                response = client.responses.create(model="gpt-5.4-mini", input=prompt)

            st.markdown("#### Answer")
            st.markdown(f'<div class="response-box">{response.output_text}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.markdown(
        '<div class="empty-state">No response yet. Choose a prompt or ask your own question.</div>',
        unsafe_allow_html=True,
    )
