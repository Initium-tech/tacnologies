# Directiva: Generación de Landing Page para Tacnologies

## Objetivo
Crear una landing page moderna, funcional y responsiva para la empresa de consultoría Tacnologies, especializada en Managed IT & Technology Services.

## Entradas (Inputs)
- **Idioma**: Español.
- **Tono**: Profesional, tecnológico y confiable.
- **Identidad Visual**:
  - Primario: `#004A99` (Royal Blue)
  - Acento: `#00A2E0` (Sky Blue)
  - Fondo Dark: `#0F172A` (Slate 900)
  - Fondo Light: `#F8FAFC` (Slate 50)
- **Contenido**:
  - Eslogan: "Empowering Digital Transformation. Soluciones IT simples, confiables y seguras diseñadas para el crecimiento."
  - Propuesta: "Gestionamos su IT para que usted pueda dirigir su negocio."
  - Servicios: Cloud & Gestión, Backup, Consultoría IT.
  - Compromiso: Talento local, sostenibilidad, diversidad.
  - Contacto: 787-508-6578, info@tacnologies.com, www.tacnologies.com
- **Recursos Técnicos**:
  - Logo S3/CloudFront: `https://d12345.cloudfront.net/customerwebpages/tacnologies-assets/tacnologieslogo.png`
  - Framework: Tailwind CSS.

## Salidas (Outputs)
- Un archivo de script en la capa de ejecución: `execution/generate_tacnologies_site.py`.
- Un archivo HTML generado por el script: `index.html`.

## Funcionalidades Dinámicas
- Interruptor de Modo Claro / Modo Oscuro.
- Diseño 100% responsivo (Mobile, Tablet, Desktop).
- Uso de gradientes lineales para escalabilidad y modernidad.

## Reglas de Ejecución
- El script debe importar y usar `@log_execution` de `utils.logger`.
- El script debe ser determinista y registrar su éxito o falla en `logs/antigravity.db`.
