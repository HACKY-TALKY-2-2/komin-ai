import fastapi
from route import dashboard_route
from fastapi.middleware.cors import CORSMiddleware


app = fastapi.FastAPI()
app.add_middlewareCORSMiddleware(
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
