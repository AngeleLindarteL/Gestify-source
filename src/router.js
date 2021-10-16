import { createRouter, createWebHashHistory } from 'vue-router'
import App from "./App.vue"
import LogIn from "./components/LogIn.vue"
import HomePage from "./components/HomePage.vue"

const routes = [{
        path: '/',
        name: 'homePage',
        component: HomePage
    },
    {
        path: '/user/login',
        name: 'logIn',
        component: LogIn
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router