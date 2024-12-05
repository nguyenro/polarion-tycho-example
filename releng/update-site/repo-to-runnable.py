import os
import argparse
import zipfile
from pathlib import Path
import shutil

def extract_manifest(jar_path):
    with zipfile.ZipFile(jar_path, 'r') as jar:
        try:
            with jar.open('META-INF/MANIFEST.MF') as manifest_file:
                for line in manifest_file:
                    decoded_line = line.decode('utf-8').strip()
                    if decoded_line.startswith("Eclipse-BundleShape:"):
                        return decoded_line.split(":")[1].strip()
        except KeyError:
            return None
    return None

def process_jar(jar_path, destination_folder):
    bundle_shape = extract_manifest(jar_path)
    jar_name = os.path.basename(jar_path)

    if bundle_shape == "dir":
        target_path = os.path.join(destination_folder, jar_name.replace(".jar", ""))
        os.makedirs(target_path, exist_ok=True)
        with zipfile.ZipFile(jar_path, 'r') as jar:
            jar.extractall(target_path)
        print(f"Unpacked {jar_name} to {target_path}")
    else:
        target_path = os.path.join(destination_folder, jar_name)
        shutil.copy(jar_path, target_path)
        print(f"Copied {jar_name} to {target_path}")

def main():
    parser = argparse.ArgumentParser(description="Unpack plugins based on Eclipse-BundleShape property")
    parser.add_argument('--source', required=True, help="Path to repository plugins folder")
    parser.add_argument('--destination', required=True, help="Path to target folder with plugins in runnable form")
    args = parser.parse_args()

    source_folder = args.source
    destination_folder = args.destination

    os.makedirs(destination_folder, exist_ok=True)

    for jar_file in Path(source_folder).glob("*.jar"):
        process_jar(jar_file, destination_folder)

    print("Processing completed.")

if __name__ == "__main__":
    main()
