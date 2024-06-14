from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#dummy datastore
items = ["Item 1", "Item 2"]

@app.get("/", response_class=HTMLResponse)
def get_items(request: Request):
    context = {
        "request": request,
        "items": items
    }
    return templates.TemplateResponse("items.html", context)


@app.post("/add-item")
def add_item(request: Request, item: str = Form(...)):
    items.append(item)
    context = {
        "request": request,
        "item":item
    }
    return templates.TemplateResponse("partials/item.html", context)
