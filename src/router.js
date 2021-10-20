import { createRouter, createWebHashHistory } from 'vue-router'
import App from "./App.vue"
import LogIn from "./components/LogIn.vue"
import HomePage from "./components/HomePage.vue"
import MainLayout from "./components/application/MainLayout.vue"
import RegistroProveedores from "./components/application/modules/RegistroProveedores.vue"
import ConsultaProveedores from "./components/application/modules/ConsultaProveedores.vue"
import RegistroInventario from "./components/application/modules/RegistroInventario.vue"
import ConsultaInventario from "./components/application/modules/ConsultaInventario.vue"

const routes = [{
        path: '/',
        name: 'homePage',
        component: HomePage
    },
    {
        path: '/user/login',
        name: 'logIn',
        component: LogIn
    },
    {
        path: '/dashboard',
        name: 'mainLayout',
        component: MainLayout,
        children: [{
                path: 'registro-proveedores',
                component: RegistroProveedores,
            },
            {
                path: 'consultar-proveedores',
                component: ConsultaProveedores,
            },
            {
                path: 'registro-inventario',
                component: RegistroInventario,
            },
            {
                path: 'consulta-inventario',
                component: ConsultaInventario,
            },
        ],
    },
    // {
    //     path: '/userauth/registro-proveedores',
    //     name: 'registroProveedores',
    //     component: RegistroProveedores
    // }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router