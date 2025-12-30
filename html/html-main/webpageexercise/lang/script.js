const translations =  {
    en:{
        selct:"select a language",
        title:"Welcome to simple web code",
        pargr:"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Beatae nesciunt aspernatur et eum pariatur molestias amet, natus libero sunt deserunt nisi laborum corporis quos quibusdam delectus debitis praesentium repudiandae asperiores.",

    },
    ar: {
    selct: "اختر لغة",
    title: "مرحبًا بكم في موقع رمز ويب بسيط",
    pargr: "هذا فقرة نموذجية لعرض ميزة اختيار اللغة في الموقع."
},
ta: {
    selct: "ஒரு மொழியைத் தேர்ந்தெடுக்கவும்",
    title: "எளிய வலை குறியீட்டு தளத்திற்கு வரவேற்கிறோம்",
    pargr: "மொழி தேர்வு வசதியை விளக்குவதற்கான எடுத்துக்காட்டு பத்தி இது."
}


    }
const languageSelectop = document.querySelector("select");
let h1 =document.getElementById("h1");
let title =document.getElementById("title");
let par =document.getElementById("par");
languageSelectop.addEventListener("change",(event)=>{
setLanguage(event.target.value)
})
const setLanguage = (language) => {
    if (language === "ar") {
       h1.innerText = translations.ar.selct;
       title.innerText=translations.ar.title;
       par.innerText=translations.ar.pargr;
    } else if (language === "en") {
       h1.innerText = translations.en.selct;
       title.innerText=translations.en.title;
       par.innerText=translations.en.pargr;
    } else if (language === "ta") {
      h1.innerText = translations.ta.selct;
       title.innerText=translations.ta.title;
       par.innerText=translations.ta.pargr;
    }
};