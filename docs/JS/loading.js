'use strict';

let main_data = fetch('./home.html')
let data_loading_text = document.querySelector("#data_loading_text");
let loading_texts = {
    loading_text_01 : 'Initialazing...',
    loading_text_02 : 'Loading assets...',
    loading_text_03 : 'Loading styles and scripts...',
    loading_text_04 : 'Getting Things ready...',
    loading_text_05 : 'Ready!!'
};

console.log("[INFO]: Launched PyBlackEditor V0.0.1 Alpha A-1.");

//class `SiteData`
class SiteData {
    //function `update_load_data`
    update_load_data(min_time=0, max_time=0) {
        setTimeout(()=>{
            main_data.then(
                data_loading_text.innerText = loading_texts.loading_text_01,
                console.log('[INFO]: Loaded \`home.html\`')
            );
        }, min_time);
        setTimeout(()=>{
            fetch('./assets/icon/favicon.ico')
            .then(
                data_loading_text.innerText = loading_texts.loading_text_02,
                console.log('[INFO]: Loaded \`./assets/icon/favicon.ico\`')
            );
            fetch('./assets/others/Eatz_Go.zip')
            .then(
                data_loading_text.innerText = loading_texts.loading_text_02,
                console.log('[INFO]: Loaded \`./assets/others/Eatz_Go.zip\`')
            );
        }, 1100);
        setTimeout(()=>{
            fetch('./JS/app.js')
            .then(
                data_loading_text.innerText = loading_texts.loading_text_03,
                console.log('[INFO]: Loaded \`./JS/app.js\`')
            );
            fetch('./JS/langs_locales.js')
            .then(
                data_loading_text.innerText = loading_texts.loading_text_03,
                console.log('[INFO]: Loaded \`./JS/langs_locales.js\`')
            );
            fetch('./JS/loading.js')
            .then(
                data_loading_text.innerText = loading_texts.loading_text_03,
                console.log('[INFO]: Loaded \`./JS/loading.js\`')
            );
            fetch('./CSS/style.css')
            .then(
                data_loading_text.innerText = loading_texts.loading_text_03,
                console.log('[INFO]: Loaded \`./CSS/style.css\`')
            );
            fetch('./CSS/loading.css')
            .then(
                data_loading_text.innerText = loading_texts.loading_text_03,
                console.log('[INFO]: Loaded \`./CSS/loading.css\`')
            );
        }, 3100);
        setTimeout(()=>{
            data_loading_text.innerText = loading_texts.loading_text_04
        }, 3500);
        setTimeout(()=>{
            data_loading_text.innerText = loading_texts.loading_text_05,
            window.location = './home.html'
        }, max_time);
    };
};