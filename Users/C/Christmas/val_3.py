###############################################################################
# START HERE: Tutorial for scraping pages behind form, using the
# very powerful Mechanize library. Documentation is here: 
# http://api.plone.org/Plone/2.5.3/private/PasswordResetTool/private/mechanize._mechanize.Browser-class.html
###############################################################################
import mechanize 
from BeautifulSoup import BeautifulSoup

# We're scraping info on clinical trials on the US
# Clinical Trials website. 
url = "http://www.clinicaltrials.gov/ct2/search/advanced"
br = mechanize.Browser()
br.open(url)

#--------------------------------------------------------------------------------------
# Loop through all the forms on the page, and print some information about each one.
# This should work with your own URL.
#--------------------------------------------------------------------------------------
for form in br.forms():
    print "--------------------"
    print "Form name : " + form.name 
    br.select_form(name=form.name)
    
    # loop through the controls in the form
    print "Controls:"
    for control in br.form.controls:
        if not control.name:
            print " - (type) =", (control.type)
            continue
            
        print " - (name, type, value) =", (control.name, control.type, br[control.name])

        # loop through all the options in any select (drop-down) controls
        if control.type == 'select':
            for item in control.items:
                print " - - - (value, labels) =", (str(item), [label.text  for label in item.get_labels()])

#--------------------------------------------------------------------------------------
# Next, let's submit the main form.
#--------------------------------------------------------------------------------------

# First, tell Mechanize which form to submit.
# If your form didn't have a CSS name attribute, use 'nr' instead 
# - e.g. br.select_form(nr=0) to find the first form on the page. 
br.select_form(name='advanced search')

# Set the fields: what are you looking for?
br["recr"] = ["Closed"]
br["rslt"] = ["Without"]
br["type"] = ["Intr"]
br["cntry1"] = ["NA:US"]
br["cntry2"] = ["SS:IN"]

# and submit the form
br.submit()

# We can now start processing it as normal
soup = BeautifulSoup(br.response().read())
h1_tags = soup.findAll('h1')
print h1_tags

