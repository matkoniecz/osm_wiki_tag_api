import mwparserfromhell
import mediawiki_api_wrapper
import password_data

example = """
{{ValueDescription
| key           = craft
| value         = printer
| image = File:Taller ino.jpg
| image_caption = 
| description   =Una pequeña imprenta que produce trabajos publicados como periódicos, libros, revistas, etc.
| osmcarto-rendering      = 
| osmcarto-rendering-size = 
| group         = Oficios
| onNode        = yes
| onWay         = no
| onArea        = yes
| onRelation    = no
| requires      = 
| implies       = 
| combination   = *{{Tag|name}}
*{{Tag|opening_hours}}
*{{Tag|phone}}
*{{Tag|fax}}
*{{Tag|website}} 
| seeAlso       = {{Tag|craft|printmaker}}
| status        = in use
| statuslink    = 
| wikidata      = Q6500733
}}
"""

def remove_wikidata_parameter(text):
    code = mwparserfromhell.parse(text)
    for template in code.filter_templates():
        if template.name.matches("ValueDescription") or template.name.matches("KeyDescription"):
            print(template)
            for param in template.params:
                key = param.split("=")[0].strip()
                value = param.split("=")[1].strip()
                if(key in ["wikidata"]):
                    template.remove(param)
    return str(code)

def create_login_session(index = 'api_password'):
    login_data = password_data.api_login_data(index)
    password = login_data['password']
    username = login_data['user']
    session = mediawiki_api_wrapper.login_and_editing.login_and_create_session(username, password)
    return session


print(remove_wikidata_parameter(example))

session = create_login_session('general_purpose_bot')
# https://wiki.openstreetmap.org/wiki/Category:Wikidata_parameter_waiting_for_removal_from_infobox
for page_title in mediawiki_api_wrapper.query.pages_from_category("Category:Wikidata parameter waiting for removal from infobox"):
    data = mediawiki_api_wrapper.query.download_page_text_with_revision_data(page_title)
    text = data['page_text']
    try:
        text = remove_wikidata_parameter(text)
    except IndexError:
        print()
        print()
        print("FAILED")
        print()
        print()
        print(page_title)
        print()
        print()
        continue
    while True:
        try:
            mediawiki_api_wrapper.login_and_editing.edit_page(session, page_title, text, "remove wikidata parameter (after [[Proposed features/remove link to Wikidata from infoboxes]])", data['rev_id'], data['timestamp'], mark_as_bot_edit=True)
            break
        except mediawiki_api_wrapper.login_and_editing.NoEditPermissionException:
            # Recreate session, may be needed after long processing
            session = shared.create_login_session()
