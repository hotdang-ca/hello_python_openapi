# Python FastAPI + OpenAPI/Swagger

## What

This is just a sample Python FastAPI application which allows me to practice my FastAPI /w OpenAPI/Swagger autogen.

## How

1. Create a python 3.10+ environment:
   ```bash
   python3.1x -m venv venv
   ```

2. Activate your VENV
   ```bash
   source ./venv/bin/activate
   ```

3. Install requirements INTO the venv
   ```bash
   pip install -r requirements.txt
   ```

4. Run FastAPI (optionally with auto-reload):
   ```
   uvicorn app:app --reload
   ```

You now have a running FastAPI, with auto-generated SwaggerUI at `http://127.0.0.1:5000/docs`

## Who

(c) 2026, James Robert Perih, Four And A Half Giraffes, Ltd. 