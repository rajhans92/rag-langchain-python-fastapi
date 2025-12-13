from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.helpers.databaseHandler import Base, engine
from app.helpers.config import API_VERSION
from app.helpers.exceptionHandler import (
    http_exception_handler,
    validation_exception_handler,
    value_error_handler,
    global_exception_handler
)
from app.routers import usersRoute, fileUploadRoute
Base.metadata.create_all(bind=engine)
app = FastAPI()

# Register exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ValueError, value_error_handler)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(usersRoute.router, prefix='/api/'+API_VERSION)
app.include_router(fileUploadRoute.route, prefix='/api/'+API_VERSION)

@app.get("/")
async def read_root():
    return {"Hello": "World"}