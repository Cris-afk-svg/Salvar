# errors.py

# Lista de mensajes de error
ERROR_MESSAGES = [
    {"code": 1000, "message": "Caracter no identificado"},
    {"code": 1001, "message": "Los identificadores deben llevar al menos una letra"},
    {"code": 1002, "message": "Los identificadores no pueden empezar con número"},
    {"code": 1003, "message": "Al < solo le puedes concatenar un ="},
    {"code": 1004, "message": "Al <= no le puedes concatenar [<,>,=,!]"},
    {"code": 1005, "message": "Al > solo le puedes concatenar un ="},
    {"code": 1006, "message": "Al >= no le puedes concatenar [<,>,=,!]"},
    {"code": 1007, "message": "Al = solo le puedes concatenar un ="},
    {"code": 1008, "message": "Al == no le puedes concatenar [<,>,=,!]"},
    {"code": 1009, "message": "Al ! solo le puedes concatenar un ="},
    {"code": 1010, "message": "Al != no le puedes concatenar [<,>,=,!]"},
    {"code": 1011, "message": "El & solo puede ir como &&"},
    {"code": 1012, "message": "El && no puede llevar más & concatenados"},
    {"code": 1013, "message": "El | solo puede ir como ||"},
    {"code": 1014, "message": "El || no puede llevar más | concatenados"},
    {"code": 1015, "message": "El ++ no puede llevar + concatenado"},
    {"code": 1016, "message": "El -- no puede llevar - concatenado"},
    {"code": 1017, "message": "El lenguaje solo soporta enteros, favor de solo concatenar números del 0-9"},
    {"code": 1018, "message": "El programa no debe acabar con una cadena abierta"},
]

def process_errors(errors):
    """
    Procesa la lista de errores y agrega mensajes descriptivos a cada error.

    :param errors: Lista de errores encontrados (con código, línea, columna, etc.).
    :return: Lista de errores con mensajes descriptivos.
    """
    return [
        {
            "code": error["code"],
            "line": error["line"],
            "col": error["col"],
            "message": next(
                (msg["message"] for msg in ERROR_MESSAGES if msg["code"] == error["code"]),
                "Error desconocido"
            ),
            "place": error.get("place", "")
        }
        for error in errors
    ]
