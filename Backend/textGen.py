from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

def gen_text(trans_scirpt, user_instructions=""):
  chat_model = ChatGroq(
    temperature=0,
    model="llama-3.1-70b-versatile",
    api_key=os.getenv("API_KEY")


  )


  if user_instructions.strip():
    human_prompt = user_instructions
  else:
      human_prompt = "Please summerize the given topic in easy words."


  chat_prompt = ChatPromptTemplate.from_messages([
    ("system",  """
        PROMPT = You will be given an array of objects where each object contains text, start, durations of the transcript. Your job will be to take this array of objects as an input, summarize them in the following pattern:

        <b>Following is the complete summary of the input video.</b>
        [0:00] explain the sentence associated with this duration
        .
        .
        .
        etc....

        <b>Conclusion</b>
        Conclusion of the Transcript............

        Note: convert the time into video time like hours:minutes:seconds
        Note: Put '##' after completing explaining each transcript. DONT MISS THIS STEP
        Note: Be sure to use html tags for formatting....
        Note: Start with this pattern and don't write starting sentance.
    
        """),
    ("system", "Please summarize {video}."),
    ("human", human_prompt)
  ])

  output_parser = StrOutputParser()
  chain = chat_prompt | chat_model | output_parser
  prompt_value = chain.invoke({"video": trans_scirpt})

  return prompt_value




