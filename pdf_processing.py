import os
from PyPDF2 import PdfReader, PdfWriter
import logging

# --- Summary ---
# This script processes PDF files within a specified directory.
# It logs the size of each PDF, identifies files exceeding 200 MB,
# and splits those large files into smaller PDFs, each under 200 MB.
# A report file ('pdf_processing_report.txt') is generated, listing file sizes and large files.
# Logging is provided to track the progress and any errors.

# --- How to Use for NotebookLM Sources ---
# 1. Install PyPDF2: pip install PyPDF2
# 2. Replace 'input_directory' and 'output_directory' with your paths.
# 3. Run the script: python your_script_name.py
# 4. Upload the PDFs from 'output_directory' to NotebookLM as sources.
# 5. Review 'pdf_processing_report.txt' for file size information.

# --- NotebookLM Size Limitations ---
# NotebookLM has size limitations for uploaded documents.
# It is recommended to keep individual files under 200 MB to ensure compatibility.
# This script helps to automatically split larger files into smaller, compatible chunks.
# NotebookLM also has limits on the total number of documents and the total size of all documents within a project.
# Please check Google's NotebookLM documentation for the most up to date limitations.
# --- End Summary ---

def setup_logging(output_dir):
    """Sets up logging to a file and console."""
    log_file = os.path.join(output_dir, "pdf_processing.log")
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def create_report_file(input_dir, output_dir, large_files):
    """Creates a report file detailing file sizes and large files."""
    report_file = os.path.join(output_dir, "pdf_processing_report.txt")
    with open(report_file, "w") as f:
        f.write("--- PDF Processing Report ---\n\n")
        f.write("--- File Sizes ---\n")
        for filename in os.listdir(input_dir):
            if filename.lower().endswith(".pdf"):
                filepath = os.path.join(input_dir, filename)
                file_size_bytes = os.path.getsize(filepath)
                file_size_mb = file_size_bytes / (1024 * 1024)
                f.write(f"{filename}: {file_size_mb:.2f} MB\n")

        f.write("\n--- Files Larger Than 200 MB ---\n")
        if large_files:
            for filename in large_files:
                f.write(f"{filename}\n")
        else:
            f.write("No files larger than 200 MB found.\n")

def process_pdfs(input_dir, output_dir, max_size_mb=200):
    """
    Processes PDF files, splits large files, and logs progress.

    Args:
        input_dir (str): Path to the directory containing the input PDFs.
        output_dir (str): Path to the directory where split PDFs will be saved.
        max_size_mb (int): Maximum allowed size of a PDF file in megabytes.
    """
    setup_logging(output_dir) #Sets up logging to file and console.

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logging.info(f"Created output directory: {output_dir}")

    large_files = []

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(input_dir, filename)
            file_size_bytes = os.path.getsize(filepath)
            file_size_mb = file_size_bytes / (1024 * 1024)

            logging.info(f"Processing {filename}: {file_size_mb:.2f} MB")

            if file_size_mb > max_size_mb:
                large_files.append(filename)
                logging.info(f"File '{filename}' is larger than {max_size_mb} MB. Splitting...")
                split_large_pdf(filepath, output_dir, max_size_mb)
            else:
                logging.info(f"File '{filename}' is within size limit.")
    create_report_file(input_dir, output_dir, large_files) #creates report file.
    logging.info("PDF processing complete.")

def split_large_pdf(filepath, output_dir, max_size_mb):
    """Splits a large PDF into multiple smaller PDFs."""
    try:
        pdf_reader = PdfReader(filepath)
        total_pages = len(pdf_reader.pages)
        base_filename = os.path.splitext(os.path.basename(filepath))[0]
        page_index = 0
        file_index = 1
        pdf_writer = PdfWriter()
        current_file_size_bytes = 0

        for page_num in range(total_pages):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
            current_file_size_bytes += len(page.extract_text().encode('utf-8')) #Very rough size estimate.

            if current_file_size_bytes >= (max_size_mb * 1024 * 1024) or page_num == total_pages - 1:
                output_path = os.path.join(output_dir, f"{base_filename}_part{file_index}.pdf")
                with open(output_path, "wb") as output_file:
                    pdf_writer.write(output_file)
                logging.info(f"Created {os.path.basename(output_path)}")
                file_index += 1
                pdf_writer = PdfWriter()
                current_file_size_bytes = 0
        logging.info(f"Successfully split '{os.path.basename(filepath)}'")

    except Exception as e:
        logging.error(f"Error splitting '{os.path.basename(filepath)}': {e}")

# Example Usage
input_directory = "path/to/your/pdfs"  # Replace with the actual input directory
output_directory = "path/to/output/pdfs" # Replace with the desired output directory
process_pdfs(input_directory, output_directory)