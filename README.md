## CloudWatch Logging with Django

This project demonstrates how to set up logging for a Django application with AWS CloudWatch using `watchtower`.

Setup Instructions

#### Step 1: Create a Virtual Environment

First, make sure you have `virtualenv` installed. If not, you can install it using pip:
pip install virtualenv

Then, create a virtual environment and activate it:

virtualenv venv

On Windows

venv\Scripts\activate

On macOS/Linux

source venv/bin/activate

#### Step 2: Install Requirements

Navigate to the `backend` directory and install the required packages using `pip`:
cd backend

pip install -r requirements.txt

#### Step 3: Create the `.env` File

Create a file named `.env` in the `backend` directory with the following content:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_DEFAULT_REGION=

Make sure to fill in your actual AWS credentials and region in the `.env` file.

Running the Application

After setting up the virtual environment, installing the requirements, and creating the `.env` file, you can run the Django application:

cd backend

python manage.py runserver

Verifying Logs

To verify that logging is working, navigate to your application in a web browser (e.g., http://127.0.0.1:8000/). Then, check the AWS CloudWatch log group `django-test` and the stream `backend` to see the logs.

Additional Information

For more information on setting up Django logging with AWS CloudWatch, refer to the official documentation for the watchtower library.
