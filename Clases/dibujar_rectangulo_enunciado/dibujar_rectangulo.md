# DIBUJAR UN RECTÁNGULO

Modificar el programa dibujar_rectangulo.py para que los valores de ALTURA, ANCHO y ESTILO del rectángulo que se dibuja, puedan ser configurables a través de en un archivo de texto.

El archivo de configuración debe tener una única línea con el siguiente formato:

```
ALTO=25,ANCHO=35,ESTILO=3;30;43
```

## ACLARACIONES:

1. Si el archivo de configuración no existe, el programa debe funcionar con los valores por defecto.
2. En caso de haber archivo de configuración, no necesariamente tiene todos los parámetros configurados.
3. El archivo está siempre bien formado. Es decir, se respeta el formato:

```   
PARAMETRO1=VALOR1,PARAMETRO=VALOR2
```