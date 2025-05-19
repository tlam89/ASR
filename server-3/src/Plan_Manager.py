import os, glob
import json
import warnings
warnings.filterwarnings("ignore")

from elasticsearch import Elasticsearch

from src.utils import initialize_a_logger

logger = initialize_a_logger()

path = "/assets/plans/cxr_examination.json"
with open('your_file.json', 'r') as file:
    json_body = json.load(file)



es = Elasticsearch('http://localhost:9200')

# Define the index name
index_name = "chest_x_ray_index"

# Create the index with mapping (optional, but recommended for nested fields)
mapping = {
    "mappings": {
        "properties": {
            "chest_x_ray": {
                "properties": {
                    "views": {
                        "type": "nested",
                        "properties": {
                            "name": {"type": "keyword"},
                            "components": {
                                "type": "nested",
                                "properties": {
                                    "name": {"type": "keyword"},
                                    "parts": {
                                        "type": "nested",
                                        "properties": {
                                            "name": {"type": "keyword"},
                                            "normal": {"type": "boolean"},
                                            "description": {"type": "text"},
                                            "relationship": {"type": "keyword"}
                                        }
                                    },
                                    "zones": {
                                        "type": "nested",
                                        "properties": {
                                            "name": {"type": "keyword"},
                                            "parts": {
                                                "type": "nested",
                                                "properties": {
                                                    "name": {"type": "keyword"},
                                                    "normal": {"type": "boolean"},
                                                    "description": {"type": "text"}
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "pa_examination_parameter": {
                                "properties": {
                                    "parameters": {"type": "nested"}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# Create the index if it doesn't exist
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=mapping)
    logger.debug(f"Index '{index_name}' created with mapping.")
else:
    logger.debug("Index '{index_name}' already exists.")

# Index the document
doc_id = "1"  # Unique ID for the document
response = es.index(index=index_name, id=doc_id, body=json_body)

# Check the response
if response['result'] == 'created' or response['result'] == 'updated':
    logger.debug(f"Document successfully indexed with ID: {doc_id}")
else:
    logger.debug(f"Failed to index document: {response}")

# Optional: Verify the document was indexed
result = es.get(index=index_name, id=doc_id)
logger.debug("Retrieved document:", json.dumps(result['_source'], indent=2))

if __name__=="__main__":
    path = "/assets/plans/cxr_examination.json"
    with open('your_file.json', 'r') as file:
        data = json.load(file)




