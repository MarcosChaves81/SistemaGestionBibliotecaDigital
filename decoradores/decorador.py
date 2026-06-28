import functools 

def anunciar_accion(accion):
    def decorador(funcion):
        @functools.wraps(funcion) 
        def envoltorio(self, *args, **kwargs):
            resultado = funcion(self, *args, **kwargs)
            
            tipo_objeto = self.__class__.__name__.replace("Gestion", "")
            
            admin = kwargs.get('admin', args[0] if args else "Sistema")
            
            print(f"[ANUNCIO]: Se {accion} un {tipo_objeto} por el admin [{admin}].")
            
            return resultado
        return envoltorio
    return decorador