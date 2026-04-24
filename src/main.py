from fastapi import FastAPI

from src.api import router as api_main_router
from src.database.postgres import init as DB_INIT


DB_INIT()
app = FastAPI()
app.include_router(api_main_router)




if __name__ == "__main__":
    pass