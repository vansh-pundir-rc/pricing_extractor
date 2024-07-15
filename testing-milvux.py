# from pymilvus import MilvusClient
#
# client = MilvusClient(uri="https://in03-5bf8808b5d43f9a.api.gcp-us-west1.zillizcloud.com", token="e2fe4ec184dec44c60d07b5482351b935b860ddc1a6b0c60bd21dcace9e34be8be2881ccbc0ebc0a4ae178e8fa112042e776a4fb")
#
# print(client.get(collection_name="medium_articles"))


from pymilvus import Collection
collection = Collection("medium_articles")      # Get an existing collection.
collection.load()

res = collection.query(
  expr = "book_id in [2,4,6,8]",
  output_fields = ["book_id", "book_intro"],
  consistency_level="Strong"
)
