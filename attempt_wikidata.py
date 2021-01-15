import extract_wikidata_data_item
import extract_wikibase_item
p = extract_wikidata_data_item.json_response_from_api("Q42")
entity = extract_wikibase_item.extract_entity_from_parsed_json(p)
print(entity)
print(extract_wikibase_item.extract_description(entity))
