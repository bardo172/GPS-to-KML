import simplekml

# Crear el objeto KML
kml = simplekml.Kml()

# Lista de coordenadas con nombre y latitud, longitud
coordinates = [
    ("Calle 2: P 8 D", 10.515365, -84.9981983333333),
    ("Calle 2: P 7 D", 10.5154133333333, -84.99789),
    ("Calle 2: P 6 D", 10.51531, -84.9977816666667),
    ("Calle 2: P 5 D", 10.51512, -84.9975716666667),
    ("Calle 2: P 3 D", 10.5145916666667, -84.9970983333333),
    ("Calle 2: P 4 D", 10.51474, -84.9975633333333),
    ("Calle 2: P 2 D", 10.5144616666667, -84.9966916666667),
    ("Calle 2: P 1 D", 10.5144, -84.9965516666667),
    ("Calle 2: P 9 D", 10.5140083333333, -84.99657),
    ("Calle 2: P 10 D", 10.5135083333333, -84.9961533333333),
    ("Calle 2: P Inicial", 10.51334, -84.9958666666667)
]

# Agregar puntos al KML
for name, lat, lon in coordinates:
    pnt = kml.newpoint(name=name, coords=[(lon, lat)])

# Guardar el archivo KML
kml.save("coordinates.kml")
