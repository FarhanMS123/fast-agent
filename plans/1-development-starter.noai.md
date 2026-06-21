# Development Starter

```sh
python -m venv .venv\nsource .venv/bin/activate
pip install 'piccolo[all]'
mkdir src
piccolo asgi new --root=src --name=fast-agent
# fastapi, uvicorn
git update-ref -d HEAD
git config --global -l
LESS="-iRFXMx4" git config --global -l
```

- vscode:python.analysis.typeCheckingMode