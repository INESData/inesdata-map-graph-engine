import os.path
import morph_kgc as mkgc
import subprocess
import argparse


def generate_graph(mappings_path: str, output_path: str, db_url: str=None):
    # Define config.ini content
    config = f"""
    [CONFIGURATION]
    logging_level: DEBUG
    output_file: {output_path}

    [DataSource]
    mappings: {mappings_path}
    """
    # if input data source is DB, add its connection url
    if db_url:
        config += f"""
        db_url: {db_url}
        """
    # save config.ini file
    with open('config.ini', "w") as config_file:
        config_file.write(config)


    # Generate knowledge graph
    if not os.path.exists(output_path):
        f = open(output_path, 'x')
    # g = mkgc.materialize(config)
    # g.parse(output_path)
    subprocess.run(["python3", "-m", "morph_kgc", 'config.ini'])
    
    # print(f'Knowledge Graph generated: {output_path}')

    
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--mappings_path', help='Mappings Path')
    parser.add_argument('-o', '--output_path', help='Output Path')
    parser.add_argument('-db', '--db_url', help='DB Connection Settings')

    args = parser.parse_args()
    mappings_path = args.mappings_path
    output_path = args.output_path
    db_url = args.db_url

    generate_graph(mappings_path, output_path, db_url)
    
    
if __name__ == "__main__":
    main()