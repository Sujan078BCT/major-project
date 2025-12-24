from app.crud import items as crud_items,users as crud_users
from app.models import items as item_model , users as user_model
from app.db.database import SessionLocal, engine
from app.schemas import items,users

def init_db():
    """Initialize database with sample data"""
    db = SessionLocal()
    
    # Create sample items
    sample_items = [
        items.ItemCreate(
            name="Laptop",
            description="High-performance laptop for development",
            price=999.99,
            is_available=True
        ),
        items.ItemCreate(
            name="Mouse",
            description="Wireless optical mouse",
            price=29.99,
            is_available=True
        ),
        items.ItemCreate(
            name="Keyboard",
            description="Mechanical gaming keyboard",
            price=89.99,
            is_available=False
        ),
        items.ItemCreate(
            name="Monitor",
            description="27-inch 4K monitor",
            price=299.99,
            is_available=True
        ),
    ]
    
    # Create sample users with passwords
    sample_users = [
        users.UserCreate(
            username="john_doe",
            email="john@example.com",
            full_name="John Doe",
            password="password123"
        ),
        users.UserCreate(
            username="jane_smith",
            email="jane@example.com",
            full_name="Jane Smith",
            password="password123"
        ),
        users.UserCreate(
            username="admin",
            email="admin@example.com",
            full_name="Administrator",
            password="admin123"
        ),
    ]
    
    try:
        # Add items
        for item_data in sample_items:
            crud_items.create_item(db, item=item_data)
        
        # Add users
        for user_data in sample_users:
            crud_users.create_user(db, user=user_data)
            
        print("Database initialized with sample data!")
        print("Sample users created:")
        print("- john_doe / password123")
        print("- jane_smith / password123")
        print("- admin / admin123")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    # Create tables
    user_model.Base.metadata.create_all(bind=engine)
    item_model.Base.metadata.create_all(bind=engine)
    # Initialize with sample data
    init_db() 