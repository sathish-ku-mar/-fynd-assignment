# fynd-assignment

### System Requirements
- Python 3+
- Anaconda 3
------------
### 1. Create of virtual environment
Open the terminal and enter the following command:<br />`$ conda create -n <environment_name> python=3`<br />
Once the environment has been created, activate the environment:<br />`$ conda activate <environment_name>`

------------
### 2. Clone project to the local machine
In the terminal, navigate to the location where the project folder has to be created. Then enter the git command to clone the project:<br />`$ git clone https://github.com/sathish-ku-mar/fynd-assignment.git`<br />
Once cloned, change the directory to **fynd_assignment**<br />`$ cd fynd_assignment`

------------
### 3. Install the project requirements
Install the python packages listed in the **requirements.txt** file.
Enter the following command in the terminal:<br />`$ pip install -r requirements.txt`

------------

### 4. Run the development server
To start the development server, run the following command:<br />`$ python manage.py runserver`<br />
By default the server runs on port`8000`<br />
Check whether the server is running by going to [localhost:8000/admin](localhost:8000/admin "localhost:8000/admin")

------------
#### References
Anaconda : https://docs.anaconda.com/anaconda/<br />Django : https://docs.djangoproject.com/en/2.2/<br />
