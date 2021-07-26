import streamlit as st
from sklearn.model_selection import train_test_split
from functions.model_functions import Mnb
from functions.viz_functions import display_confusion_matrix

def display_model(data_final) :
    # Setup model
    st.header('Modèle Multinomial Naives Bayes')
    st.write('''Le MNB est un modèle utilisé pour les classifications avec des caractéristiques discrètes 
             (par exemple, le nombre de mots pour la classification de texte).''')

    data_load_state = st.text('Loading data...')
    
    # Training model on train_set and prediction on test_set
    sms_train, sms_test, label_train, label_test = train_test_split(data_final["text"], data_final["spam"], test_size=0.3, random_state=5)
    model = Mnb(sms_train, label_train)
    pred_test_MNB_tfidfvec= model.predict(sms_test)
    pred_test_MNB_tfidfvec_score = model.score(sms_test, label_test)
    
    st.write('Précision du modèdle (accuracy) :')
    st.write(pred_test_MNB_tfidfvec_score)
    
    # Display confusion matrix
    st.subheader('Matrice de confusion')
    fig = display_confusion_matrix(label_test, pred_test_MNB_tfidfvec)
    st.pyplot(fig)
  
    data_load_state.text('Loading data...DONE!')