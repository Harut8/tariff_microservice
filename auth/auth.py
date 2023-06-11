from datetime import datetime, timedelta
from functools import wraps
from typing import Union, Any, Callable
import httpx
from fastapi import Depends, HTTPException
from service.parser import ParseEnv


def auth_required(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any):
        try:
            _LOGIN_URL = "http://"+ParseEnv.API_HOST+":"+'8000'+ParseEnv.AUTH_PATH
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url=_LOGIN_URL,
                    headers={
                        "Authorization": "Bearer " + kwargs["authorize"],
                    },
                )
                if response.status_code == 200:
                    return await func(*args, **kwargs)
                raise HTTPException(status_code=403)
        except httpx.HTTPError as error:
            return HTTPException(status_code=500)

    return wrapper

