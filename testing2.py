import mechanicalsoup
import streamlit as st
import re

def cosas():
    browser = mechanicalsoup.StatefulBrowser()

    browser.open("https://www.bing.com")

    browser.select_form('form[action="/search"]')

    browser["q"] = "944022363"

    browser.submit_selected()
    # ---------------------------------------------------

    html_content = browser.page.prettify()

    # if value == "944022363":
    #     st.write(html_content)

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html_content)

    if emails:
        for email in emails:
       
            print(email)
            return email


def main():
    st.write(cosas())


if __name__=="__main__":
    main()
