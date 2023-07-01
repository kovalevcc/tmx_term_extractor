import streamlit as st
from tmx_processing import *
from io import BytesIO
import tempfile

def main():
    st.title("TMX term extractor")
    st.write("Upload a .tmx file.")

    file = st.file_uploader("Upload File")

    if file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file.read())
            temp_file_path = temp_file.name

        #content = file.read()
        source,target = get_text(temp_file_path)
        keywords = get_keywords(source)
        st.write(keywords)

    

if __name__ == "__main__":
    main()
