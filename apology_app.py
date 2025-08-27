import streamlit as st

st.title("💌🥲 Apology Letter ")

name = st.text_input("Enter your BEAUTIFUL name MADAM :")

if st.button("Generate Letter"):
    letter = f"""
    Dear {name},

    I want to take a moment to say I’m truly sorry.  
    I know I hurt you, and that’s the last thing I ever wanted to do.  
    You mean so much to me, and it breaks my heart knowing I caused you pain. 💔  

    I promise to listen better, love harder, and never take you for granted.  
    LAST 2 Days ah oru busy schedule and work la irunthe 🥲, thats why . Today unaku periods
    start aagiduchu but still naa unkita atha pathi kekama irunthe 🥲 THAT IS MY BIG BIG MISTAKE 🫠
    Unoda birthday ku kandipa oru nalla GIFT 🎁💐 kudupen . Yeah I m biggest clown 🤡😿 in this 
    BEAUTIFUL RELATIONSHIP 💕. Romba days aachu letter kuduthu so Nenu ee lekhanu naa ammayiki icchanu 🫀🫵
    
    ఇకనుంచి చిన్ని, ఇలా చేయకు. నీకు కోపం వచ్చినా, ఏదైనా సమస్య వచ్చినా నన్ను చూపించు, లేదా నన్ను
    కొట్టాలి అనుకుంటే కొట్టు, నేనేమీ అందుకోడానికి సిద్ధంగా ఉన్నాను. నేను సగం కూడా మన ప్రేమలో
    చేయలేదు 🙁😔. కానీ నేను వినతి చేస్తున్నాను, దయచేసి వెళ్లవద్దు 😭. 
    
    నీవే నా పెళ్ళం, నా ప్రపంచం, నా అన్నీ మేడమ్ 🫂👻🤍
    
    YOU ARE MY NOT TARA AND I M NOT UR AATHI(ohh kadhal kanmani😅movie)
    
    I M UR CHINNU AND U ARE MY MUTTAKANNI 😍 🖤💞💋
    

    Yours always,  
    CHINNU 😁❣
    """
    st.markdown(letter)