"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig, table_finder

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="fast_agent",
    migrations_folder_path=os.path.join(
        os.path.dirname(CURRENT_DIRECTORY), "models", "migrations"
    ),
    table_classes=table_finder(modules=["models.task"], exclude_imported=True),
    migration_dependencies=[],
    commands=[],
)
