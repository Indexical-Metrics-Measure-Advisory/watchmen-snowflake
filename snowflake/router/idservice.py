import logging
from fastapi import APIRouter

from snowflake.core.snowflake import get_int_surrogate_key

router = APIRouter()

log = logging.getLogger("app." + __name__)


@router.get("/snowflakeid", tags=["snowflake"])
def next_id():
    return get_int_surrogate_key()
