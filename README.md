# INESDATA-MAP: KG-GENERATION

**`kg-generation`** es un paquete de Python cuya finalidad es generar un grafo de conocimiento a partir de un fichero de mapeos en formato RML, junto con las fuentes de datos y las ontologías asociadas.

## Uso ▶️

Este paquete se ejecutaría de la siguiente forma:

```bash
python3 -m kg_generation -dt XML -m data/input/mappings/gtfs-xml.rml.ttl -o data/output/knowledge-graph-xml.nt
```

Los argumentos son los siguientes:

- `data_source_type`: parámetro _obligatorio_ con el tipo de datos de la fuente de datos. Los valores que puede tomar son: `XML`, `CSV`, `JSON`, `DB`.
- `mappings_path`: parámetro _obligatorio_ con la ruta al fichero de mapeos RML.
- `mappings_path`: parámetro _obligatorio_ con la ruta al grafo de conocimiento resultante.
- `db_url`: parámetro _opcional_ para indicar la cadena de conexión a la base de datos en el caso de que la fuente de datos sea de tipo `DB`.
