import { createApp } from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

import router from './router'
import App from './App.vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

const app = createApp(App)
app.use(router)
app.use(VueAxios, axios)

const slug =
  (window.P2L && window.P2L.gameSlug) ||
  document.getElementById('app')?.dataset?.game ||
  ''

const desiredPath = slug ? `/${slug}/` : null

router.isReady().then(() => {
  if (desiredPath && router.currentRoute.value.path !== desiredPath) {
    if (router.getRoutes().some(r => r.path === desiredPath)) {
      router.replace(desiredPath)
    }
  }
  app.mount('#app')

})
