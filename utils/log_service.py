import logging
import os

class LogService:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(__name__)
        
        # Si ya tiene configuración, no la volvemos a poner (evita logs duplicados)
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            # 1. Mostrar en Consola
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            # 2. Guardar en Archivo
            if not os.path.exists('logs'):
                os.makedirs('logs')
            
            # mode='w' borra el log anterior en cada ejecución. Usa 'a' si quieres acumular.
            file_handler = logging.FileHandler('logs/execution.log', mode='w') 
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger