import os
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Jesse Domingo | AI Resume",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fdf2f8 0%, #eef2ff 45%, #ecfeff 100%);
    }
    .main .block-container {
        max-width: 1060px;
        padding-top: 1rem;
        padding-bottom: 3rem;
        padding-left: 1.75rem;
        padding-right: 1.75rem;
    }
    section[data-testid="stSidebar"] {
        width: 390px !important;
    }
    section[data-testid="stSidebar"][aria-expanded="false"] {
        width: 0 !important;
    }
    [data-testid="stSidebarCollapsedControl"] {
        margin-left: 0.35rem;
        margin-top: 0.35rem;
    }
    @media (max-width: 768px) {
        .main .block-container {
            max-width: 100%;
            padding-top: 1rem;
            padding-bottom: 2.25rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    .minimal-wrap {
        text-align: center;
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }
    .hero h1 {
        margin: 0;
        font-size: 3rem;
        line-height: 1.05;
        color: #0f172a;
    }
    .hero .title {
        margin: 0.7rem 0 0 0;
        font-size: 1.1rem;
        color: #334155;
        font-weight: 600;
    }
    .hero .tagline {
        margin: 0.9rem 0 0 0;
        font-size: 1rem;
        color: #475569;
    }
    .suggestion-label {
        margin: 0;
        color: #64748b;
        font-size: 0.92rem;
        letter-spacing: 0.02em;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 999px;
        border: 1px solid #dbe3f1;
        background: #ffffff;
        color: #0f172a;
        padding: 0.65rem 0.9rem;
        font-weight: 500;
    }
    div.stButton > button:hover {
        border-color: #b9c8e7;
        background: #f8fbff;
    }
    div.stButton > button[kind="primary"] {
        border: 0;
        background: #0f172a;
        color: #ffffff;
        font-weight: 600;
    }
    .response-box {
        border: 1px solid #d9e4ff;
        background: #f8fbff;
        border-radius: 14px;
        padding: 1rem;
        text-align: left;
    }
    .section-card {
        border: 1px solid #e2e8f0;
        background: #ffffff;
        border-radius: 14px;
        padding: 1rem 1.1rem;
        text-align: left;
    }
    .section-card h3 {
        margin: 0 0 0.55rem 0;
        color: #0f172a;
        font-size: 1rem;
    }
    .section-card p,
    .section-card li {
        color: #334155;
        font-size: 0.95rem;
    }
    .section-card ul {
        margin: 0;
        padding-left: 1.1rem;
    }
    .sidebar-title {
        margin: 0;
        color: #0f172a;
        font-weight: 700;
        font-size: 1.1rem;
    }
    .ticket-count {
        margin-top: 0.2rem;
        color: #64748b;
        font-size: 0.88rem;
    }
    .ticket-card {
        border-radius: 12px;
        padding: 0.72rem 0.8rem;
        margin-bottom: 0.55rem;
        border: 1px solid rgba(148, 163, 184, 0.35);
    }
    .ticket-card strong {
        color: #0f172a;
    }
    .ticket-card p {
        margin: 0.2rem 0 0 0;
        color: #1e293b;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=api_key)

urgency_styles = {
    "HIGH": "background: rgba(239, 68, 68, 0.16); border-color: rgba(239, 68, 68, 0.35);",
    "MEDIUM": "background: rgba(245, 158, 11, 0.14); border-color: rgba(245, 158, 11, 0.35);",
    "LOW": "background: rgba(34, 197, 94, 0.14); border-color: rgba(34, 197, 94, 0.35);",
}

ticket_queue = [
    {"id": "#48322", "title": "System timeout on prior auth submission", "urgency": "HIGH", "status": "Blocked"},
    {"id": "#5-4BA8", "title": "Unable to submit or check prior authorizations", "urgency": "HIGH", "status": "New"},
    {"id": "#5-F9BD", "title": "Unable to submit or check prior authorizations", "urgency": "HIGH", "status": "New"},
    {"id": "#N/A", "title": "Prior authorizations not submitting or viewable", "urgency": "MEDIUM", "status": "Completed"},
    {"id": "#48323", "title": "Dropdown menu overlaps text on small screens", "urgency": "MEDIUM", "status": "New"},
    {"id": "#48324", "title": "System inaccessible, 500 error", "urgency": "MEDIUM", "status": "Blocked"},
    {"id": "#5-9DC2", "title": "Profile update not saving", "urgency": "MEDIUM", "status": "Completed"},
    {"id": "#12345", "title": "Profile update not saving", "urgency": "LOW", "status": "Completed"},
    {"id": "#48326", "title": "Export reports to Excel", "urgency": "LOW", "status": "New"},
]

def dedupe_tickets(tickets):
    unique_tickets = []
    seen = set()
    for ticket in tickets:
        key = (ticket["title"], ticket["urgency"], ticket["status"])
        if key in seen:
            continue
        seen.add(key)
        unique_tickets.append(ticket)
    return unique_tickets

display_tickets = dedupe_tickets(ticket_queue)

with st.sidebar:
    st.markdown('<p class="sidebar-title">🎟️ Ticket Queue</p>', unsafe_allow_html=True)
    total_tickets = len(display_tickets)
    in_progress_tickets = sum(1 for ticket in display_tickets if ticket["status"] == "Blocked")
    completed_tickets = sum(1 for ticket in display_tickets if ticket["status"] == "Completed")
    st.markdown(f'<p class="ticket-count">{total_tickets} ticket(s)</p>', unsafe_allow_html=True)
    stats_col_1, stats_col_2 = st.columns(2, gap="small")
    stats_col_1.metric("In progress", in_progress_tickets)
    stats_col_2.metric("Completed", completed_tickets)

    selected_ticket_id = st.selectbox(
        "Choose ticket",
        options=[ticket["id"] for ticket in display_tickets],
        label_visibility="collapsed",
    )
    selected_ticket = next(
        (ticket for ticket in display_tickets if ticket["id"] == selected_ticket_id),
        display_tickets[0],
    )

    selected_urgency_style = urgency_styles.get(selected_ticket["urgency"], "")
    st.markdown(
        f"""
        <div class="ticket-card" style="{selected_urgency_style}">
            <strong>{selected_ticket['id']} · {selected_ticket['title']}</strong>
            <p>{selected_ticket['urgency']} · {selected_ticket['status']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

profile_context = """
NAME: Jesse Domingo
TITLE: Technical Support Engineer | AI Workflow Builder

SUMMARY:
- Debugs production incidents using logs, SQL, and APIs
- Leads incident response across engineering, product, and operations
- Turns root-cause findings into fixes that reduce repeat outages
- Communicates technical issues clearly to technical and non-technical stakeholders

EXPERIENCE:
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

behavior = """
Answer clearly, confidently, and professionally based on the context.
Keep responses concise and structured for recruiters.
Use short bullets when helpful.
"""

st.markdown('<div class="minimal-wrap">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero">
        <h1>Jesse Domingo</h1>
        <p class="title">Technical Support Engineer | AI Workflow Builder</p>
        <p class="tagline">I solve high-pressure production problems and build practical automation teams can trust.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-card">
        <h3>About me</h3>
        <ul>
            <li>I specialize in incident response, escalations, and finding the true root cause quickly.</li>
            <li>I connect engineering, product, and operations so issues get solved end-to-end.</li>
            <li>I use AI workflows to make support work faster, cleaner, and more consistent.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-card">
        <h3>How to use this page</h3>
        <ul>
            <li>Pick one of the suggested prompts or type your own question below.</li>
            <li>Ask about my impact, incident approach, projects, or collaboration style.</li>
            <li>Use this as a quick recruiter snapshot before an interview.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="suggestion-label">Suggested questions</p>', unsafe_allow_html=True)

suggested_questions = [
    "What problems has Jesse solved?",
    "How does Jesse handle incidents?",
    "What has Jesse built?",
    "Why hire Jesse?",
]

suggest_cols = st.columns(2, gap="small")
for idx, prompt_text in enumerate(suggested_questions):
    with suggest_cols[idx % 2]:
        if st.button(prompt_text, key=f"prompt_{idx}"):
            st.session_state["question_input"] = prompt_text
            st.session_state["run_insight"] = True

question = st.text_input(
    "Question input",
    value=st.session_state.get("question_input", ""),
    placeholder="Ask about Jesse's impact, technical strengths, or workflow style.",
    label_visibility="collapsed",
)

run_from_button = st.button("Get Insight", type="primary")
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
            with st.spinner("Thinking..."):
                response = client.responses.create(model="gpt-5.4-mini", input=prompt)

            st.markdown(f'<div class="response-box">{response.output_text}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
