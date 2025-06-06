from functools import lru_cache
from typing import Dict, Type

from .settings.base import BaseAppSettings, AppEnvTypes
from .settings.app import AppSettings
from .settings.dev import DevAppSettings
from .settings.prod import ProdAppSettings


environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.prod: ProdAppSettings, 
    AppEnvTypes.dev: DevAppSettings
}


@lru_cache() 
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    
    return config()


env_config = get_app_settings().env_configs

QDRANT_CONFIG = env_config['STORAGE']['QDRANT']
NEO4J_CONFIG = env_config['STORAGE']['NEO4J']
XINFERENCE_CONFIG = env_config['STORAGE']['XINFERENCE']
MINIO_CONFIG = env_config['STORAGE']['MINIO']

URL_BACKEND_API = env_config['REQUEST']['BACKEND_API']['URL']