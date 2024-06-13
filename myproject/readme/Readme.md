# Proyecto Django - Cervecería

## Descripción

Este proyecto Django es una aplicación web diseñada para consultar y mostrar cervecerías de diferentes países utilizando la API de Open Brewery DB. La aplicación permite a los usuarios filtrar cervecerías por país y ciudad, mostrando los resultados en una tabla HTML. La interfaz está diseñada utilizando Bootstrap para mejorar la apariencia y la usabilidad.

## Funcionalidades

- Consulta de cervecerías utilizando la API de Open Brewery DB.
- Filtro de cervecerías por país y ciudad.
- Visualización de resultados en una tabla HTML.
- Interfaz responsiva y amigable utilizando Bootstrap.

## API Utilizada

### Open Brewery DB

La aplicación utiliza la API de Open Brewery DB (https://www.openbrewerydb.org/) para obtener datos de cervecerías. Open Brewery DB es una API pública que proporciona información detallada sobre cervecerías en todo el mundo, incluyendo nombres, tipos, ubicaciones y más.

## Codigo

Configuración de Plantillas

En el archivo settings.py, se configuró la ruta a la carpeta de plantillas para que Django pueda encontrar y renderizar las plantillas correctamente. La carpeta templates se encuentra en la raíz del proyecto y contiene subcarpetas específicas para cada aplicación.

Vistas y URLs

La vista principal (breweries_view) se encuentra en el archivo views.py de la aplicación breweries. Esta vista se encarga de realizar la consulta a la API de Open Brewery DB y de renderizar los resultados en una plantilla HTML (breweries.html). La URL para esta vista se configura en el archivo urls.py de la aplicación breweries.

Plantilla HTML

La plantilla breweries.html utiliza Bootstrap para proporcionar una interfaz de usuario atractiva y responsiva. La plantilla incluye un formulario para filtrar cervecerías por país y ciudad, y una tabla para mostrar los resultados.

Conclusión

Este proyecto demuestra cómo crear una aplicación web simple utilizando Django, con una API externa y mostrar los datos en una interfaz de usuario atractiva. La API de Open Brewery DB proporciona los datos necesarios para la aplicación, y el uso de Bootstrap mejora la experiencia del usuario.
