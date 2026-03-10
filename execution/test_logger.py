import os
import sys

# Permitir importar utils desde el root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.logger import log_execution

@log_execution
def test_antigravity_agent():
    """Script de prueba para validar que el logger se está ejecutando correctamente y generando trazas."""
    print("[Agent Test] Inicializando tareas del agente...")
    
    # Simulando algún trabajo de procesamiento
    resultado = "Operación de prueba de Antigravity completada exitosamente."
    
    print(f"[Agent Test] {resultado}")
    return resultado

if __name__ == "__main__":
    test_antigravity_agent()
