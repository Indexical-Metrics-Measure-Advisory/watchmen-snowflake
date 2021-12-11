
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from snowflake.config.config import settings
from snowflake.monitor.prometheus import init_prometheus_monitor
from snowflake.router import idservice

log = logging.getLogger("app." + __name__)

app = FastAPI(title=settings.PROJECT_NAME, version="0.1.35",
              description="a lighter platform for data analytics")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if settings.PROMETHEUS_ON:
    init_prometheus_monitor(app)


log.info("system init rest api")

app.include_router(idservice.router)

