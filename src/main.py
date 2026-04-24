from fastapi import FastAPI

from src.api import router as api_main_router


app = FastAPI()
app.include_router(api_main_router)




if __name__ == "__main__":
    pass