import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import * as VueGoogleMaps from 'vue2-google-maps'


Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyD3oyqqwQrUmSYNvwK8ymFVrdM1koZUWCg',
    libraries: 'places' // necessary for places input
  }
});

new Vue({
  render: h => h(App)
}).$mount('#app')
