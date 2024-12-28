from typing import Dict, Any, Optional

class Response:
    def __init__(self, success: bool, data: Optional[Dict[str, Any]] = None, error: Optional[str] = None):
        self.success = success
        self.data = data
        self.error = error
