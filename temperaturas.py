# Promedio de temperatura en diferentes ciudades
temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 24},
            {"dia": "Martes", "temperatura": 28},
            {"dia": "Miércoles", "temperatura": 30},
            {"dia": "Jueves", "temperatura": 25},
            {"dia": "Viernes", "temperatura": 32},
            {"dia": "Sábado", "temperatura": 32},
            {"dia": "Domingo", "temperatura": 29}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 29},
            {"dia": "Martes", "temperatura": 30},
            {"dia": "Miércoles", "temperatura": 28},
            {"dia": "Jueves", "temperatura": 32},
            {"dia": "Viernes", "temperatura": 30},
            {"dia": "Sábado", "temperatura": 33},
            {"dia": "Domingo", "temperatura": 34}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 33},
            {"dia": "Martes", "temperatura": 31},
            {"dia": "Miércoles", "temperatura": 34},
            {"dia": "Jueves", "temperatura": 30},
            {"dia": "Viernes", "temperatura": 33},
            {"dia": "Sábado", "temperatura": 32},
            {"dia": "Domingo", "temperatura": 31}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temperatura": 28},
            {"dia": "Martes", "temperatura": 29},
            {"dia": "Miércoles", "temperatura": 33},
            {"dia": "Jueves", "temperatura": 30},
            {"dia": "Viernes", "temperatura": 29},
            {"dia": "Sábado", "temperatura": 27},
            {"dia": "Domingo", "temperatura": 30}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 16},
            {"dia": "Martes", "temperatura": 20},
            {"dia": "Miércoles", "temperatura": 18},
            {"dia": "Jueves", "temperatura": 16},
            {"dia": "Viernes", "temperatura": 15},
            {"dia": "Sábado", "temperatura": 17},
            {"dia": "Domingo", "temperatura": 19}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 20},
            {"dia": "Martes", "temperatura": 18},
            {"dia": "Miércoles", "temperatura": 19},
            {"dia": "Jueves", "temperatura": 16},
            {"dia": "Viernes", "temperatura": 16},
            {"dia": "Sábado", "temperatura": 15},
            {"dia": "Domingo", "temperatura": 16}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 14},
            {"dia": "Martes", "temperatura": 15},
            {"dia": "Miércoles", "temperatura": 12},
            {"dia": "Jueves", "temperatura": 13},
            {"dia": "Viernes", "temperatura": 10},
            {"dia": "Sábado", "temperatura": 14},
            {"dia": "Domingo", "temperatura": 12}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temperatura": 16},
            {"dia": "Martes", "temperatura": 15},
            {"dia": "Miércoles", "temperatura": 18},
            {"dia": "Jueves", "temperatura": 16},
            {"dia": "Viernes", "temperatura": 19},
            {"dia": "Sábado", "temperatura": 22},
            {"dia": "Domingo", "temperatura": 20}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"dia": "Lunes", "temperatura": 20},
            {"dia": "Martes", "temperatura": 22},
            {"dia": "Miércoles", "temperatura": 20},
            {"dia": "Jueves", "temperatura": 23},
            {"dia": "Viernes", "temperatura": 19},
            {"dia": "Sábado", "temperatura": 21},
            {"dia": "Domingo", "temperatura": 22}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temperatura": 18},
            {"dia": "Martes", "temperatura": 19},
            {"dia": "Miércoles", "temperatura": 22},
            {"dia": "Jueves", "temperatura": 24},
            {"dia": "Viernes", "temperatura": 23},
            {"dia": "Sábado", "temperatura": 24},
            {"dia": "Domingo", "temperatura": 20}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temperatura": 20},
            {"dia": "Martes", "temperatura": 16},
            {"dia": "Miércoles", "temperatura": 14},
            {"dia": "Jueves", "temperatura": 17},
            {"dia": "Viernes", "temperatura": 13},
            {"dia": "Sábado", "temperatura": 14},
            {"dia": "Domingo", "temperatura": 12}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temperatura": 15},
            {"dia": "Martes", "temperatura": 13},
            {"dia": "Miércoles", "temperatura": 12},
            {"dia": "Jueves", "temperatura": 14},
            {"dia": "Viernes", "temperatura": 16},
            {"dia": "Sábado", "temperatura": 13},
            {"dia": "Domingo", "temperatura": 14}
        ]
    ]
]

# Promedio de temperaturas de las ciudades en cada semana
ciudades = ["Guayaquil", "Quito", "Cuenca"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temperatura"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Temperatura promedio de {ciudades[ciudad_idx]} en la semana {semana_idx + 1}: {promedio:.2f} °C.")