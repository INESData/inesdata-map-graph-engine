import argparse
import os.path
import subprocess


def generate_graph(mappings_path: str, output_path: str, db_url: str=None, db_user: str=None, db_pass: str=None):
    # Define config.ini content
    config = f"""
    [CONFIGURATION]
    logging_level: DEBUG
    output_file: {output_path}
    """
    # if input data source is DB, add its connection url
    if db_url:
        db_driver, db_url_rest = db_url.split("://")
        if "mysql" in db_driver:
            db_driver = "mysql:pymysql"
        db_driver = db_driver.replace(":", "+")
        print(f"{db_driver}://{db_user}:{db_pass}@{db_url_rest}")
        config += f"""
    [DataSource]
    db_url: {db_driver}://{db_user}:{db_pass}@{db_url_rest}
    mappings: {mappings_path}
        """
    else:
        config += f"""
    [DataSource]
    mappings: {mappings_path}
        """
    print(config)
    # save config.ini file
    with open('config.ini', "w") as config_file:
        config_file.write(config)

    # Generate knowledge graph
    if not os.path.exists(output_path):
        f = open(output_path, 'x')
    # g = mkgc.materialize(config)
    # g.parse(output_path)
    proc = subprocess.run(["python3", "-m", "morph_kgc", 'config.ini'], check=True)
    
    print(f'Knowledge Graph generated: {output_path}')
    return proc.returncode

    
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--mappings_path', help='Mappings Path')
    parser.add_argument('-o', '--output_path', help='Output Path')
    parser.add_argument('-db', '--db_url', help='DB Connection URL')
    parser.add_argument('-dbu', '--db_user', help='DB Connection user')
    parser.add_argument('-dbp', '--db_pass', help='DB Connection password')

    args = parser.parse_args()
    mappings_path = args.mappings_path
    output_path = args.output_path
    db_url = args.db_url
    db_user = args.db_user
    db_pass = args.db_pass

    returncode = generate_graph(mappings_path, output_path, db_url, db_user, db_pass)
    print(f"exit code: {returncode}")
    
    return returncode
    
    
if __name__ == "__main__":
    main()
