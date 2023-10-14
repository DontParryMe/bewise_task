## How to run postgres database
# In root of the project run the command "pip install requirements"
# In root of the project create file ".env"
# Example of the ".env" file:
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=ww00ac
    POSTGRES_DB=questions
# U can use any username, any password, any database name as u want
# In root of the project open terminal and run the command "docker-compose up -d (U need already installed docker)"
# Open second terminal window still in root of the project and run command "uvicorn main:app --reload"

## U can try to send your post request just open another one terminal window and run the command "python exp.py"
    
