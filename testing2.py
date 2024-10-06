import mechanicalsoup
import streamlit as st
import re

def cosas():
    browser = mechanicalsoup.Browser()

    browser.add_headers({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.9",
        "Connection": "keep-alive",
        "Referrer-Policy": "origin-when-cross-origin"
    })

    browser.get("https://www.bing.com")

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
