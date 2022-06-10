# SKY


## My Approach
In this project, I have used Python Django Rest Framework. I have defined a model named Report and loaded the model with all the instances from both the clouds. To get a list of running instances grouped by teams, I have defined an api with endpoint **/report**. <br/>


## Setting up the envrionment
Create a virtual environment, activate the same, and install all the required packages mentioned in the requirements.txt file using below commands.

```

virtualenv .venv
.venv/Scripts/activate
pip3 install -r requirements.txt

```

## Running the application


Please run the application using below command. 

```
python manage.py runserver

```

This will start the local server running on port 8000. Access the report using api on http://127.0.0.1:8000/report/

  
