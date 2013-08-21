import scraperwiki
import lxml.html
from mechanize import ParseResponse, urlopen, urljoin
url ="http://www.censusindia.gov.in/Census_Data_2001/Census_Data_Online/Household_Population/Female_Headed_HH_By_Marital_Status_Age.aspx"

response = urlopen(url)

forms = ParseResponse(response, backwards_compat=False)
print forms
form = forms[0]
print form
form.set_value(["rdbState"], kind="singlelist", nr=0)

# form.click() returns a mechanize.Request object
# (see HTMLForm.click.__doc__ if you want to use only the forms support, and
# not the rest of mechanize)
#print urlopen(form.click()).read()
#print form.click()

response= urlopen(form.click())
forms = ParseResponse(response, backwards_compat=False)
form = forms[0]

#print control.name, control.value, control.type
#control.value = ["01"]
#print control.name, control.value, control.type

form.set_value(['36'], name="drpState")
content=urlopen(form.click())
response=lxml.html.fromstring(content.read())
#print response.read()
row=[]
data=[]
l_c=0
s_no=1
for i in response.cssselect("tr.GridRows td"):
    if l_c<10:
        row.append(i.text_content())
        l_c+=1
    else:
        row.append(i.text_content())
        l_c=0
        data.append(row)
        scraperwiki.sqlite.save(unique_keys=["S_no"],data={"S_no":s_no,"State":row[1],"Age Groups":row[2],"Never_married_head_males":row[3],"Never_married_head_females":row[4],"Currently_married_head_males":row[5],"Currently_married_head_females":row[6],"Widowed_head_Males":row[7],"Widowed_head_females":row[8],"Divorced_head_male":row[9],"Divorced_head_female":row[10]})
        s_no+=2
        row=[]

s_no=2
for i in response.cssselect("tr.GridAlternativeRows td"):
    if l_c<10:
        row.append(i.text_content())
        l_c+=1
    else:
        row.append(i.text_content())
        l_c=0
        data.append(row)
        scraperwiki.sqlite.save(unique_keys=["S_no"],data={"S_no":s_no,"State":row[1],"Age Groups":row[2],"Never_married_head_males":row[3],"Never_married_head_females":row[4],"Currently_married_head_males":row[5],"Currently_married_head_females":row[6],"Widowed_head_Males":row[7],"Widowed_head_females":row[8],"Divorced_head_male":row[9],"Divorced_head_female":row[10]})
        s_no+=2
        row=[]

