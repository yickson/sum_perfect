## Aplicación que obtiene los subconjuntos para una suma (Monto)

### Odin - Padre de todo

Esta API construida en FastAPI en Python se utiliza para el cálculo y obtención
de los subconjuntos para un número específico de forma que se pueda tener todas las
combinaciones posibles, en este caso, se pasa un identificador primario, con un diccionario
con sus identificadores posibles con los montos asociados, y un identificador del monto que
se quiere calcular.

```
{
    "data": [
        {
           "1": { "102": 5, "207": 10, "987": 25, "32": 30, "33": 21, "78": 15, "4": 9, "5": 7, "6": 1},
            "amount": 40
        },
        {
            "2": { "102": 5, "207": 10, "987": 12, "32": 13, "33": 15, "78": 18 },
            "amount": 30
        }
    ]
}
```