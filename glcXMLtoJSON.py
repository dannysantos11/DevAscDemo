import xmltodict
import json

with open('glc.xml') as f:
    xml_data = f.read()

# Parse the XML data into a Python dictionary
glc_dict = xmltodict.parse(xml_data)

# Convert Python dictionary to JSON string
glc_json = json.dumps(glc_dict, indent=4)

# Print the JSON string
print(glc_json)

# Optionally, write the JSON data to a file named glc.json
# with open('glc.json', 'w') as f:
#     f.write(glc_json)

# Convert to YAML
import yaml

glc_yaml = yaml.dump(glc_dict, sort_keys=False, indent=4)
print(glc_yaml)

# Optionally, write the YAML data to a file named glc.yaml
with open('glc.yaml', 'w') as f:
    f.write(glc_yaml)

