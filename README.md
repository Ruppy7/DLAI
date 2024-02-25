## OCR Repository Readme

This repository comprises two main components: scripts for performing Optical Character Recognition (OCR) tasks on files stored in the Samples folder, and a web application developed using Django and Django Rest Framework (DRF). 

### Usage Instructions

#### Setting up Virtual Environment

To ensure a clean and isolated environment, it's recommended to use Pipenv for managing dependencies:

1. Create a virtual environment:
    ```
    pipenv shell
    ```

2. Install dependencies:
    ```
    pipenv install
    ```

Alternatively, if you prefer not to use a virtual environment, you can install dependencies globally using pip:

```
pip install
```


#### Running Scripts

Scripts can be executed by navigating to the appropriate directory and running the Python files. Ensure to verify file paths and configurations before execution.

Example:
```
py script_name.py
```


#### Running the Django Web Application

To run the Django web application, follow these steps:

1. Navigate to the `DLAI` subdirectory where `manage.py` file is located.

2. Start the local server:
    ```
    py manage.py runserver
    ```

### Web Application Functionality

The web application provides an API and a frontend interface for uploading files, sending them to the backend, and performing OCR to extract information. The extracted information is then displayed on the frontend.

### Note

Please ensure that all necessary configurations and the file paths are set up correctly before running the scripts or starting the web application.
