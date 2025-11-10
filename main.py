import streamlit as st
from collections import Counter
import time

st.set_page_config(page_title="What's Your Current Vibe?", page_icon="🌙", layout="centered")

st.markdown("""
    <style>
    @keyframes fadeIn {
        from { 
            opacity: 0; 
            transform: translateY(30px); 
        }
        to { 
            opacity: 1; 
            transform: translateY(0); 
        }
    }
    
    @keyframes glow {
        0%, 100% { 
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.3); 
        }
        50% { 
            box-shadow: 0 0 40px rgba(255, 215, 0, 0.6); 
        }
    }
    
    .result-container {
        animation: fadeIn 1s ease-out;
        padding: 30px;
        border-radius: 20px;
        margin: 20px 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        backdrop-filter: blur(10px);
    }
    
    .mood-image {
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin: 20px 0;
        animation: fadeIn 1.2s ease-out;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    h1, h2 {
        animation: fadeIn 0.8s ease-out;
    }
    </style>
    """, unsafe_allow_html=True)

def calculate_mood(answers):
    letter_counts = Counter(answers.values())
    max_count = max(letter_counts.values())
    tied_letters = [letter for letter, count in letter_counts.items() if count == max_count]
    
    mood_results = {
        'A': {
            'title': '🌤️ Golden Ember',
            'description': "You're glowing but grounded — peaceful, creative, a little dreamy. You're in a soft-focus moment of rest before something new.",
            'image': 'attached_assets/generated_images/Golden_Ember_vibe_image_172fa472.png',
            'celebration': 'balloons'
        },
        'B': {
            'title': '⚡ Electric Storm',
            'description': "You're buzzing, bold, and a bit chaotic. Passion, irritation, and excitement are tangled together — but you're alive with purpose.",
            'image': 'attached_assets/generated_images/Electric_Storm_vibe_image_e51388d3.png',
            'celebration': 'balloons'
        },
        'C': {
            'title': '🔮 Glass Horizon',
            'description': "You're in a liminal mood — detached, observant, reflective. The world feels like a movie, and you're both inside it and watching from afar.",
            'image': 'attached_assets/generated_images/Glass_Horizon_vibe_image_6ac9cd64.png',
            'celebration': 'snow'
        },
        'D': {
            'title': '🌙 Midnight Current',
            'description': "You're magnetic, intuitive, and maybe a little mysterious. You're pulling energy toward you without saying a word — transformation's brewing.",
            'image': 'attached_assets/generated_images/Midnight_Current_vibe_image_1b3383c2.png',
            'celebration': 'snow'
        }
    }
    
    if len(tied_letters) == 1:
        result = mood_results[tied_letters[0]]
        return result['title'], result['description'], result['image'], result['celebration'], tied_letters[0]
    else:
        tied_letters.sort()
        mood_names = [mood_results[letter]['title'] for letter in tied_letters]
        mood_titles = " + ".join(mood_names)
        blended_description = f"You're in a blended state between {' and '.join(mood_names)}. Your energy is multifaceted right now — embracing multiple vibes at once."
        first_letter_image = mood_results[tied_letters[0]]['image']
        return mood_titles, blended_description, first_letter_image, 'balloons', None

st.title("🌙 What's Your Current Vibe?")
st.markdown("### A mood-coded quiz — answer instinctively, not logically.")

st.markdown("---")

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:
    with st.form("mood_quiz"):
        q1 = st.radio(
            "**1️⃣ Pick a sky:**",
            ['A) Pale pink dawn, soft and sleepy', 
             'B) Thunderclouds rolling in, electric and loud', 
             'C) Indigo twilight, one star showing', 
             'D) Midday blue, too bright to think'],
            key='q1'
        )
        
        q2 = st.radio(
            "**2️⃣ A song starts playing — what instrument do you hear first?**",
            ['A) A low bassline that hums through your chest', 
             'B) A violin trembling with emotion', 
             'C) Distant drums from another room', 
             'D) Synth notes that sound like falling stars'],
            key='q2'
        )
        
        q3 = st.radio(
            "**3️⃣ You walk into an empty room. What's the temperature of it?**",
            ['A) Cool, almost silver', 
             'B) Warm with sunlight and dust', 
             'C) Slightly too cold — but awake', 
             'D) The air feels charged, like something\'s about to happen'],
            key='q3'
        )
        
        q4 = st.radio(
            "**4️⃣ Pick a texture:**",
            ['A) Velvet', 
             'B) Denim', 
             'C) Glass', 
             'D) Smoke'],
            key='q4'
        )
        
        q5 = st.radio(
            "**5️⃣ You're handed a drink. What does it taste like?**",
            ['A) Cinnamon and honey', 
             'B) Black coffee with a spark of citrus', 
             'C) Mint and melting ice', 
             'D) Something floral you can\'t name'],
            key='q5'
        )
        
        q6 = st.radio(
            "**6️⃣ Choose the phrase that feels right right now:**",
            ['A) "Everything\'s in motion."', 
             'B) "I could vanish or bloom."', 
             'C) "Let\'s see what burns."', 
             'D) "Quiet is a kind of power."'],
            key='q6'
        )
        
        submitted = st.form_submit_button("✨ Reveal My Vibe ✨", width='stretch')
        
        if submitted:
            st.session_state.submitted = True
            answers = {
                'q1': q1[0],
                'q2': q2[0],
                'q3': q3[0],
                'q4': q4[0],
                'q5': q5[0],
                'q6': q6[0]
            }
            st.session_state.answers = answers
            st.rerun()

if st.session_state.submitted:
    mood_title, mood_description, mood_image, celebration, mood_letter = calculate_mood(st.session_state.answers)
    
    with st.spinner('Revealing your vibe...'):
        time.sleep(1)
    
    if celebration == 'balloons':
        st.balloons()
    else:
        st.snow()
    
    st.markdown(f"""
        <div class="result-container">
            <div style="background-color: #d4edda; border-left: 4px solid #28a745; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                <h3 style="margin: 0; color: #155724;">✨ Your Vibe Revealed ✨</h3>
            </div>
            <h2 style="margin: 20px 0;">{mood_title}</h2>
            <p style="font-size: 1.1rem; line-height: 1.6;">{mood_description}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.image(mood_image, width='stretch')
    
    st.markdown("---")
    if st.button("✨ Take Quiz Again ✨", width='stretch'):
        st.session_state.submitted = False
        st.rerun()
