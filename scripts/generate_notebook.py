import sys
import json
import os
import glob

def create_notebook(src_dir, output_file):
    # Find README.md
    readme_path = os.path.join(src_dir, "README.md")
    
    # Find the python script (.py) - assuming there's only one main script per dir
    py_files = glob.glob(os.path.join(src_dir, "*.py"))
    
    cells = []
    
    # Add Markdown cell
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        md_lines = md_content.splitlines(True)
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": md_lines
        })
    else:
        print(f"Warning: No README.md found in {src_dir}")
        
    # Add Code cell
    if py_files:
        py_file = py_files[0]
        with open(py_file, "r", encoding="utf-8") as f:
            py_content = f.read()
            
        py_lines = py_content.splitlines(True)
        # Add magic command for inline plots
        py_lines.insert(0, "%matplotlib inline\n")
        
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": py_lines
        })
    else:
        print(f"Warning: No .py file found in {src_dir}")
        
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=1)
        
    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_notebook.py <src_dir> <output_file>")
        sys.exit(1)
        
    create_notebook(sys.argv[1], sys.argv[2])
