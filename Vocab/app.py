import streamlit as st
from pathlib import Path

with st.container(border=True):
    st.set_page_config(page_icon="✍️",page_title="Vocab",layout="centered")

    MainFolder = Path("Files") # it points the main folder name which has all md files

    sectionFiles = sorted(MainFolder.glob("*.md")) # sectionFiles is a list stores all the files
    # .glob("*.md") this is a function that finds all the files ending with .md and sort them alphabetically
    st.title("MY VOCABULARY 📝")
    st.caption("**Learn. Remember. Speak with confidence**")
    st.divider()

    if "page" not in st.session_state:
            st.session_state.page = 1  # beacuse default page number always starting page 

    current_file = sectionFiles[st.session_state.page - 1] # why -1 beaacuse it is a list and files are stored from indexx 0 so in index zero we have file 1 so current page finds easily

    st.subheader(f":blue[{'Vocabulary'}]")
    with st.container(border=True):
        st.markdown(f"**Table** **{st.session_state.page}** ",text_alignment="center")
    
        with open(current_file,"r",encoding="utf-8") as f:
            st.markdown(f.read())

            st.divider()
            page_num = st.pagination(num_pages=len(sectionFiles),max_visible_pages=3,default=1) # it creates the pagibation and stored the page no 1 initially

            if page_num != st.session_state.page:
                 st.session_state.page = page_num
                 st.rerun()

    st.caption("**Vocab 💠 Learn Every day 💠 Built with Streamlit**",text_alignment="right") 
    st.caption(f"**Made by :blue[Tharun Kumar]**",text_alignment="right") 


