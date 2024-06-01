# Simple Semantic Search

A simple semantic search using MongoDB vector search and Huggingface sentence-transformers model.

In this project, I've used MongoDB sample dataset. I've retrieved and updated 100 documents with the embeddings data. That is why, the search result may not be so much perfect.

## Run the Project

```bash
# * update pip
pip install --upgrade pip
# or
pip3 install --upgrade pip

# * install dependencies
pip install -r requirements.txt
# or
pip3 install -r requirements.txt

# * run
python movie_reqs.py
# or
python3 movie_reqs.py
```

## Additionals

### Load Sample Data in MongoDB

To begin, first create a project in MongoDB Atlas. Once the project is created, proceed to create a cluster. Then, create a user for the database and configure the network access settings.

After completing these steps, navigate to the **Database** section on the left sidebar. Next to the **Browse Collections** button, you'll see three dots. Click on the three dots to access the **Load Sample Dataset** option. Simply click on that and the data will be loaded in a few minutes.

### Create Vector Search Index in MongoDB

To create a vector search index, follow these steps:

1. Click on the **Browse Collection** button.
2. Look for the tab labeled **Atlas Search**.
3. In the Atlas Search tab, you can create a search index. Choose Atlas Vector Search and click _Next_.
4. Select the database and collection.
5. Name your index and set the parameters according to your requirements.

Here's an example of JSON to set preferences for the index:

```json
{
  "fields": [
    {
      "type": "vector",
      "path": "plot_embeddings",
      "numDimensions": 384,
      "similarity": "cosine"
    }
  ]
}
```
