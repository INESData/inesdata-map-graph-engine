# INESDATA-MAP: KG_GENERATION

**`kg_generation`** es un paquete de Python cuya finalidad es generar un grafo de conocimiento a partir de un fichero de mapeos en formato RML, junto con las fuentes de datos y las ontologías asociadas.

## Uso ▶️

Este paquete se ejecutaría de la siguiente forma:

```bash
python3 -m kg_generation -m data/input/mappings/gtfs-xml.rml.ttl -o data/output/knowledge-graph-xml.nt
```

o

```bash
python3 -m kg_generation -m data/input/mappings/gtfs-xml.rml.ttl -o data/output/knowledge-graph-xml.nt -db jdbc:mysql://localhost:3306/lubm4obda -dbu root -dbp root
```

Los argumentos son los siguientes:

- `mappings_path` [`-m`]: parámetro _obligatorio_ con la ruta al fichero de mapeos RML.
- `output_path` [`-o`]: parámetro _obligatorio_ con la ruta al grafo de conocimiento resultante.
- `db_url` [`-db`]: parámetro _opcional_ para indicar la URL de la base de datos en el caso de que la fuente sea una base de datos.
- `db_user` [`-dbu`]: parámetro _opcional_ para indicar el usuario de la base de datos en el caso de que la fuente sea una base de datos.
- `db_pass` [`-dbp`]: parámetro _opcional_ para indicar la contraseña de la base de datos en el caso de que la fuente sea una base de datos.
