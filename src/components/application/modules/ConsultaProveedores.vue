<template>
  <div>
    <h1>Consulta de proveedores</h1>
    <!-- <form action="" class="search-form">
      <div class="input-container input-container--search">
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
    </form> -->
    <table class="scroll-table">
      <table class="table">
        <thead>
          <tr class="table__header">
            <th class="table__header-item">Nombre</th>
            <th class="table__header-item">Contacto</th>
            <th class="table__header-item">Correo electrónico</th>
            <th class="table__header-item">Acciones</th>
          </tr>
        </thead>
        <tbody class="table__body">
          <tr v-for="(provider, index) in userProviders" :key="index">
            <td class="table__body-item">{{ provider.p_name }}</td>
            <td class="table__body-item">{{ provider.p_telephone }}</td>
            <td class="table__body-item">{{ provider.p_email }}</td>
            <td class="table__body-item">
              <button class="edit-btn" @click="openEditProviderModal(index)">
                <ges-icon icon="edit" size="lg"></ges-icon>
              </button>
              <button
                type="button"
                class="close-btn"
                @click="deleteProvider(provider.p_name)"
              >
                <ges-icon size="lg" icon="trash-alt"></ges-icon>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </table>
    <ModalEditProvider
      v-show="isModalVisible"
      @close="closeModal"
      v-bind="editProvider"
    >
    </ModalEditProvider>
  </div>
</template>
<script>
import axios from "axios";
import jwt_decode from "jwt-decode";
import ModalEditProvider from "../modals/ModalEditProvider.vue";
export default {
  name: "consultaProveedores",
  components: {
    ModalEditProvider,
  },
  data: function () {
    return {
      provider: {
        p_name: "",
        p_telephone: "",
        p_email: "",
      },
      userProviders: [],
      editProvider: {},
      isModalVisible: false,
    };
  },
  methods: {
    getUserProviders: function () {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      axios
        .get(`https://gestify-be.herokuapp.com/user/${userId}/providers`, {
          headers: { Authorization: `Bearer ${userToken}` },
        })
        .then((result) => {
          this.userProviders = result.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    openEditProviderModal(providerId) {
      this.isModalVisible = true;
      this.editProvider = this.userProviders[providerId];
    },
    closeModal() {
      this.isModalVisible = false;
    },

    deleteProvider(providerCodeDelete) {
      let userToken = localStorage.getItem("token_access");
      let userId = jwt_decode(userToken).user_id.toString();
      let providerId = providerCodeDelete.toString();
      axios
        .delete(
          `https://gestify-be.herokuapp.com/user/${userId}/providers/${providerId}`,
          {
            headers: { Authorization: `Bearer ${userToken}` },
          }
        )
        .then((result) => {
          alert("Proveedor eliminado con éxito");
          this.$router.go();
        })
        .catch((error) => {
          console.log(error);
          alert("Falló eliminación de proveedor");
        });
    },
  },
  beforeMount() {
    this.getUserProviders();
  },
};
</script>