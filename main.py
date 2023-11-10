import fastapi
from route import dashboard_route, analyze_route
from fastapi.middleware.cors import CORSMiddleware


app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(dashboard_route.router, prefix='/dashboard')
app.include_router(analyze_route.router, prefix='/analyze')

