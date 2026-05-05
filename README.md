# 🏙️ Sistema de Reportes Ciudadanos

Sistema en Python que permite a ciudadanos reportar incidentes urbanos (luminarias dañadas, basura, ruidos molestos, etc.) con protección de datos personales integrada.

## ✨ Funcionalidades

- Registro de incidentes con validación y sanitización de datos
- Anonimización automática de nombre y correo
- Generación de ID único por reporte
- Visualización de reportes con correo enmascarado

## 🔒 Seguridad y privacidad

- El nombre del ciudadano **nunca se almacena directamente** — se reemplaza por un seudónimo
- El correo se **enmascara** al mostrarse (`u***@dominio.com`)
- Se mantiene un respaldo interno separado para cruzar datos si es necesario
- Todos los campos pasan por sanitización con expresiones regulares

## 📋 Campos del reporte

| Campo | Validación |
|---|---|
| Nombre | Solo letras y espacios |
| Correo | Formato válido de email |
| Tipo de incidente | Solo letras |
| Descripción | Máximo 30 caracteres, sin caracteres especiales |
| Ubicación | Letras, números, puntos y comas |

## ▶️ Uso

```bash
python reporte_ciudadano.py
```

Menú de opciones:
