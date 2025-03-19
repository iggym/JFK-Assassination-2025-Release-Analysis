# JFK Assassination 2025 Release Analysis

[JFK Assassination](https://en.wikipedia.org/wiki/Assassination_of_John_F._Kennedy) Records - 2025 Documents Release files analysis and  the script to download all the files.

## Analysis Summary 

The CIA’s detailed tracking of Oswald, combined with unclear affiliations (e.g., DBA-2088-3), potential KGB ties, and the handling of third-party claims (e.g., Czornonoh’s), could imply that some information was either withheld, underexplored, or intentionally minimized—perhaps to protect institutional interests, avoid Cold War escalation, or preserve the lone gunman conclusion.

The notes hint at a possible cover-up through omission and ambiguity—particularly regarding intelligence agencies’ knowledge of Oswald.

---
---

## Instructions How to Use:

### Install Libraries:

If you don't have them already, install the requests and beautifulsoup4 libraries:

```Bash

pip install requests beautifulsoup4
```

### Save the Code:

Save the Python code as a .py file (e.g., download_jfk_pdfs.py).

### Run the Script:

Open a terminal or command prompt and navigate to the directory where you saved the file.
Execute the script:

```Bash

python download_jfk_pdfs.py
```

### Downloaded PDFs:

The PDFs will be downloaded into a folder named jfk_pdfs in the same directory as the script.

Use your favorite AI  to create summaries and then do analysis on the summaries. I used Notebook LM and included is a script `pdf_processing.py`  to prepare the pdfs for Notebook LM.

---



## Instructions for Using `pdf_processing.py` to Create NotebookLM Sources

### Overview

The `pdf_processing.py` script is designed to process PDF files in a specified directory. It performs the following tasks:
- Logs the size of each PDF file.
- Identifies files exceeding 200 MB.
- Splits large files into smaller PDFs, each under 200 MB.
- Generates a report file (`pdf_processing_report.txt`) with details about file sizes and large files.

This script ensures compatibility with NotebookLM's size limitations by preparing PDFs for upload.

### Steps to Use

1. **Install Required Library**  
    Install the `PyPDF2` library if you haven't already:  
    ```bash
    pip install PyPDF2
    ```

2. **Set Input and Output Directories**  
    Update the script to specify your input and output directories by replacing `input_directory` and `output_directory` with the appropriate paths.

3. **Run the Script**  
    Execute the script in your terminal or command prompt:  
    ```bash
    python pdf_processing.py
    ```

4. **Upload to NotebookLM**  
    After processing, upload the PDFs from the `output_directory` to NotebookLM as sources.

5. **Review the Report**  
    Check the `pdf_processing_report.txt` file for details about file sizes and any files that were split.

### NotebookLM Size Limitations

NotebookLM has specific size limitations for uploaded documents:
- Individual files should be under 200 MB.
- There are limits on the total number of documents and the total size of all documents within a project.

This script helps ensure your files meet these requirements. For the latest limitations, refer to Google's NotebookLM documentation.
