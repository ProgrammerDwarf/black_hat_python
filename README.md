# Black Hat Python (2nd Edition) - Laboratorio y Notas de Estudio

Este repositorio recopila mis notas técnicas, ejercicios prácticos y adaptaciones de código realizadas durante el estudio del libro **[Black Hat Python, 2nd Edition](https://nostarch.com/black-hat-python2E/)** de **Justin Seitz** y **Tim Arnold** (No Starch Press, 2021).

El objetivo del proyecto es puramente formativo: profundizar en conceptos de redes, seguridad ofensiva/defensiva y programación de herramientas en Python 3.

---

## 🛠️ Entorno de Trabajo y Tecnologías

A diferencia de la configuración sugerida en el libro (Kali Linux como máquina host/VM principal), muchas de las prácticas se adaptaron para ejecutarse en el siguiente entorno:

- **Sistema Operativo:** Windows 10
- **Editor / IDE:** Visual Studio Code (con extensiones oficiales de Python)
- **Lenguaje:** Python 3.12>=
- **Librerías principales exploradas:** `socket`, `argparse`, `subprocess`, `shlex`, `threading`, `sys`, entre otras.

---

## 📂 Estructura del Repositorio

- `capitulo_1/` / `networking_basics/`: Clientes y servidores TCP/UDP, exploración de sockets y puertos efímeros.
- `capitulo_2/` / `netcat_tool/`: Reimplementación en Python de la utilidad Netcat (modos cliente/servidor, manejo de buffers y ejecución de comandos).
- *(Carpetas sucesivas según el avance en los capítulos)*

---

## 📌 Modificaciones y Aportes Personales

Con el fin de consolidar el aprendizaje y adaptar los ejemplos a mi flujo de trabajo:
- Se adaptaron directivas de red específicas de Windows (por ejemplo, resolución de direcciones locales `127.0.0.1` vs. bindings `0.0.0.0`).
- Se añadieron comentarios explicativos detallados en el código sobre el flujo de ejecución, manejo de procesos y opciones de sockets (`SO_REUSEADDR`, tuberías/pipes, etc.).
- Se implementaron mejoras en el manejo de excepciones y formato de salida por consola.

---

## ⚖️ Aviso Legal y Atribución (Disclaimer)

- **Derechos de Autor:** El código base y la estructura conceptual de los ejercicios pertenecen a **Justin Seitz, Tim Arnold** y **No Starch Press, Inc.** (Copyright © 2021). Todos los derechos reservados por sus respectivos titulares.
- **Uso Justo / Fines Educativos:** Este repositorio no pretende redistribuir comercialmente el contenido del libro, sino servir como un registro de estudio personal y portafolio de aprendizaje técnico bajo los principios de uso legítimo con fines académicos (*Fair Use*).
- **Código Fuente Oficial:** Los ejemplos oficiales proporcionados por la editorial pueden encontrarse en el sitio de No Starch Press: [nostarch.com/black-hat-python2E/](https://nostarch.com/black-hat-python2E/).