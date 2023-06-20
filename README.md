# Parquet Demo

This is a small demo application consisting of a Python server using Parquet for data storage and a Quasar Vue frontend.

## Project Structure

```
/
  /data                # Parquet files
  /frontend            # Quasar Vue app
  /server              # Python server
```

## Preqrequisites

[Python3](https://www.python.org/downloads/)

[Node 16+](https://nodejs.org/en/download/)

## Running the Server

```
cd server
```

Install all dependencies

```
python3 -m pip install pyarrow pandas flask flask_cors
```

Start the server

```
python3 server.py
```

## Running the Frontend

```
cd frontend
```

Install all dependencies

```
npm i
```

Start the frontend

```
quasar dev
```
