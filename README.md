## This is a Review Analyser Build for my Project Homestayz
Link to Homestayz :- https://homestayz.vercel.app/         
Link to its Github :- https://github.com/ayushmangarg2003/Homestayz         

## Tech Used
Language: Python         
Model : Gemini-Pro         
Framework : Langchain         


## Requirements
pymongo   
langchain==0.0.184   
python-dotenv==1.0.0   
huggingface-hub==0.14.1   
google-generativeai   

## Steps To Run      
1. Create Environment using :-        
   conda create -p venv python=3.10 -y      
2. Activate Environment        
   conda activate venv/      
3. Install requirements.text        
   pip install -r requirements.txt      
4. Run app.py file by        
   python app.py      

## ENV FILE STRUCTURE            

HUGGINGFACEHUB_API_TOKEN= 'YOUR_HUGGINGFACE_KEY'        
MONGO_PASSWORD = 'YOUR_MONGO_PASSWORD'        
MONGO_USERNAME= 'YOUR_MONGO_USERNAME'        
DATABASE_NAME= 'YOUR_DB_NAME'        
COLLECTION_NAME= 'YOUR_COLLECTION_NAME'      
GEMINI_API_KEY = 'YOUR_GEMINI_KEY'      
