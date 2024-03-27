class Vector3:
    def __init__(self, x=0, y=0, z=0):
        # Konstruktor, initialisiert die Koordinaten x, y und z mit Standardwerten (0 oder den übergebenen Werten)
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        # Diese Methode wird aufgerufen, wenn str() auf ein Vector3-Objekt angewendet wird.
        # Gibt eine formatierte Zeichenkette zurück, die die Koordinaten des Vektors enthält.
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        # Diese Methode wird aufgerufen, wenn ein Vector3-Objekt mit einem anderen Objekt addiert wird.
        # Rückgabe eines neuen Vector3-Objekts mit den summierten Koordinaten.
        return Vector3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        # Diese Methode wird aufgerufen, wenn ein Vector3-Objekt von einem anderen Objekt subtrahiert wird.
        # Rückgabe eines neuen Vector3-Objekts mit den subtrahierten Koordinaten.
        return Vector3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        # Diese Methode wird aufgerufen, wenn ein Vector3-Objekt mit einem anderen Objekt multipliziert wird.
        if type(other) == Vector3:
            # Komponentenweise Multiplikation mit einem anderen Vector3-Objekt.
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif type(other) == float or type(other) == int:
            # Multiplikation jedes Attributes mit einem Skalar.
            return Vector3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        # Diese Methode wird aufgerufen, wenn ein anderes Objekt mit einem Vector3-Objekt multipliziert wird.
        # Hier wird die rechtsseitige Multiplikation unterstützt.
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def dot(self, other):
        # Diese Methode berechnet das Skalarprodukt mit einem anderen Vektor.
        return Vector3(self.x * other, self.y * other, self.z * other)

    def cross(self, other):
        # Diese Methode berechnet das Kreuzprodukt mit einem anderen Vektor.
        # Die Rückgabe ist ein Tupel der Ergebnisse der Kreuzproduktberechnung.
        return (self.y*other.z - self.z*other.y), (self.z*other.x - self.x*other.z), (self.x*other.y - self.y*other.x)

    def magnitude(self):
        # Diese Methode berechnet die Länge (Magnitude) des Vektors.
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def normalize(self):
        # Diese Methode normalisiert den Vektor.
        # Zunächst wird die Länge des Vektors berechnet.
        r = self.magnitude()
        # Dann werden die Koordinaten des Vektors durch die Länge geteilt, um den normalisierten Vektor zu erhalten.
        return Vector3(self.x / r, self.y / r, self.z / r)


a = Vector3(3,4,2)
b = Vector3(2,1,0)
 
