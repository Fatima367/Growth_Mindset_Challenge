# import streamlit as st
# from fpdf import FPDF
# from PIL import Image
# import os
# from docx2pdf import convert
# import tempfile

# def text_to_pdf(text, output_file):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
    
#     # Split text into lines and add to PDF
#     for line in text.split('\n'):
#         pdf.cell(0, 10, txt=line, ln=True)
    
#     pdf.output(output_file)

# def image_to_pdf(image_file, output_file):
#     image = Image.open(image_file)
#     # Convert image to RGB if it's not
#     if image.mode != 'RGB':
#         image = image.convert('RGB')
#     image.save(output_file, "PDF")

# def main():
#     st.title("📚 Growth Mindset File Converter")
    
#     st.write("""
#     Welcome to the File Converter App! This tool embodies the growth mindset by helping you:
#     - Learn new file formats
#     - Adapt content for different needs
#     - Embrace the learning process
#     """)

#     conversion_type = st.selectbox(
#         "Choose your conversion type:",
#         ["Text to PDF", "Word to PDF", "Image to PDF"]
#     )

#     if conversion_type == "Text to PDF":
#         st.subheader("Text to PDF Converter")
#         text_content = st.text_area("Enter your text here:", height=200)
        
#         if st.button("Convert to PDF"):
#             if text_content:
#                 try:
#                     with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
#                         text_to_pdf(text_content, tmp_file.name)
#                         with open(tmp_file.name, "rb") as file:
#                             st.download_button(
#                                 label="Download PDF",
#                                 data=file,
#                                 file_name="converted_text.pdf",
#                                 mime="application/pdf"
#                             )
#                     os.unlink(tmp_file.name)
#                 except Exception as e:
#                     st.error(f"An error occurred: {str(e)}")
#             else:
#                 st.warning("Please enter some text to convert.")

#     elif conversion_type == "Word to PDF":
#         st.subheader("Word to PDF Converter")
#         docx_file = st.file_uploader("Upload Word Document", type=['docx'])
        
#         if docx_file is not None:
#             if st.button("Convert to PDF"):
#                 try:
#                     with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_docx:
#                         tmp_docx.write(docx_file.getvalue())
                        
#                     pdf_path = tmp_docx.name.replace('.docx', '.pdf')
#                     convert(tmp_docx.name, pdf_path)
                    
#                     with open(pdf_path, "rb") as file:
#                         st.download_button(
#                             label="Download PDF",
#                             data=file,
#                             file_name="converted_document.pdf",
#                             mime="application/pdf"
#                         )
                    
#                     # Clean up temporary files
#                     os.unlink(tmp_docx.name)
#                     os.unlink(pdf_path)
#                 except Exception as e:
#                     st.error(f"An error occurred: {str(e)}")

#     else:  # Image to PDF
#         st.subheader("Image to PDF Converter")
#         image_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
        
#         if image_file is not None:
#             st.image(image_file, caption="Uploaded Image", use_column_width=True)
            
#             if st.button("Convert to PDF"):
#                 try:
#                     with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
#                         image_to_pdf(image_file, tmp_file.name)
#                         with open(tmp_file.name, "rb") as file:
#                             st.download_button(
#                                 label="Download PDF",
#                                 data=file,
#                                 file_name="converted_image.pdf",
#                                 mime="application/pdf"
#                             )
#                     os.unlink(tmp_file.name)
#                 except Exception as e:
#                     st.error(f"An error occurred: {str(e)}")

#     st.markdown("""
#     ### 🌱 Growth Mindset Tips
#     - Every conversion is a learning opportunity
#     - If something doesn't work, try a different approach
#     - Share your knowledge with others
#     """)

# if __name__ == "__main__":
#     main()

import streamlit as st
from fpdf import FPDF
from PIL import Image
import os
from docx2pdf import convert
import tempfile
import time

# Configure the page layout and theme
st.set_page_config(
    page_title="Growth Mindset File Converter",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        margin-top: 1rem;
    }
    .stButton > button:hover {
        background-color: #FF2B2B;
        border-color: #FF2B2B;
    }
    .upload-box {
        border: 2px dashed #cccccc;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
    .success-message {
        padding: 1rem;
        border-radius: 10px;
        background-color: #28a745;
        color: white;
        margin: 1rem 0;
    }
    .converter-card {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    .header-container {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #FF4B4B 0%, #FF8F8F 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def text_to_pdf(text, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for line in text.split('\n'):
        pdf.cell(0, 10, txt=line, ln=True)
    
    pdf.output(output_file)

def image_to_pdf(image_file, output_file):
    image = Image.open(image_file)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image.save(output_file, "PDF")

def main():
    # Header Section
    st.markdown("""
        <div class="header-container">
            <h1>📚 Growth Mindset File Converter</h1>
            <p>Transform your files with a growth mindset approach!</p>
        </div>
    """, unsafe_allow_html=True)

    # Sidebar with tips and information
    with st.sidebar:
        st.header("🌱 Growth Mindset Tips")
        st.info("""
        - Every conversion is a learning opportunity
        - If something doesn't work, try a different approach
        - Share your knowledge with others
        """)
        
        st.header("📖 About")
        st.write("""
        This tool helps you convert various file formats while embracing 
        the growth mindset philosophy. Keep learning and growing!
        """)

    # Main content
    conversion_type = st.selectbox(
        "What would you like to convert today?",
        ["Text to PDF", "Word to PDF", "Image to PDF"],
        index=0
    )

    # Create three columns for better layout
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        
        if conversion_type == "Text to PDF":
            st.subheader("✍️ Text to PDF Converter")
            text_content = st.text_area(
                "Enter your text here:",
                height=200,
                placeholder="Start typing or paste your text here..."
            )
            
            if st.button("Convert to PDF 📄"):
                if text_content:
                    with st.spinner('Converting your text to PDF...'):
                        try:
                            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                                text_to_pdf(text_content, tmp_file.name)
                                with open(tmp_file.name, "rb") as file:
                                    st.success("Conversion successful! ✨")
                                    st.download_button(
                                        label="Download PDF 📥",
                                        data=file,
                                        file_name="converted_text.pdf",
                                        mime="application/pdf"
                                    )
                            os.unlink(tmp_file.name)
                        except Exception as e:
                            st.error(f"An error occurred: {str(e)}")
                else:
                    st.warning("⚠️ Please enter some text to convert.")

        elif conversion_type == "Word to PDF":
            st.subheader("📎 Word to PDF Converter")
            st.markdown('<div class="upload-box">', unsafe_allow_html=True)
            docx_file = st.file_uploader("Drop your Word document here", type=['docx'])
            st.markdown('</div>', unsafe_allow_html=True)
            
            if docx_file is not None:
                if st.button("Convert to PDF 📄"):
                    with st.spinner('Converting your Word document to PDF...'):
                        try:
                            with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_docx:
                                tmp_docx.write(docx_file.getvalue())
                                
                            pdf_path = tmp_docx.name.replace('.docx', '.pdf')
                            convert(tmp_docx.name, pdf_path)
                            
                            with open(pdf_path, "rb") as file:
                                st.success("Conversion successful! ✨")
                                st.download_button(
                                    label="Download PDF 📥",
                                    data=file,
                                    file_name="converted_document.pdf",
                                    mime="application/pdf"
                                )
                            
                            os.unlink(tmp_docx.name)
                            os.unlink(pdf_path)
                        except Exception as e:
                            st.error(f"An error occurred: {str(e)}")

        else:  # Image to PDF
            st.subheader("🖼️ Image to PDF Converter")
            st.markdown('<div class="upload-box">', unsafe_allow_html=True)
            image_file = st.file_uploader("Drop your image here", type=['png', 'jpg', 'jpeg'])
            st.markdown('</div>', unsafe_allow_html=True)
            
            if image_file is not None:
                st.image(image_file, caption="Preview", use_column_width=True)
                
                if st.button("Convert to PDF 📄"):
                    with st.spinner('Converting your image to PDF...'):
                        try:
                            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                                image_to_pdf(image_file, tmp_file.name)
                                with open(tmp_file.name, "rb") as file:
                                    st.success("Conversion successful! ✨")
                                    st.download_button(
                                        label="Download PDF 📥",
                                        data=file,
                                        file_name="converted_image.pdf",
                                        mime="application/pdf"
                                    )
                            os.unlink(tmp_file.name)
                        except Exception as e:
                            st.error(f"An error occurred: {str(e)}")

        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style="text-align: center; margin-top: 3rem; padding: 1rem; background-color: #f8f9fa; border-radius: 10px;">
            <p>Made with ❤️ for learning and growth</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

