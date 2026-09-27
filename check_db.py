import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

# Replace with your actual Database URL
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/taskdb"

async def check_tables():
    engine = create_async_engine(DATABASE_URL)
    async with engine.connect() as conn:
        # List all tables in the public schema
        result = await conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
        """))
        tables = [row[0] for row in result.fetchall()]
        print("Existing tables:", tables)

        # Inspect columns of the tasks table
        if "tasks" in tables:
            columns = await conn.execute(text("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_name = 'tasks';
            """))
            print("\nColumns in 'tasks':")
            for col in columns.fetchall():
                print(f" - {col[0]} ({col[1]}, nullable: {col[2]})")

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(check_tables())