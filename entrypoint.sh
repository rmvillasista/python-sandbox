#!/bin/sh
set -e

echo "Running database migrations..."
alembic upgrade head

echo "Starting Uvicorn web server..."

echo "Waiting for PostgreSQL database..."

python << END
import sys
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

async def wait_for_db():
    db_url = os.getenv("DATABASE_URL")
    engine = create_async_engine(db_url)
    for _ in range(30):
        try:
            async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            print("Database connection successful!")
            await engine.dispose()
            sys.exit(0)
        except Exception:
            await asyncio.sleep(1)
    print("Database connection timed out.")
    sys.exit(1)

asyncio.run(wait_for_db())
END

echo "Executing Alembic database migrations..."
python -m alembic upgrade head

echo "Starting Uvicorn web application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000