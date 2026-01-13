from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-Flash", temperature=0)

prompt = PromptTemplate(
    input_variables=["incident"],
    template="""
Classify the incident into ONE category:
LOG_ANALYSIS
SOP_LOOKUP
CALCULATION
GENERAL_REASONING

Incident:
{incident}

Return only the category.
""",
)


def classify(incident: str) -> str:
    return llm.invoke(prompt.format(incident=incident)).content.strip()
