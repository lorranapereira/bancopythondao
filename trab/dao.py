class DaoDepartamento:
    
    def inserir(self):
        cur.execute("insert into departamento (nome) values (%s)",["guilherme"])
        con.commit()
   