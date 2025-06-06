from qdrant_client import QdrantClient
from typing import Optional
from xinference.client import Client as XinferenceClient

from src.core.config import QDRANT_CONFIG, XINFERENCE_CONFIG


class QdrantClientSingleton:
    _instance: Optional[QdrantClient] = None
    
    @classmethod
    def get_instance(cls) -> QdrantClient:
        if cls._instance is None:
            cls._instance = QdrantClient(
                url=QDRANT_CONFIG['URL'],
            )
        return cls._instance

class XinferenceClientSingleton:
    _instance: Optional[QdrantClient] = None
    
    @classmethod
    def get_instance(cls) -> XinferenceClient:
        if cls._instance is None:
            cls._instance = XinferenceClient(
                url=XINFERENCE_CONFIG['URL'],
            )
        return cls._instance

def get_qdrant_client() -> QdrantClient:
    return QdrantClientSingleton.get_instance()

def get_xinference_client() -> XinferenceClient:
    return QdrantClientSingleton.get_instance()

