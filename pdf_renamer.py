import os
import json
import re
from pathlib import Path

def load_config(config_file="variables.json"):
    """Load configuration from JSON file"""
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: {config_file} not found. Please create it first.")
        return None
    except json.JSONDecodeError:
        print(f"Error: {config_file} is not valid JSON.")
        return None

def rename_pdfs(folder_path, prefix="S", year="2020"):
    """
    Rename PDFs in folder to format: PREFIX_SERIALNUMBER_YEAR_ORIGINALNAME.pdf
    
    Args:
        folder_path (str): Path to folder (Windows or Unix)
        prefix (str): Single letter prefix (default "S")
        year (str): Year to add (default "2020")
    """
    
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder not found: {folder_path}")
        return
    
    # Find all PDFs and existing numbered files
    pdf_files = sorted([f for f in folder.glob("*.pdf") if f.is_file()])
    
    if not pdf_files:
        print(f"No PDF files found in {folder_path}")
        return
    
    # Pattern to match existing format: S_01_2020_filename.pdf
    pattern = rf"^{re.escape(prefix)}_(\d+)_{re.escape(year)}_"
    
    # Find largest existing serial number
    max_serial = 0
    already_renamed = set()
    
    for pdf in pdf_files:
        match = re.match(pattern, pdf.name)
        if match:
            serial = int(match.group(1))
            max_serial = max(max_serial, serial)
            already_renamed.add(pdf.name)
    
    # Rename files that don't match the pattern
    next_serial = max_serial + 1
    renamed_count = 0
    
    for pdf in pdf_files:
        if pdf.name in already_renamed:
            print(f"✓ Already named: {pdf.name}")
            continue
        
        # Create new filename
        new_name = f"{prefix}_{next_serial:02d}_{year}_{pdf.name}"
        new_path = folder / new_name
        
        # Rename file
        pdf.rename(new_path)
        print(f"✓ Renamed: {pdf.name} → {new_name}")
        
        next_serial += 1
        renamed_count += 1
    
    print(f"\n✓ Completed: {renamed_count} files renamed")

# ============== MAIN ==============
if __name__ == "__main__":
    # Load configuration from variables.json
    config = load_config("variables.json")
    
    if config:
        folder_path = config.get("folder_path")
        prefix = config.get("prefix", "S")
        year = config.get("year", "2020")
        
        print(f"Using folder: {folder_path}")
        print(f"Prefix: {prefix}, Year: {year}\n")
        
        rename_pdfs(folder_path, prefix, year)
