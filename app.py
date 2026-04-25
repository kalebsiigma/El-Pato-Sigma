import streamlit as st

st.title("PATO LEGAL")

st.header("O Site De Um Pato Sigma")

nome = st.text_input("Olá sigma, qual teu name?")

if nome:
    st.write(f"Olá {nome}" " Ultra Sigma")
