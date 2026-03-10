import sqlite3
import datetime
import functools
import traceback
import os
import inspect

# La base de datos estará en la carpeta logs/
# Desde utils/, asumimos que el root del proyecto está un nivel arriba.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB_PATH = os.path.join(PROJECT_ROOT, 'logs', 'antigravity.db')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS execution_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            script_name TEXT,
            function_name TEXT,
            status TEXT,
            error_message TEXT,
            duration_seconds REAL,
            tokens_used INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Inicializamos la base de datos la primera vez que se importa el logger
init_db()

def log_execution(func):
    """
    Decorador obligatorio para todos los scripts de ejecución en la capa 3.
    Registra automáticamente el inicio, fin, estado (SUCCESS/ERROR) y duración de la ejecución.
    Para reportar "tokens", el script debería tener una forma de inyectarlo, pero por defecto puede ser nulo.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        status = 'SUCCESS'
        error_message = ''
        
        # Intentamos obtener el nombre del script donde se ejecutó
        script_name = inspect.getmodule(func).__name__ if inspect.getmodule(func) else "unknown"
        function_name = func.__name__

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            status = 'ERROR'
            error_message = f"{str(e)}\n\n{traceback.format_exc()}"
            raise e
        finally:
            end_time = datetime.datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            # Guardamos el registro en la base de datos (Operación Determinista)
            try:
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO execution_logs (timestamp, script_name, function_name, status, error_message, duration_seconds)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (start_time.isoformat(), script_name, function_name, status, error_message, duration))
                conn.commit()
            except Exception as db_err:
                print(f"Error escribiendo logger en {DB_PATH}: {db_err}")
            finally:
                if 'conn' in locals():
                    conn.close()

    return wrapper
