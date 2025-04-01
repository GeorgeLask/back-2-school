from pydantic import BaseModel
from typing import List

class Book(BaseModel):
    title: str
    author: str
    price: float

class Library(BaseModel):
    name: str
    books: List[Book]

# Create an instance of the Library model
library = Library(
    name="City Library",
    books=[
        Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price=10.99),
        Book(title="1984", author="George Orwell", price=6.99)
    ]
)

library_json = library.model_dump_json()
print("Serialized JSON:")
print(library_json)

library_from_json = Library.model_validate_json(library_json)
print("\nDeserialized Library Model:")
print(library_from_json)

# Nested models in JSON serialization
nested_json = '''
{
    "name": "Small Library",
    "books": [
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 8.99},
        {"title": "Brave New World", "author": "Aldous Huxley", "price": 9.99}
    ]
}
'''

# Deserialize the nested JSON into the Library model
library_from_nested_json = Library.model_validate_json(nested_json)
print("\nDeserialized Nested Library Model:")
print(library_from_nested_json)

from pydantic import BaseModel, Field
from datetime import datetime

class Event(BaseModel):
    name: str
    date: datetime

    class Config:
        # Custom encoder for datetime
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

# Create an event instance
event = Event(name="Conference", date=datetime(2025, 3, 26, 10, 30))

# Serialize with custom encoder
event_json = event.model_dump_json()
print("\nSerialized Event with Custom Date Format:")
print(event_json)

# Invalid JSON data (missing required field 'price')
invalid_json = '''
{
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien"
}
'''

try:
    book = Book.model_validate_json(invalid_json)  # This will raise a ValidationError
except ValueError as e:
    print("\nValidation Error:", e)
