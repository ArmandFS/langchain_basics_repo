from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_community.chat_models import ChatOllama

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOllama(model="llama3")

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.

messages = [
		#this will give context
	  SystemMessage(content="Solve the following math problems"),
	  HumanMessage(content = "What is 120 divided by 12?"),
]

#invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")


#message from an AI
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 120 divided by 12?"),
    AIMessage(content="120 divided by 12 is 10."),
    HumanMessage(content="What is 10 times 55?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
