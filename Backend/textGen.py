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

  system_prompt = "Your are a video summrizer AI, whose job will be to job will be to summerize the provided transcript into a complete summary based on user instructions. (Additional Cases: If the transcript is  different then Enlish language, translate it into English.) "
  system_prompt_v2 = "Please summarize {video}."


  if user_instructions.strip():
    human_prompt = "Please the given topic in easy words."
  else:
      human_prompt = "Please the given topic in easy words."




  chat_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("system", system_prompt_v2),
    ("human", human_prompt)
  ])

  output_parser = StrOutputParser()
  chain = chat_prompt | chat_model | output_parser
  prompt_value = chain.invoke({"video": trans_scirpt})

  return prompt_value



input = [ 
"00:00:01.200 All right, so here we are, in front of theelephants",
"00:00:05.318 the cool thing about these guys is that theyhave really...",
"00:00:07.974 really really long trunks",
"00:00:12.616 and that's cool",
"00:00:14.421 (baaaaaaaaaaahhh!!)",
"00:00:16.881 and that's pretty much all there is tosay",
]


print(gen_text(input))