import os.path
import morph_kgc as mkgc


data_source_type = "XML"
db_url = None # "mysql+pymysql://user:password@localhost:3306/db_name"
mappings_path = "/home/code/inesdata-map/test/data/input/mappings/gtfs-xml.rml.ttl"

output_path = "/home/code/inesdata-map/test/data/output/knowledge-graph-xml.nt"

def generate_graph(data_source_type: str, mappings_path: str, output_path: str, db_url: str=None):
    # Define config.ini content
    config = f"""
    [CONFIGURATION]
    logging_level: DEBUG
    output_file: {output_path}

    [DataSource{data_source_type}]
    mappings: {mappings_path}
    """
    # if input data source is DB, add its connection url
    if db_url:
        config += f"""
        db_url: {db_url}
        """

    # Generate knowledge graph
    if not os.path.exists(output_path):
        f = open(output_path, 'x')
    g = mkgc.materialize(config)
    g.parse(output_path)
    
    print(f'Knowledge Graph generated: {output_path}')

    
generate_graph(data_source_type, mappings_path, output_path, db_url)