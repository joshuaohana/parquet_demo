import random
import json
import os

import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import numpy as np

from flask import Flask, Response
from flask_cors import CORS


# Setup the server
parquet_dir = '../data/'
app = Flask(__name__)
CORS(app)


def get_combined_dataframe():
    # Returns a dataframe combining all the parquet files in the data directory
    parquet_files = [file for file in os.listdir(
        parquet_dir) if file.endswith('.parquet')]
    if not parquet_files:
        return None

    dfs = []
    for file in parquet_files:
        table = pq.read_table(os.path.join(parquet_dir, file))
        df = table.to_pandas()
        dfs.append(df)

    df_concatenated = pd.concat(dfs)

    return df_concatenated


@app.route('/nodes/<id>', methods=['GET'])
def get_node_by_id(id):
    df = get_combined_dataframe()
    mask = df['id'] == int(id)
    node = df.loc[mask].squeeze().to_dict()

    if node is None:
        return Response(status=404)

    # Convert ndarray to list
    node['neighbors'] = node['neighbors'].tolist()

    return json.dumps(node)


@app.route('/nodes/random', methods=['GET'])
def get_random_node():
    df = get_combined_dataframe()

    if df is None or df.empty:
        return Response(status=204)

    node = df.sample().squeeze().to_dict()

    # Convert ndarray to list
    node['neighbors'] = node['neighbors'].tolist()

    return json.dumps(node)


@app.route('/nodes/length', methods=['GET'])
def get_num_nodes():
    df = get_combined_dataframe()

    if df is None or df.empty:
        return Response(status=204)

    return str(len(df))


@app.route('/nodes', methods=['POST'])
def make_nodes():
    # Generate and save random nodes to a parquet file
    num_nodes = random.randint(500, 1000)

    nodes = []
    for i in range(num_nodes):
        num_neighbors = random.randint(0, 5)
        neighbors = random.sample(range(num_nodes), num_neighbors)
        node = {
            'id': i,
            'foo': random.randint(0, 1000),
            'bar': random.randint(0, 1000),
            'baz': random.randint(0, 1000),
            'qux': ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for j in range(random.randint(3, 6))),
            'quux': ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for j in range(random.randint(3, 6))),
            'corge': ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for j in range(random.randint(3, 6))),
            'neighbors': neighbors
        }
        nodes.append(node)

    df = pd.DataFrame(nodes)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_dir + 'data.parquet')

    return Response(status=200)


@app.route('/nodes', methods=['DELETE'])
def delete_nodes():
    # Delete all parquet files in the data directory
    parquet_files = [file for file in os.listdir(
        parquet_dir) if file.endswith('.parquet')]

    for file in parquet_files:
        file_path = os.path.join(parquet_dir, file)
        os.remove(file_path)

    return Response(status=200)


# Start the server
if __name__ == '__main__':
    app.run()
