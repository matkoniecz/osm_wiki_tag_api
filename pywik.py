import pywikibot

# https://www.mediawiki.org/wiki/Manual:Pywikibot/Installation#Install_Pywikibot
# I followed it, run script, and recopied it here
# https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script

site = pywikibot.Site()
page = pywikibot.Page(site, "Key:highway")
text = page.text
print(text)