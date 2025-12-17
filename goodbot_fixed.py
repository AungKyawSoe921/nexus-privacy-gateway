from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.docstore.document import Document

# 1. THE PRIVATE KNOWLEDGE (The "Secret" Policy)
# This is data that DOES NOT exist on the internet.
policy_text = """
Orbital Coffee Payment Policy:
We are an experimental space cafe.
1. We strictly DO NOT accept cash, credit cards, or Bitcoin.
2. The ONLY valid form of payment is Moon Rocks.
3. Refunds are issued in Stardust.
"""

print("--- 🧠 SMART BOT (Your RAG Approach) ---")
print("Loading private company policies...")

# 2. CREATE THE KNOWLEDGE BASE (Embeddings)
documents = [Document(page_content=policy_text)]
embed_model = OllamaEmbeddings(model="tinyllama") # Or mistral
db = Chroma.from_documents(documents, embed_model)
retriever = db.as_retriever()

# 3. THE PIPELINE
llm = Ollama(model="tinyllama") 

question = "I want to buy a latte at Orbital Coffee. Can I pay with a credit card?"
print(f"\nUser: {question}")

# A. Retrieve relevant policy
docs = retriever.invoke(question)
context = docs[0].page_content

# B. Augment the prompt
prompt = f"""
You are a Customer Support Agent for Orbital Coffee.
Answer the question based ONLY on the specific company policy below.

POLICY:
{context}

QUESTION:
{question}
"""

# C. Generate Answer
response = llm.invoke(prompt)

print(f"Agent: {response}")
print("--------------------------------------------------")