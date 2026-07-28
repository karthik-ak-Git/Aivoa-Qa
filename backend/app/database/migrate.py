"""
Database migration script for PharmaQMS AI Copilot.
Run: python -m backend.app.database.migrate
"""
import asyncio
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


async def migrate():
    """Create all tables in the database."""
    from app.database import init_db, create_tables, close_db, check_db_health

    print("=" * 60)
    print("PharmaQMS AI Copilot — Database Migration")
    print("=" * 60)

    try:
        await init_db()
        health = await check_db_health()
        if health["status"] != "connected":
            print(f"ERROR: Database not connected: {health.get('error')}")
            return False

        print(f"Connected to: {health.get('version', 'unknown')}")
        print("\nCreating tables...")

        await create_tables()

        print("\nMigration complete!")
        print("=" * 60)

        # Print table list
        from app.models import Base
        print("\nTables created:")
        for table_name in Base.metadata.tables:
            print(f"  - {table_name}")

        return True

    except Exception as e:
        print(f"\nMigration failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        await close_db()


if __name__ == "__main__":
    success = asyncio.run(migrate())
    sys.exit(0 if success else 1)
