import streamlit as st

st.set_page_config(
    page_title="For Pallluuuu ❤️",
    page_icon="💖",
    layout="centered"
)

st.balloons()

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#ffd6e7,#ffeaf4,#fff7fb);
}

.block-container{
    padding-top:4rem;
}

.card{
    max-width:650px;
    margin:auto;
    padding:45px;
    background:rgba(255,255,255,0.70);
    backdrop-filter:blur(12px);
    border-radius:30px;
    box-shadow:0 15px 40px rgba(255,105,180,.25);
    text-align:center;
    animation:float 3s ease-in-out infinite;
    transition:.4s;
}

.card:hover{
    transform:scale(1.02);
}

@keyframes float{
0%{transform:translateY(0);}
50%{transform:translateY(-8px);}
100%{transform:translateY(0);}
}

.title{
font-size:48px;
font-weight:700;
color:#ff4f8b;
}

.name{
font-size:42px;
font-weight:bold;
color:#ff2d75;
margin-top:10px;
}

.msg{
font-size:24px;
line-height:1.8;
color:#555;
margin-top:30px;
}

.footer{
margin-top:40px;
font-size:22px;
color:#ff4f8b;
font-weight:bold;
}

.hearts{
font-size:34px;
animation:pulse 1.2s infinite;
}

@keyframes pulse{
50%{
transform:scale(1.25);
}
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<div class="hearts">
💖 🌸 💕 ✨ 🌷
</div>

<div class="title">
Hii
</div>

<div class="name">
Pallluuuu ❤️
</div>

<div class="msg">
Hope your work is going well. 😊<br><br>

I know you're busy, and I don't want to disturb you...<br><br>

Whenever you get a little free time,<br>
please call me dear. 🥺❤️<br><br>

I'll be waiting for your call. 💕
</div>

<div class="footer">
With lots of care 💖
</div>

</div>
""", unsafe_allow_html=True)
