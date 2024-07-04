# Proyecto_Fundamentos_Rob

## Diseño de robot manipulador de 7 grados de libertad tomando como referencia el robot ES200RDII

El proyecto del curso consiste en diseñar un robot manipulador serial con alguna estructura cinemática de al menos 6 grados de libertad. Se puede tomar como base la estructura de algún robot existente, brindándole algunas características distintivas, o se puede realizar un diseño de cero. Este robot debe ser luego modelado y controlado. Todo el sistema debe ser implementado usando ROS.

El proyecto tiene 2 partes: el reporte escrito (80 %) y la presentación oral (20 %). Las partes que debe contener el reporte escrito, con su puntaje, son las siguientes:

### [1 pt] Introducción. 

Debe contener una introducción general al robot que se está usando, indicando características y posibles aplicaciones del mismo.

### [2 pt] Componentes. 

Debe contener una descripción detallada de qué componentes utilizaría el robot si fuese implementado de manera real. Debe incluirse la estructura mecánica, el sistema de percepción, la actuación (y transmisión, de ser aplicable), así como los elementos que conformarían el sistema de control.

### [3 pt] Modelo del robot. 

Debe presentar el modelo del robot en RViz y Gazebo.

Se debe visualizar el diseño realizado (un boceto inicial mostrando el dimensionado del robot), y el robot en URDF. Lo mínimo necesario es usar figuras geométricas básicas de RViz, pero con los parámetros de la cadena cinemática diseñada para el robot (1 punto).

El incluir enmallado (mesh) para las partes del robot tiene un peso de 1 punto.
La simulación con Gazebo tiene un peso de 1 punto. Para tener puntaje completo se debe demostrar la funcionalidad del modelo (movimiento articular básico) con imágenes o con algún video.

### [4 pt] Cinemática directa e inversa

Se debe mostrar el modelamiento cinemático (usando el método geométrico o Denavit-Hartenberg), así como algunas configuraciones esperadas y obtenidas a partir del modelo cinemático. La verificación debe, al menos, realizarse usando RViz (2 puntos).

Se puede utilizar cualquier método para el cálculo de la cinemática inversa. Se debe mostrar cómo se implementó, verificando la validez para diferentes configuraciones (2 puntos). Para tener puntaje completo, en el caso de usar un método numérico, se debe incluir gráficos que muestren la convergencia del algoritmo en diferentes configuraciones.

### [4 pt] Control Cinemático

Se debe obtener el modelo cinemático diferencial del robot, mostrando claramente el procedimiento seguido para el cálculo de los Jacobianos que sean relevantes. Se debe indicar matemáticamente cómo se llegó al Jacobiano (justificar el cálculo numérico con ecuaciones). Se debe, además, indicar las posibles configuraciones singulares del robot (2 puntos).

Se debe implementar control cinemático verificando el movimiento con RViz a través de la visualización y de gráficos que muestren el funcionamiento adecuado para diferentes casos. Por facilidad, se puede solo hacer control de posición (2 puntos).

### [3 pt] Dinámica y Control Dinámico

Se debe mostrar de manera detallada el procedimiento seguido para el cálculo de la dinámica del robot. Se recomienda indicar un ejemplo de la matriz M, C, g obtenidas para al menos una configuración particular, indicando dicha configuración. Se puede utilizar algún paquete como RBDL (1 punto).

Debe implementarse dos esquemas de control dinámico para el robot, mostrando la descripción teórica y pruebas de movimiento con RViz y/o Gazebo. Se debe, además, incluir figuras que muestren el comportamiento del sistema sin control y con control (2 puntos) .

### [1 pt] Conclusiones y Recomendaciones

### [1 pt] Anexo: código impementado. Se debe incluir el código comentado de las partes más importantes implementados (no de todos los programas). De manera alternativa, se puede incluir el enlace de un repositorio de github creado para el proyecto (en este caso debe indicarse claramente qué archivo implementa qué parte).

Para cada figura utilizada se debe tener algún comentario pertinente: no basta con incluir la figura, sino que hay que indicar qué se muestra en dicha figura. Además, la adecuada redacción, ortografía y orden tendrá un peso de 1 punto. Para la redacción, cada figura y tabla debe tener un título y numeración (Tabla 1, Figura 1), y deben ser referenciadas desde el texto. El reporte se puede presentar en cualquier formato: como reporte (en una sola columna) o como artículo (en 2 columnas).

La presentación oral debe seguir un esquema similar al del reporte, mostrando las partes que se considere más importantes. La duración será de máximo 15 minutos por grupo y todos los integrantes deben realizar alguna parte de la presentación.

Las presentaciones se realizarán durante la semana 15 y la semana 16.

Hasta antes del inicio de las presentaciones, cada integrante de cada grupo debe enviarme un correo personal indicando el nivel de compromiso y trabajo de sus demás compañeros de grupo, en una escala de 0 a 10, donde 0 es el mínimo valor ("no hizo nada") y 10 es el máximo valor ("hizo todo lo requerido de la mejor manera posible"). Esta evaluación no será revelada a los demás miembros del grupo y se utilizará para ponderar la nota individual de cada integrante. 
