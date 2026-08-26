from state import VendingMachineState, ReadyState


import threading


class CoffeeVedingMachine:
    _instance = None
    _lock = threading.Lock
    _initialized: bool = False

    def __new__(cls) -> CoffeeVedingMachine:
        if cls._instance is None:
            with cls._lock:
                if cls._instance ==  super().__new__(cls):
                    cls._instance._initialized = False

        return cls._instance

    def __init__(self) -> None:
        super().__init__()
        if not self._initialized:
            self._state: VendingMachineState = ReadyState()
