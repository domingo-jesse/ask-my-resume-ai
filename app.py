import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Ask Jesse AI", page_icon="🧠", layout="centered")

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

mode = st.selectbox(
    "Mode",
    ["General Q&A", "Interview Mode", "Role Fit"]
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

st.title("Ask Jesse AI")
st.write(
    """
This AI assistant answers questions about my background, skills, projects, and career direction.

Try asking about:
- support engineering experience
- healthcare technology background
- technical strengths
- role fit
- interview questions
"""
)

st.write("Suggested questions:")
st.markdown("- What experience does Jesse have?")
st.markdown("- What roles is Jesse a good fit for?")
st.markdown("- What are Jesse’s strongest technical skills?")
st.markdown("- What interview questions would you ask Jesse?")

question = st.text_input("Ask a question:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
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
                response = client.responses.create(
                    model="gpt-5.4-mini",
                    input=prompt
                )

            st.subheader("Answer")
            st.write(response.output_text)

        except Exception as e:
            st.error(f"Error: {e}")