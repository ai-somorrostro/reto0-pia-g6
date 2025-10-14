

## 🪙 **METALIA** - Página Web Corporativa
Este repositorio contiene el código fuente y toda la documentación del sitio web corporativo de METALIA, una *consultora de inversión de élite especializada en el sector de los metales preciosos*.

---

## 🎯 Propósito y Finalidad del Proyecto
El objetivo principal de este proyecto es la creación de un sitio web profesional y moderno que sirva como la principal carta de presentación digital de **METALIA**. 

La web está diseñada para proyectar una imagen de:

*Seriedad y Experiencia*: A través de un diseño sobrio y contenido de valor.

*Modernidad*: Utilizando tecnologías actuales y animaciones fluidas.

*Confianza y Transparencia*: Ofreciendo información clara sobre el equipo, los servicios y el marco legal de la empresa.

---

## ✨ La Idea y el Concepto Creativo
La visión fue crear una experiencia de usuario inmersiva que reflejara la naturaleza del negocio de METALIA: el **lujo**, la **precisión** y el valor intrínseco de los *metales preciosos*.

Para lograrlo, el diseño se basa en los siguientes pilares:

🌃 *Tema Oscuro*: Un fondo elegante que transmite seriedad y permite que los elementos importantes destaquen.

⚜️ *Acentos Dorados*: Una paleta de colores inspirada en el oro y la plata para reforzar la identidad de la marca.

🏞️ *Fondo Fijo*: Una imagen de alta calidad que permanece fija, creando una sensación de profundidad y estabilidad.

✒️ *Tipografía Profesional*: Fuentes limpias y legibles, adecuadas para el sector financiero.

⚙️ Organización y Funcionamiento Técnico
La web ha sido construida utilizando un Generador de Sitios Estáticos, lo que garantiza máxima velocidad, seguridad y una gestión sencilla del contenido.

---

## **Herramientas Utilizadas**

🚀 *MkDocs*: El motor principal para generar la web, elegido por su simplicidad y potencia.
🎨 *El tema Material for MkDocs*: Uno de los temas más profesionales para MkDocs, que proporciona el diseño adaptable, las animaciones y las funcionalidades avanzadas.
🐍 *Python y venv*: Para gestionar las dependencias del proyecto de forma limpia y aislada.

---

## **Estructura de Carpetas**
El proyecto está organizado de la siguiente manera para facilitar su mantenimiento:

METALIA/

├── 📂 overrides/       # Plantillas HTML personalizadas (hero, footer, etc.)

├── 📂 docs/            # Todo el contenido visible de la web

│   ├── 🖼️ assets/      # Imágenes, logos y favicon

│   ├── 🎨 stylesheets/ # Hoja de estilos CSS personalizada (extra.css)

│   ├── 📈 analisis/    # Página de Análisis de Mercado

│   ├── ⚖️ legal/       # Páginas de Aviso Legal y Privacidad

│   └── ... (archivos .md de cada página principal)

├── 📦 venv/            # Entorno virtual de Python (ignorado por Git)

└── ⚙️ mkdocs.yml       # El cerebro del sitio: archivo principal de configuración

---

## 📋 **Prerrequisitos**

Antes de poder ejecutar el proyecto en tu máquina local, asegúrate de tener instaladas las siguientes herramientas esenciales en tu sistema.

### 1. Git

Es el sistema de control de versiones que utilizamos para gestionar el código y para desplegar el sitio en GitHub Pages.

*   **Cómo verificar si está instalado:**
    ```bash
    git --version
    ```
*   **Cómo instalarlo:**
    Puedes descargarlo desde su página oficial: **[git-scm.com](https://git-scm.com/downloads)**

### 2. Python 3

Es el lenguaje de programación sobre el que funciona MkDocs y todas sus dependencias. Se necesita una versión reciente.

*   **Requisito:** Python **3.8 o superior**.
*   **Cómo verificar si está instalado:**
    ```bash
    python3 --version
    ```
*   **Cómo instalarlo:**
    Puedes descargarlo desde su página oficial: **[python.org](https://www.python.org/downloads/)**

### 3. Módulo `venv` de Python

Es la herramienta estándar de Python para crear entornos virtuales aislados. Esto nos permite instalar las dependencias del proyecto de forma segura, sin afectar al sistema operativo.

*   **En la mayoría de los casos (Windows, macOS):** Este módulo ya viene incluido con la instalación de Python 3.
*   **En algunos sistemas Linux (como Debian/Ubuntu):** Puede que necesites instalarlo por separado.
    ```bash
    sudo apt update && sudo apt install python3-venv
    ```

---

💻 Cómo Ejecutar el Proyecto en **Local**
Para ver o modificar la web en un entorno de desarrollo, sigue estos pasos:
Clona el repositorio a tu máquina local.

**git clone** (repositorio SHH)

Navega a la carpeta del proyecto:

**cd reto0-pia-g6/METALIA/**

Crea y activa el entorno virtual de Python:

**python3 -m venv venv**

**source venv/bin/activate**

Instala las dependencias necesarias:

**pip install mkdocs mkdocs-material**

Inicia el servidor de desarrollo:

**mkdocs serve**

Abre tu navegador y ve a *http://127.0.0.1:8000* para ver la web en tiempo real.

---

🌐 Despliegue en GitHub Pages
La publicación de la web está automatizada. Con buscar el link:  ** github.com/ai-somorrostro/reto0-pia-g6/settings/pages ** Podras acceder a la pagina web ya subida en **GitHub Pages** de manera profesional.

---