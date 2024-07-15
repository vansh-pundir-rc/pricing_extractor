
from pymilvus import Collection
collection = Collection("medium_articles")      # Get an existing collection.
collection.load()

res = collection.query(
  expr = "book_id in [2,4,6,8]",
  output_fields = ["book_id", "book_intro"],
  consistency_level="Strong"
)
