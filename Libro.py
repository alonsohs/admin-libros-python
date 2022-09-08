class Libro(object):
    def __init__(self, id, titulo, autor, editorial):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial

    def __str__(self):
        return "%s - %s - %s - %s" % (self.id, self.titulo, self.autor, self.editorial)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)
