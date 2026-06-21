import os

os.environ.setdefault("PICCOLO_CONF", "config.piccolo_conf")

if __name__ == "__main__":

    import uvicorn

    uvicorn.run("api.app:app", app_dir="src", reload=True)
