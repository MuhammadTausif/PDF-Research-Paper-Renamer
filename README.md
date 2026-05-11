# PDF Research Paper Renamer

Automatically rename research PDFs with a consistent naming convention: `PREFIX_SERIALNUMBER_YEAR_ORIGINALNAME.pdf`

## Features

✓ **Sequential numbering** - Auto-detects last number and continues  
✓ **Secure config** - Folder paths stored locally in `variables.json` (not in git)  
✓ **Batch processing** - Rename multiple PDFs at once  
✓ **Safe** - Skips already-renamed files  

## Quick Start

### 1. Setup

```bash
# Clone or download this project
git clone <your-repo>
cd pdf-renamer

# Edit variables.json with YOUR folder path
# Example for Windows:
# {
#   "folder_path": "C:\\Users\\YourName\\Documents\\ResearchPapers",
#   "prefix": "S",
#   "year": "2020"
# }
```

### 2. Run

```bash
python pdf_renamer.py
```

### 3. Output Example

```
Using folder: C:\Users\YourName\Documents\ResearchPapers
Prefix: S, Year: 2020

✓ Renamed: paper1.pdf → S_01_2020_paper1.pdf
✓ Renamed: paper2.pdf → S_02_2020_paper2.pdf
✓ Renamed: paper3.pdf → S_03_2020_paper3.pdf

✓ Completed: 3 files renamed
```

## Configuration

Edit `variables.json`:

```json
{
  "folder_path": "C:\\Users\\YourName\\Documents\\ResearchPapers",
  "prefix": "S",
  "year": "2020"
}
```

| Key | Description |
|-----|-------------|
| `folder_path` | Full path to folder with PDFs (Windows: use `\\` or raw string `r"C:\..."`) |
| `prefix` | Single letter prefix (e.g., "S" for Survey, "R" for Research) |
| `year` | Year to add to filename |

## Security

⚠️ **`variables.json` is NOT tracked by git** - it stays on your machine  

Why?
- Contains your personal folder paths
- Not shared with team/GitHub
- Each developer creates their own `variables.json`

## File Structure

```
pdf-renamer/
├── pdf_renamer.py          # Main script
├── variables.json          # Your config (NOT tracked)
├── .gitignore              # Excludes variables.json
├── README.md               # This file
└── GIT_SETUP.md            # Detailed git instructions
```

## How It Works

1. **Reads** `variables.json` for folder path and settings
2. **Scans** folder for all `.pdf` files
3. **Finds** highest existing serial number in filenames
4. **Renames** unmapped files sequentially starting from next number
5. **Skips** files already in correct format

## Requirements

- Python 3.6+
- Windows/Mac/Linux

## Troubleshooting

**Error: `variables.json not found`**
```bash
# Make sure variables.json exists in same folder as pdf_renamer.py
# Copy from variables.json template and edit it
```

**Error: `Folder not found`**
```bash
# Check folder_path in variables.json
# Use full path, not relative path
# Windows: C:\Users\Name\Docs (or r"C:\Users\Name\Docs")
```

**No PDFs found**
```bash
# Check folder actually contains .pdf files
# Make sure they're .pdf not .PDF (case sensitive on Mac/Linux)
```

## Example Use Cases

- **Organize research papers**: `S_01_2020_smith_2020.pdf`
- **Conference submissions**: `C_01_2024_paper_title.pdf`
- **Literature review**: `L_01_2023_methodology.pdf`

Change `prefix` in `variables.json` for each category.

## Git Workflow

```bash
# First commit (one time)
git add .gitignore pdf_renamer.py README.md
git commit -m "Initial commit: Add PDF renaming script with secure config setup"
git push origin main
```

Your personal `variables.json` never gets committed. ✓

## For Team Members

```bash
git clone <repo>
cd pdf-renamer
# Create your own variables.json
python pdf_renamer.py
```

## License

MIT (or specify your license)

---

**Questions?** See `GIT_SETUP.md` for detailed git instructions.
