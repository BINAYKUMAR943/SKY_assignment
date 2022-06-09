# Global task


## My Approach
In this project, I have used Python Django Rest Framework. I have defined a model named Report and loaded the model with all the instances from both the clouds. An api with endpoint /report is defined to return the list of running instances grouped by teams.<br/>


## Setting up the envrionment
Create a virtual environment, install all the required packages mentioned in the requirements.txt file

```

virtualenv .venv
pip3 install -r requirements.txt

```

## Running the application


Please run the application using below command. 

```
python manage.py runserver

```

This will start the local server running on port 8000. You will get the required output in the url http://127.0.0.1:8000/report/

  
