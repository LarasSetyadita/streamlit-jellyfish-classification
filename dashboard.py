import streamlit as st

#########################
# pengaturan tampilan #
#########################
st.set_page_config(layout='wide')

# load css file
st.markdown(
    '<link rel="stylesheet" href="css/style.css">',
    unsafe_allow_html=True
)

###############
# main method #
###############
def main():

    st.markdown('<h1 class="page-title">🌊 Jellyfish Classification Dashboard 🪼</h1>', unsafe_allow_html=True)
    st.write('hello world')

#########################
# menjalankan kode main #
#########################
if __name__ == '__main__':
    main()