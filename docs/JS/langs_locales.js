const locales = {
    "wlcm_msg_text" : "Welcome to Eatz Go online HomePage !",
    "downlaod_btn_text" : "Downlaod The Last version of EatzGo (v0.0.1 Alpha C-3), Alpha Release",
    "main_docs_title_text" : "Documentation of EatzGo",
    "question_01_text" : "How to use it ?",
    "awnser_01_text" : "Just launch <tt>EatzGo.exe</tt> file for launch EatzGo.",
    "awnser_01_bis_text" : "And that's it, the IA will prupose to you a meal !",
    "question_02_text" : "How to switch the language ?",
    "awnser_02_text" : "Just click the button <tt>switch to french (passer en français)</tt> on the bottom of the window.",
    "awnser_02_bis_text" : "And that's it, it will be switched to french !",

    "fr_wlcm_msg_text" : "Bienvenu sur la documentation web de EatzGo !",
    "fr_downlaod_btn_text" : "Télécharger la dernière version de EatzGo (v0.0.1 Alpha C-3) Realse Alpha",
    "fr_main_docs_title_text" : "Documentation de EatzGo",
    "fr_question_01_text" : "Comment l'utiliser ?",
    "fr_awnser_01_text" : "Lancez juste le fichier <tt>EatzGo.exe</tt> pour lancer EatzGo.",
    "fr_awnser_01_bis_text" : "Et c'est bon, L'IA vous proposera de quoi manger !",
    "fr_question_02_text" : "Comment changer de language ?",
    "fr_awnser_02_text" : "Appuyez seulement sur le boutton <tt>switch to french (passer en français)</tt> en bas à gauche de la fenêtre.",
    "fr_awnser_02_bis_text" : "Et c'est bon, l'app va être transcrite en français",
}
const switch_to_french_btn = document.querySelector('#switch_to_french_btn');
const wlcm_msg = document.querySelector('#welcome_title');
const downlaod_btn = document.querySelector('#downlaod_btn');
const main_docs_title = document.querySelector('#main_docs_title');
const question_01 = document.querySelector("#q_1");
const awnser_01 = document.querySelector("#a_1");
const awnser_01_bis = document.querySelector("#a_1b");
const question_02 = document.querySelector("#q_2");
const awnser_02 = document.querySelector("#a_2");
const awnser_02_bis = document.querySelector("#a_2b");

wlcm_msg.innerText = locales.wlcm_msg_text;
downlaod_btn.innerText = locales.downlaod_btn_text;
main_docs_title.innerText = locales.main_docs_title_text;
question_01.innerText = locales.question_01_text;
awnser_01.innerHTML = locales.awnser_01_text;
awnser_01_bis.innerText = locales.awnser_01_bis_text;
question_02.innerText = locales.question_02_text;
awnser_02.innerHTML = locales.awnser_02_text;
awnser_02_bis.innerText = locales.awnser_02_bis_text;

switch_to_french_btn.addEventListener('click', ()=>{
    wlcm_msg.innerText = locales.fr_wlcm_msg_text;
    downlaod_btn.innerText = locales.fr_downlaod_btn_text;
    main_docs_title.innerText = locales.fr_main_docs_title_text;
    question_01.innerText = locales.fr_question_01_text;
    awnser_01.innerHTML = locales.fr_awnser_01_text;
    awnser_01_bis.innerText = locales.fr_awnser_01_bis_text;
    question_02.innerText = locales.fr_question_02_text;
    awnser_02.innerHTML = locales.fr_awnser_02_text;
    awnser_02_bis.innerText = locales.fr_awnser_02_bis_text;
});