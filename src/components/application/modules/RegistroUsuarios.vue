<template>
  <div>
    <h1 class="form-title">Registro Proveedores</h1>
    <form v-on:submit.prevent="createUser">
      <div class="register-form">
        <div class="input-container">
          <label for="name" class="input-container__label"
            >Nombre completo</label
          >
          <input
            type="text"
            class="input-container__input"
            name="name"
            id="name"
            v-model="user.name"
            required
          />
        </div>
        <div class="input-container">
          <label for="username" class="input-container__label"
            >Nombre de usuario</label
          >
          <input
            type="text"
            class="input-container__input"
            name="username"
            id="username"
            v-model="user.username"
            required
          />
        </div>
        <div class="input-container">
          <label for="email" class="input-container__label"
            >Correo electrónico</label
          >
          <input
            type="email"
            class="input-container__input"
            name="email"
            id="email"
            v-model="user.email"
            required
          />
        </div>
      </div>
      <button type="submit" class="primary-btn primary-btn--margin">Crear usuario</button>
    </form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "registroUsuarios",
  data: function () {
    return {
      user: {
        name: "",
        username: "",
        email: "",
        password: "TiendasYa2021*",
      },
    };
  },

  methods: {
    createUser: function () {
      axios
        .post("https://gestify-be.herokuapp.com/user", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          alert("Usuario creado con éxito")
          this.$router.go();
        })
        .catch((error) => {
          console.error(error);
          alert("Falló el registro");
        });
    },
    clearData: function () {
      this.user.name = "";
      this.user.username = "";
      this.user.email = "";
    },
  },
};
</script>