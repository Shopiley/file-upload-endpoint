# file-upload

## Set up
- Install Python from <https://www.python.org/downloads/> if you haven't
- cd into the project folder
- Ensure a virtual environment has been created and activated by either using

    ```bash
    python -m venv venv # to create a virtualenv
    source venv/bin/activate # activate for linux
    venv\Scripts\activate # activate for windows
    ```

  Then install the requirements
  
    ```bash
    pip install -r requirements.txt
    ```

- Start the server by using the following command

  ```bash
  py -m uvicorn app:app --reload
  ```

