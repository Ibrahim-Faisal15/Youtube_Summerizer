from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

def gen_text(trans_scirpt, user_instructions=""):
  chat_model = ChatGroq(
    temperature=2,
    model="llama3-70b-8192",
    api_key=os.getenv("API_KEY")


  )


  if user_instructions.strip():
    human_prompt = user_instructions
  else:
      human_prompt = "Please summerize the given topic in easy words."


  chat_prompt = ChatPromptTemplate.from_messages([
    ("system",  "Your are a video summrizer AI, whose job  will be to summerize the provided transcript into a complete summary based on user instructions. (Additional Cases: If the transcript is  different then Enlish language, translate it into English. Explain each timestamp like [timestamp : summaray (convert each timestamp into minutes like in a video)] and also add a conclusion at the end after done explaining each timestamp. "),
    ("system", "Please summarize {video}."),
    ("human", human_prompt)
  ])

  output_parser = StrOutputParser()
  chain = chat_prompt | chat_model | output_parser
  prompt_value = chain.invoke({"video": trans_scirpt})

  return prompt_value




