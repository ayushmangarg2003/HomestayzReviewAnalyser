from pymongo import MongoClient
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()

# If using Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
isGemini = True
    
 
mongo_username = os.getenv('MONGO_USERNAME')
mongo_password = os.getenv('MONGO_PASSWORD')
mongo_database_name =  os.getenv('DATABASE_NAME')
mongo_collection_name = os.getenv('COLLECTION_NAME')

if isGemini == True:
    llm = genai.GenerativeModel('gemini-pro')
else:     
    llm = HuggingFaceHub(repo_id="google/flan-t5-base")
 
def EstablishConnection(username, password):
    print("Establishing Connection ...")
    
    uri = f"mongodb+srv://{username}:{password}@cluster0.pib3sys.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    cl = MongoClient(uri)
        
    return cl

def getReviewString(cl, db_name, coll_name):
    print("Transforming Reviews ... ")
    
    database = cl[db_name] 
    coll = database[coll_name]
    reviews = [] 
    
    for document in coll.find({}):
        reviews.append(document['review'])
    rev_str = ' || '.join(reviews)
        
    return rev_str

def getResponseFromLLM(model, rev_str, isGemini):
    prompt = f'''
    Your Task is to go through a string containing multiple reviews spearated by || and then tell Top 5 Positive Points and Top 5 Negative Points based on that in points.
    Here are my reviews {rev_str}'''
    print("Analysing Reviews ...")

    if isGemini == True:
        res = model.generate_content(prompt).text
    else:
        res = model(prompt)
        
    return res

client = EstablishConnection(mongo_username, mongo_password)
review_string = getReviewString(client,mongo_database_name, mongo_collection_name )

response = getResponseFromLLM(llm, review_string, isGemini=isGemini)
print("Response :" , response)

