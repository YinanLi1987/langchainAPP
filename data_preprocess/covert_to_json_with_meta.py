import docx
import json

# Function to convert a Word document to JSON
def convert_docx_to_json(docx_path, metadata):
    # Load the Word document
    doc = docx.Document(docx_path)

    # Extract text content from paragraphs
    paragraphs = [p.text for p in doc.paragraphs]
    page_content = "\n".join(paragraphs)

    # Create JSON object
    json_data = {
        "page_content": page_content,
        "metadata": metadata
    }

    return json_data

# Example usage
docx_path = "/Users/yinanli/Documents/OAMK/mediatek/docs/24501CR/C1-242696.docx"  # Path to your Word document
#metadata = {
#    "title0":"3GPP TS 24.501",
#    "title1": "Technical Specification Group Core Network and Terminals",
#    "title2":"Non-Access-Stratum(NAS) protocol for 5G System(5GS); Stage 3;",
#    "title3":"Physical layer procedures for control",
#    "Release": 18,
#    "Version":"V18.6.0",
#    "Publish_time":"2024-03",
#}
# define the metadata of CR

metadata= {
      "header": {
        "WG": "TSG-CT WG1",
        "Meeting": "#148",
        "Meeting_location": "Changsha, Hunan Province, China",
        "Meeting_date": "15-04-2024",
        "TDoc_no.": "C1-242696",
        "TDoc_no._was":"C1-242619"
      },
      "spec_number": "24.501",
      "CR_number": "6229",
      "revise_number": "2",
      "Current_version": "18.6.0",
      "Incorporates_to_version":"",
      "Proposed_change_affects_UICC": "Core Network",
      "Title": "Update UL PDU Set handling when inter-system change",
      "Source_to_WG": "Nokia",
      "Source_to_TSG": "C1",
      "Work_item_code": "XRM",
      "Date": "08-04-2024",
      "Category": "F (correction)",
      "Release": "Rel-18",
      "WG_status":"postponed",
      "TSG_status":"",
    }
# Convert the Word document to JSON
json_data = convert_docx_to_json(docx_path, metadata)

# Save JSON to a file
output_path = "/Users/yinanli/Documents/OAMK/mediatek/langchainAPP/docs_json/242696.json"
with open(output_path, "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print("Conversion complete. JSON saved to:", output_path)
