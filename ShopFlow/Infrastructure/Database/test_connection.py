
from sqlalchemy import text
from Infrastructure.Database.database import engine

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Database connection successful.")

        version = connection.execute(
            text("SELECT version()")
        ).fetchone()

        print(f"Database version: {version[0]}")

except Exception as e:
    print(f"Database connection failed: {e}")

finally:
    engine.dispose()
