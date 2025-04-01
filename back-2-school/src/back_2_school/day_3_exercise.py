from pydantic import BaseModel, confloat, field_validator
from typing import List

class Book(BaseModel):
    title: str
    author: str
    price: confloat(ge=0)

class Library(BaseModel):
    books: List[Book]

    @field_validator("books")
    @classmethod
    def check_book_title_length(cls, value):
        for b in value:
            if len(b.title) < 3:
                raise ValueError(f'Book title of {b.title} is less than three characters')
        return value

library1_data = {
    "books" : [
    {"title":"In the dark", "author":"George", "price":15.3},
    {"title":"Don't go to sleep", "author":"Laskaris", "price":3.1415}
]
}

library2_data = {
    "books": [
    {"title":"Dune", "author":"Frank Herbert", "price":12.5},
    {"title":"OA", "author":"Maliatsis", "price":99.99}
]
}

try:
    library_1 = Library(**library1_data)
except ValueError as e:
    print("Validation Error:", e)

try:
    library_2 = Library(**library2_data)
except ValueError as e:
    print("Validation Error:", e)