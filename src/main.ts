// import './assets/main.css'
import "primeflex/primeflex.css";
import "primevue/resources/themes/lara-light-green/theme.css";
import "primeicons/primeicons.css";

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ToastService from 'primevue/toastservice';
import PrimeVue from 'primevue/config'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(PrimeVue)

app.use(createPinia())

app.use(router)

app.use(ToastService);

app.mount('#app')
