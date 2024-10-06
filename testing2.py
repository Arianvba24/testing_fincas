import mechanicalsoup
import streamlit as st


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
            data_json[str(indice)] = email
            print(email,value)
            return email


def main():
    st.write(cosas())


if __name__=="__main__":
    main()