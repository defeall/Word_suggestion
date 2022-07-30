# Word Suggestion Application


## To run the application <br>

Step 1: Clone this repo or download the code in a directory

Step 2: Create a virtualenv and activate it by writing following commands in terminal

        - To install virtualenv
            pip install virtualenv

        - To create a virtualenv
            virtualenv env
        
        - To activate virtualenv
            env/Scripts/activate (For windows)
            source env/bin/activate (For mac/unix)


Step 3: Install the packages mentioned in requirements.txt file by writing the following command in terminal:

        - pip install -r requirements.txt

Step 4: Set following variable in terminal:
        
        set FLASK_APP=app
        set FLASK_ENV=developemnt

Step 5: Run the app in localhost by writing following command in terminal:
        
        flask run