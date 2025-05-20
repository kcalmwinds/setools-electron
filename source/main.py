from pyscript import window, document
from js import navigator as nav

summary_element = document.getElementById("summarybox")
summary_output = document.getElementById("summaryoutput")

current_action_element = document.getElementById("currentactionbox")
current_action_output = document.getElementById("currentactionoutput")

next_action_element = document.getElementById("nextactionbox")
next_action_output = document.getElementById("nextactionoutput")

current_action_select = document.getElementById("currentownerselect")
next_action_select = document.getElementById("nextownerselect")
current_action_select_out = document.getElementById("currentactionselectout")
next_action_select_out = document.getElementById("nextactionselectout")

next_contact_datetime_local = document.getElementById("nextcontactdatetime")
next_contact_out = document.getElementById("nextcontactoutput")

all_output = document.getElementById("outputtext")





def update_summary(event):
    summary_output.innerText = summary_element.value


def update_currentaction(event):
    current_action_output.innerText = current_action_element.value


def update_nextaction(event):
    next_action_output.innerText = next_action_element.value

def update_current_action_owners(event):
    current_action_select_out.innerText = current_action_select.value
    
def update_next_action_owners(event):
    next_action_select_out.innerText = next_action_select.value

def update_next_contact_date(event):
    next_contact_out.innerText = next_contact_datetime_local.value
    #window.console.log(next_contact_datetime_local.value)

def copy_to_clipboard(event):
    #navigator.clipboard.writeText(all_output.innerText)
    nested_element = all_output.innerText
    nav.clipboard.writeText(nested_element)


def reset_all_fields(event):
    summary_element.value = "" 
    summary_output.innerText = "" 

    current_action_element.value = "" 
    current_action_output.innerText = "" 

    next_action_element.value = ""     
    next_action_output.innerText = ""

    current_action_select.value = "" 
    next_action_select.value = "" 
    current_action_select_out.innerText = "" 
    next_action_select_out.innerText = "" 

    next_contact_datetime_local.value = "" 
    next_contact_out.innerText = "" 