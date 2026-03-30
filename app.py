import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Ask My Resume AI")

st.title("Ask My Resume AI")
st.write("Try asking:")
st.write("- What experience does Jesse have?")
st.write("- What roles is Jesse a good fit for?")
st.write("- What are Jesse’s strongest technical skills?")
st.write("- What interview questions would you ask Jesse?")

client = OpenAI()

profile_context = """
NAME: Jesse Domingo

HEADLINE:
Technical Program Manager | Technical Operations | Support Engineering

PROFESSIONAL SUMMARY:
Jesse is a technical support and operations professional with a strong background in healthcare technology, production troubleshooting, root cause analysis, and cross-functional coordination. He is experienced in working with engineering, product, and operations teams to resolve complex incidents, improve workflows, and drive reliability.

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
- Led cross-team incident investigations
- Coordinated debugging across APIs, automation pipelines, and databases
- Used SQL, Postman, and logs to diagnose failures
- Improved time to resolution for escalations
- Communicated findings to technical and business stakeholders
- Supported incident response during production outages
- Mentored new team members

Technical Support Analyst  
Olive AI
- Managed escalated issues in a healthcare automation platform
- Investigated defects through logs, validation, and diagnostics
- Worked with engineering and product to reproduce bugs and validate fixes
- Created technical documentation and reports

Software Implementation Consultant  
FAST Enterprises
- Worked on a large-scale government vehicle tax system
- Debugged and fixed application logic
- Improved reliability and system behavior

Founder / Owner  
The Cryptic Cube
- Built and operated an escape room business
- Designed puzzle systems and customer experiences
- Managed operations, finances, and process improvement

PROJECTS:
- Built an AI-powered resume web app that answers questions about Jesse’s background
- Exploring AI-powered Jira ticket triage and support workflow automation
- Interested in AI agents, support tooling, and workflow orchestration

LEADERSHIP AND COACHING:
- Speech and Debate Coach
- Mentors others through structured feedback and coaching
- Eagle Scout

CAREER GOALS:
Jesse is interested in roles that combine technical problem-solving, operations, support engineering, AI workflow automation, and cross-functional coordination. He is especially interested in building practical AI tools that improve triage, support, and decision-making workflows.

IMPORTANT RULES:
- Only answer using the information in this context
- Do not invent facts
- If something is not supported here, say so clearly
- When useful, explain Jesse’s fit for a role based on the evidence above
"""

question = st.text_input("Ask a question:")

if st.button("Ask"):
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=f"""
You are an AI assistant acting like a hiring manager reviewing Jesse Domingo.

Rules:
- Only use the resume
- Do NOT make up information
- If something is not in the resume, say that clearly
- Be professional but conversational

When answering:
- Give a clear answer
- Mention relevant experience or skills
- If the question is vague or weak, suggest a better follow-up question

RESUME:
{profile_context}

QUESTION:
{question}
"""
    )
    st.write(response.output_text)