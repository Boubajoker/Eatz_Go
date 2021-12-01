const downlaod_btn = document.querySelector('#downlaod_btn');
const dark_mod_btn = document.querySelector('#dark_mod_btn');
const light_mod_btn = document.querySelector('#light_mod_btn');
const main_theme_btn = document.querySelector("#main_theme_btn");
const doc_txt = document.querySelector("#a_1");

document.body.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
document.body.style.fontFamily = "Arial";

downlaod_btn.addEventListener('click', () => {
    window.open("assets/others/Eatz_Go.zip")
});
dark_mod_btn.addEventListener('click', () => {
    document.body.style.backgroundColor = "#000"
});
light_mod_btn.addEventListener('click', () => {
    document.body.style.backgroundColor = "#fff"
});
main_theme_btn.addEventListener('click', () => {
    document.body.style.backgroundColor = "rgba(0, 0, 0, 0.5)"
});