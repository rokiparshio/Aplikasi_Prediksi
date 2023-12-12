## Load Libraries
import streamlit as st 
from PIL import Image

# Display the c title
st.title("Makhluk Air")

## set team iamge
image = Image.open('Team logo/foto1.webp')

# set the desired size
new_size = (400, 300)

#Resize the image
resized_image = image.resize(new_size)

##set the image
st.image(resized_image)

##info about the team
st.write("SpongeBob SquarePants adalah seri animasi terpopuler di jaringan Nickelodeon. Pada awalnya seri animasi ini ditayangkan pada 1999 di Amerika Serikat dan diciptakan oleh almarhum Stephen Hillenburg, seorang animator dan ahli biologi laut,")
st.write("erbagai karakter juga menerima ulasan positif serta mendapat perhatian dari berbagai selebritas. Selain muncul di televisi, karakter juga diperankan dalam film teater, permainan video, dan dua seri spin-off. Selain itu juga karakter terkenal dalam budaya populer seperti meme. Karakter utama SpongeBob SquarePants menjadi ikon penjualan serta terkenal dalam hal komersial.")

st.subheader("Dibawah adalah tokoh lainnya")

##For members
st.header("Spongebob SquerPants")
st.info('Semua Tokoh')
lead=Image.open('Team photos/Team1.jpeg')
size=(400,250)
lead_image=lead.resize(size)
st.image(lead_image)

st.subheader("Connect dengan Spongebob")

# Button to send an email
if st.button("Contact Me via Email"):
    st.markdown('<a href="rokipahmad35@gmail.com">Send Email</a>', unsafe_allow_html=True)

# Button to visit linkedin Profile
if st.button("Visit My Linkedin"):
    st.markdown('<a href="https://www.linkedin.com/in/rokip-ahmad-a47b4522b/">Send Linkedin</a>', unsafe_allow_html=True)
    
# Button to visit Instagram Profile
if st.button("Visit My Instagram"):
    st.markdown('<a href="https://www.instagram.com/arrokipar.56/">Send DM Instagram</a>', unsafe_allow_html=True)
    
# Button to visit Github
if st.button("Visit My Github "):
    st.markdown('<a href="https://github.com/rokiparshio">Lets go Join!</a>', unsafe_allow_html=True)
    




