# FAST API APP

- Implementation of JWT authentication
- Used mongodb ('beanie')

## Environment variables

1. Create a `.env` file in `app/` directory

2. Populate with the following variables

    ```sh
    JWT_SECRET_KEY=thisisaauthfastapiapp

    JWT_REFRESH_SECRET_KEY=thisisaauthfastapiapp

    MONGO_CONNECTION_STRING=mongodb://localhost:27017 

    PORT=8000
    ```

## Installation using Poetry

1. Install [poetry](https://python-poetry.org/docs/)
2. To install dependencies

    ```sh
    poetry install
    ```

    Note: This will also create a virtual environment

3. To start app

    ```sh
    poetry run python -m app
    ```

Note: You can test endpoints via Swagger docs at `/docs`
