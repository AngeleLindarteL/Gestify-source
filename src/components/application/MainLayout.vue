<template>
  <div class="main-layout">
    <nav class="sidenav">
      <div class="sidenav-content">
        <h1>Gestify</h1>
        <details
          v-for="option in options"
          :key="option"
          class="sidenav-options"
        >
          <summary class="sidenav-options__summary">
            <ges-icon icon="chevron-right"></ges-icon>
            <span> {{ option.title }}</span>
          </summary>
          <ul class="sidenav-list">
            <li
              v-for="subitem in option.children"
              :key="subitem"
              class="sidenav-list__subitem"
            >
                <router-link :to="subitem.url" class="sidenav-list__link"> {{subitem.name}} </router-link>
            </li>
          </ul>
        </details>
      </div>
    </nav>
    <div class="main-content">
      <div class="main-component">
        <router-view> </router-view>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "mainLayout",
  data: () => {
    return {
      options: [
        {
          title: "Inventario",
          children: [
            {
              name: "Registro de inventario",
              url: "/dashboard/registro-inventario",
            },
            {
              name: "Consultar inventario",
              url: "/dashboard/consulta-inventario",
            },
          ],
        },
        {
          title: "Proveedores",
          children: [
            {
              name: "Registro de proveedores",
              url: "/dashboard/registro-proveedores",
            },
            {
              name: "Consultar proveedores",
              url: "/dashboard/consultar-proveedores",
            },
          ],
        },
        {
          title: "Productos",
          children: [
            {
              name: "Ingreso de producto",
              url: "/dashboard/registro-productos",
            },
            {
              name: "Listado de productos",
              url: "/dashboard/consultar-proveedores",
            },
          ],
        },
        {
          title: "Categorías",
          children: [
            {
              name: "Crear categoría",
              url: "/dashboard/registro-categorias",
            },
            {
              name: "Listado de categorías",
              url: "/dashboard/consultar-proveedores",
            },
          ],
        },
      ],
    };
  },
  methods: {
    //   function: sendToModule(option) {
    //       this.
    //   };
    sendToModule: function (subitem) {
      console.log(subitem);
      let urlName = subitem.url;
      console.log(urlName);
      this.$router.push({ name: subitem.url });
    },
  },
};
</script>