import streamlit as st
import sqlite3
import pandas as pd
import os
from datetime import datetime

# Asumimos que ejecutamos el dashboard desde la raíz del proyecto
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB_PATH = os.path.join(PROJECT_ROOT, 'logs', 'antigravity.db')

st.set_page_config(
    page_title="Antigravity Observability",
    page_icon="🌌",
    layout="wide"
)

st.title("🛰️ Antigravity - Observabilidad de Agentes")
st.markdown("Dashboard de métricas generadas por las ejecuciones de los POE en el Proyecto Antigravity.")

if not os.path.exists(DB_PATH):
    st.warning(f"La base de datos aún no se ha creado en {DB_PATH}. Por favor, ejecuta un script utilizando el decorador `@log_execution`.")
else:
    try:
        conn = sqlite3.connect(DB_PATH)
        
        # Leer todos los logs
        df = pd.read_sql_query("SELECT * FROM execution_logs ORDER BY timestamp DESC", conn)
        
        if df.empty:
            st.info("La base de datos de logs está vacía. Esperando por las primeras ejecuciones del agente.")
        else:
            # Procesar datos
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            total_ejecuciones = len(df)
            exitos = len(df[df['status'] == 'SUCCESS'])
            errores = len(df[df['status'] == 'ERROR'])
            tasa_exito = round((exitos / total_ejecuciones) * 100, 1) if total_ejecuciones > 0 else 0
            
            # --- KPIs Globales ---
            st.header("Métricas Globales")
            kpi1, kpi2, kpi3, kpi4 = st.columns(4)
            kpi1.metric(label="Ejecuciones Totales", value=total_ejecuciones)
            kpi2.metric(label="Éxitos", value=exitos)
            kpi3.metric(label="Errores", value=errores)
            kpi4.metric(label="Tasa de Éxito", value=f"{tasa_exito}%")
            
            st.markdown("---")
            
            # --- Historial de Ejecuciones (Vista General) ---
            st.header("Historial Reciente de Ejecuciones")
            st.dataframe(
                df[['id', 'timestamp', 'script_name', 'function_name', 'status', 'duration_seconds']],
                use_container_width=True,
                hide_index=True
            )
            
            # --- Errores / Debug ---
            st.header("Vista de Error Stack Trace")
            df_errores = df[df['status'] == 'ERROR']
            
            if df_errores.empty:
                st.success("No hay errores recientes. Todos los sistemas funcionando sin problemas.")
            else:
                st.error(f"Se encontraron {len(df_errores)} errores.")
                for _, row in df_errores.head(10).iterrows():
                    with st.expander(f"🔴 Fallo en '{row['function_name']}' organizado en '{row['script_name']}' - {row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}"):
                        st.code(row['error_message'], language="python")
                        st.caption(f"Duración antes del fallo: {row['duration_seconds']:.2f}s")
            
    except Exception as e:
        st.error(f"Hubo un problema al procesar la base de datos de logs: {e}")
    finally:
        conn.close()
