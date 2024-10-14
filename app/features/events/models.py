from app import db


class Evento(db.Model):
    __tablename__ = 'eventos'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)

    def __repr__(self):
        return f'<Evento {self.titulo}>'
