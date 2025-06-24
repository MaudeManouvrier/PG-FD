import subprocess #to execute functional_dependencies

def run_functional_dependencies():
     result = subprocess.run(["python", "functional_dependencies.py"])

def run_PG_FD():
    subprocess.run(["python", "PGFDPrototypeV2.py"], check=True)

if __name__ == "__main__":
    run_functional_dependencies()
    run_PG_FD()