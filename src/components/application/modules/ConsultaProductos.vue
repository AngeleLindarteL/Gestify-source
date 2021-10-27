<template>
  <div>
    <h1>Consulta de Productos</h1>
    <form action="" class="register-form">
      <div class="input-container">
        <label for="search" class="input-container__label">Buscar</label>
        <input
          type="text"
          class="input-container__input"
          name="search"
          id="search"
          required
        />
        <small>Puedes buscar por código o nombre del producto</small>
      </div>
    </form>
    <table class="table">
      <thead>
        <tr class="table__header">
          <th class="table__header-item">Código</th>
          <th class="table__header-item">Nombre</th>
          <th class="table__header-item">Stock</th>
          <th class="table__header-item">Proveedor</th>
          <th class="table__header-item">Categoría</th>
          <th class="table__header-item">Costo unitario</th>
          <th class="table__header-item">Acciones</th>
        </tr>
      </thead>
      <tbody class="table__body">
        <tr v-for="product in userProducts" :key="product">
          <td class="table__body-item">{{product.code}}</td>
          <td class="table__body-item">{{product.p_name}}</td>
          <td class="table__body-item">{{product.quantity}}</td>
          <td class="table__body-item">{{product.prov_name}}</td>
          <td class="table__body-item">{{product.category}}</td>
          <td class="table__body-item">{{product.price}}</td>
          <td class="table__body-item">
            <ges-icon icon="trash-alt"></ges-icon>
            <ges-icon icon="edit"></ges-icon>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";
import jwt_decode from "jwt-decode";

export default {
  name: "consultaProductos",
  data: function () {
    return {
      product: {
        code: "",
        prov_name: "",
        p_name: "",
        quantity: "",
        movement: "Entrada",
        price: "",
        category: "",
        description: "",
      },
      userProducts: [],
    };
  },
  methods: {
    getUserProducts: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      axios
        .get(
          `https://gestify-be.herokuapp.com/user/${userId}/products`,
          {
            headers: { Authorization: `Bearer ${userToken}` },
          }
        )
        .then((result) => {
          console.log(result);
          this.userProducts = result.data;
          console.log(this.userProducts);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  beforeMount() {
    this.getUserProducts();
  },
};
</script>