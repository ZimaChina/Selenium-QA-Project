# Proyecto de Automatización QA con Selenium + Pytest
## 🧪 Selenium QA Automation Project

El repositorio contiene un proyecto de automatización de pruebas sobre la plataforma de[saucedemo.com](https://www.saucedemo.com), utilizando **Python**, **Selenium WebDriver**, y **Pytest**.

### 🔧 Tecnologías y herramientas utilizadas
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Esperas explícitas (`WebDriverWait`)
- Capturas automáticas en caso de error
- Estructura modular y escalable
- Pruebas manuales documentadas
- Preparado para integración continua (CI/CD)

### 📂 Estructura del repositorio
- `/tests`: scripts de pruebas automatizadas
- `/pages`: objetos de página para mantener el código limpio
- `/docs`: documentación de casos manuales, bugs y entorno
- `/screenshots`: capturas generadas en ejecuciones fallidas
- `conftest.py`: configuración de Pytest y WebDriver

### 🚀 Qué cubre actualmente
- Test de login exitoso
- Flujo completo de compra (selección, checkout y confirmación)
- Validación de elementos presentes y navegación correcta

### 📌 Próximos pasos (pendientes o en curso)
- Agregar más validaciones negativas
- Incluir pruebas sobre formularios inválidos
- Integrar con GitHub Actions para CI
- Reportes HTML (ej. `pytest-html` o Allure)

---

