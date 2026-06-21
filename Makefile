PICCOLO = PYTHONPATH=src PICCOLO_CONF=config.piccolo_conf .venv/bin/piccolo
APP = fast_agent

.PHONY: migrations migrate

# Generate an auto migration for the app
migrations:
	$(PICCOLO) migrations new $(APP) --auto

# Apply all pending migrations (app + admin/user/session_auth)
migrate:
	$(PICCOLO) migrations forwards all
