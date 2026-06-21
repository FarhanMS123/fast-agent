from piccolo_conf import *  # noqa

DB = PostgresEngine(
    config={
        "database": "fast-agent_test",
        "user": "postgres",
        "password": "",
        "host": "localhost",
        "port": 5432,
    }
)
