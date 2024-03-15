# Vertex AI Search Integration
## Example of using Vertex AI Search with an existing web service

This example code shows how to integrate the Vertex AI Search widget within an exisitng web service. For more information, please visit https://cloud.google.com/generative-ai-app-builder/docs/add-widget

## main.py
Defines a FastAPI application with routes for the main page and image upload endpoint.
Renders an HTML template for the main page using the templates/main.html and static/styles.css files.
The widget is loaded in the top section of the page, while other rendered content such as forms and submit buttons are non functional for this demonstration.

## How it works:
A user visits the main page and selects the "Search Here for AskHR" input box.
The Vertex AI Search widget loads and the user enters a query.
The widget returns the result of the query based on the backend configuration.

## How to run it:
Ensure you have the current gcloud command line tool installed and python packages outlined in requirements.txt. You can run "gcloud init" to setup your local evniroment and "pip install -r requirements.txt" to install the python packages.

1. Start the web service locally by running:
python3 -m uvicorn main:app --reload

2. Open a browser and go to http://localhost:8000. Select the "Search Here for AskHR" input box.

3. Enter a query in the search window and review the results.

