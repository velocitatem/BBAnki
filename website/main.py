import streamlit as st
from bbanki import convert
# this is an interface for a user to use the data downloaded from BlackBoard. THis data is a quiz. This will convert that quiz to an anki file.


# create an about in the sidebar
# https://github.com/velocitatem/BBAnki
st.sidebar.title("About")
st.sidebar.info(
    """
    This is a tool to convert BlackBoard quizzes to Anki flashcards.
    """
)
# mention the github repo
st.sidebar.markdown(
    """
    [GitHub](https://github.com/velocitatem/BBAnki)
    """
)


st.title("BlackBoard Quiz to Anki")
st.write("This is a tool to convert a BlackBoard quiz to an anki file. This is a work in progress. Please report any bugs to the github page.")

# Step 1: In blackboard open the graded quiz
# Step 2: Open the console, find out [here](https://appuals.com/open-browser-console/)
# Step 3: Copy the code below and paste it in the console
# Step 4: Copy the output and paste it in the text box below

st.markdown("1. Open the graded quiz in BlackBoard")
st.markdown("2. Open the console, find out [here](https://appuals.com/open-browser-console/)")
st.markdown("3. Copy the code below and paste it in the console")
st.code("""
let path=window.location.pathname,course=path.split("/")[3],assessment=path.split("/")[9],request={url:"https://blackboard.ie.edu/learn/api/v1/courses/"+course+"/gradebook/attempts/"+assessment+"/assessment/answers/grades?expand=questionAttempt.question,questionAttempt.answerCorrectness",method:"GET"};async function provide(e){let o=e.body.getReader(),t=new TextDecoder("utf-8"),n="";await o.read().then((function e({done:s,value:a}){return s?n:(n+=t.decode(a,{stream:!0}),o.read().then(e))})),e=JSON.parse(n),console.log(e),navigator.clipboard.writeText(e).then((function(){console.log("Async: Copying to clipboard was successful!"),alert("Copying to clipboard was successful!")}),(function(o){console.error("Async: Could not copy text: ",o),alert("Could not copy text to clipboard, you can copy it manually from the console."),console.log("You can copy the following text manually from the console:"),console.log(e)}));let s=new Blob([JSON.stringify(e)],{type:"application/json"}),a=URL.createObjectURL(s);window.open(a)}fetch(request.url,(e=>e.json())).then((e=>{provide(e)}));
""")
st.markdown("4. Copy the output and paste it in the text box below")

# paste here the quiz data
#st.write("Paste the quiz data here")
quiz_data = st.text_area("Paste the quiz data here:")


# what is this quiz called?
quiz_name_in = st.text_input("What is this quiz called?", "Quiz Name")




if st.button("Convert"):
    output= convert(quiz_data, quiz_name_in)
    # read teh file and download it
    with open(output, 'rb') as f:
        bytes = f.read()
        st.download_button(
            label="Download Anki file",
            data=bytes,
            file_name=output,
            mime="application/octet-stream",
        )