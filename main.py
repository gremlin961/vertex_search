from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import base64
import json
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part



# Create a FastAPI app
app = FastAPI()

# Mount the static files directory for serving static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create a Jinja2Templates object for rendering HTML templates
templates = Jinja2Templates(directory="templates")


# Route for the main page
@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    # Render the main.html template
    return templates.TemplateResponse("main.html", {"request": request})
