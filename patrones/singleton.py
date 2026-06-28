class Singleton:
    _instance = None
    _init_args = None
    _init_kwargs = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._init_args = args
            cls._init_kwargs = kwargs
            print(f" Instancia única creada para la clase '{cls.__name__}'.")
        else:
            # Si ya existe, comparamos si intentan cambiar los parámetros
            if cls._init_args != args or cls._init_kwargs != kwargs:
                print(f" Ya existe una instancia activa de '{cls.__name__}'.")
                print(f" Se ignoraron los nuevos parámetros {args} {kwargs} y se reutilizará la original.")
            else:
                print(f"  Reutilizando instancia existente de '{cls.__name__}'.")
        
        return cls._instance

    def __init__(self, *args, **kwargs):
        if hasattr(self, '_inicializado'):
            return
        self._inicializado = True
        super().__init__()
