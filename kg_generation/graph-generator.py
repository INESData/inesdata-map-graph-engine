import os.path
import morph_kgc as mkgc
import subprocess
import argparse


config_path = "/home/code/inesdata-map/kg-generation/inesdata_map/config.ini"
data_source_type = "XML"
db_url = None # "mysql+pymysql://user:password@localhost:3306/db_name"
mappings_path = "/home/code/inesdata-map/kg-generation/inesdata_map/data/input/mappings/gtfs-xml.rml.ttl"

output_path = "/home/code/inesdata-map/kg-generation/inesdata_map/data/output/knowledge-graph-xml.nt"


def generate_graph(config_path: str, data_source_type: str, mappings_path: str, output_path: str, db_url: str=None):
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
    # save config.ini file
    with open(config_path, "w") as config_file:
        config_file.write(config)

    # Generate knowledge graph
    if not os.path.exists(output_path):
        f = open(output_path, 'x')
    # g = mkgc.materialize(config)
    # g.parse(output_path)
    subprocess.run(["python3", "-m", "morph_kgc", config_path])
    
    print(f'Knowledge Graph generated: {output_path}')

    
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--config_path', help='Config Path')
    parser.add_argument('-dt', '--data_source_type', help='Data Source Type', choices=["XML", "CSV", "JSON", "DB"])
    parser.add_argument('-m', '--mappings_path', help='Mappings Path')
    parser.add_argument('-o', '--output_path', help='Output Path')
    parser.add_argument('-db', '--db_url', help='DB Connection Settings')

    args = parser.parse_args()
    config_path = args.config_path
    data_source_type = args.data_source_type
    mappings_path = args.mappings_path
    output_path = args.output_path
    db_url = args.db_url

    generate_graph(config_path, data_source_type, mappings_path, output_path, db_url)
    
    
if __name__ == "__main__":
    main()